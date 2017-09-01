# -*- coding: utf-8 -*-
# © 2013-2015 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# © 2014 Serv. Tecnol. Avanzados - Pedro M. Baeza
# © 2016 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, api, _
from openerp.exceptions import Warning
from openerp.tools.safe_eval import safe_eval
from datetime import datetime
from lxml import etree
from openerp import tools
import logging
import base64


try:
    from unidecode import unidecode
except ImportError:
    unidecode = None

logger = logging.getLogger(__name__)


class BankingExportPain(models.AbstractModel):
    _name = 'banking.export.pain'

    @api.model
    def _validate_iban(self, iban, context=None):
        """if IBAN is valid, returns IBAN
        if IBAN is NOT valid, raises an error message"""
        if self.env['res.partner.bank'].is_iban_valid(iban):
            return iban.replace(' ', '')
        else:
            raise Warning(_("This IBAN is not valid : %s") % iban)

    def _cvt2bankcodeset(self, value, gen_args=None, context=None):
        # [antoniov: 2017-06-29] code extracted from body of prepare_field
        # SEPA uses XML ; XML = UTF-8 ; UTF-8 = support for all characters
        # But we are dealing with banks...
        # and many banks don't want non-ASCCI characters !
        # cf section 1.4 "Character set" of the SEPA Credit Transfer
        # Scheme Customer-to-bank guidelines
        if gen_args.get('convert_to_ascii'):
            # [antoniov: 2017-06-29] value may be bool
            if isinstance(value, basestring):
                value = unidecode(value)
                unallowed_ascii_chars = [
                    '"', '#', '$', '%', '&', '*', ';', '<', '>', '=', '@',
                    '[', ']', '^', '_', '`', '{', '}', '|', '~', '\\', '!']
                for unallowed_ascii_char in unallowed_ascii_chars:
                    value = value.replace(unallowed_ascii_char, '-')
            elif isinstance(value, (int, long)):            # pragma: no cover
                value = str(value)
            else:                                           # pragma: no cover
                value = ''
        return value

    @api.model
    def _prepare_field(self, field_name, field_value, eval_ctx,
                       max_size=0, gen_args=None, context=None):
        """This function is designed to be inherited !"""
        if gen_args is None:                                # pragma: no cover
            gen_args = {}
        assert isinstance(eval_ctx, dict), 'eval_ctx must contain a dict'
        try:
            value = safe_eval(field_value, eval_ctx)
            value = self._cvt2bankcodeset(value, gen_args, context=context)
        except:
            line = eval_ctx.get('line')
            if line:
                raise Warning(
                    _("Cannot compute the '%s' of the Payment Line with "
                        "reference '%s'.")
                    % (field_name, line.name))
            else:
                raise Warning(
                    _("Cannot compute the '%s'.") % field_name)
        if not isinstance(value, (str, unicode)):
            raise Warning(
                _("The type of the field '%s' is %s. It should be a string "
                    "or unicode.")
                % (field_name, type(value)))
        if not value:
            raise Warning(
                _("The '%s' is empty or 0. It should have a non-null value.")
                % field_name)
        if max_size and len(value) > max_size:              # pragma: no cover
            value = value[0:max_size]
        return value

    @api.model
    def _validate_xml(self, xml_string, gen_args, context=None):
        xsd_etree_obj = etree.parse(
            tools.file_open(gen_args['pain_xsd_file']))
        official_pain_schema = etree.XMLSchema(xsd_etree_obj)

        try:
            root_to_validate = etree.fromstring(xml_string)
            official_pain_schema.assertValid(root_to_validate)
        except Exception, e:
            logger.warning(
                "The XML file is invalid against the XML Schema Definition")
            logger.warning(xml_string)
            logger.warning(e)
            raise Warning(
                _("The generated XML file is not valid against the official "
                    "XML Schema Definition. The generated XML file and the "
                    "full error have been written in the server logs. Here "
                    "is the error, which may give you an idea on the cause "
                    "of the problem : %s")
                % unicode(e))
        return True

    @api.multi
    def _declare_sepa_file_header(
            self, xml_root, gen_args, context=None):
        xml_string = etree.tostring(
            xml_root, pretty_print=True, encoding='UTF-8',
            xml_declaration=True)
        # [antoniov: 2016-06-29] Customizing for Italian CBI
        if gen_args.get('variant_xsd') == 'CBI-IT':
            xattr = 'xsi:schemaLocation='
            xattr += '"urn:CBI:xsd:CBIPaymentRequest.00.04.00'
            xattr += ' CBIPaymentRequest.00.04.00.xsd"'
            i = xml_string.find('xmlns:')
            xml_string = xml_string[:i] + xattr + ' ' + xml_string[i:]
        logger.debug(
            "Generated SEPA XML file in format %s below"
            % gen_args['pain_flavor'])
        logger.debug(xml_string)
        return xml_string

    @api.multi
    def finalize_sepa_file_creation(
            self, xml_root, total_amount, transactions_count, gen_args,
            context=None):
        xml_string = self._declare_sepa_file_header(
            xml_root, gen_args, context=context)
        self._validate_xml(xml_string, gen_args, context=context)

        order_ref = []
        for order in self.payment_order_ids:
            if order.reference:
                order_ref.append(order.reference.replace('/', '-'))
        filename = '%s%s.xml' % (gen_args['file_prefix'], '-'.join(order_ref))

        self.write({
            'nb_transactions': transactions_count,
            'total_amount': total_amount,
            'filename': filename,
            'file': base64.encodestring(xml_string),
            'state': 'finish',
            })

        action = {
            'name': _('SEPA File'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form,tree',
            'res_model': self._name,
            'res_id': self.ids[0],
            'target': 'new',
        }
        return action

    @api.model
    def generate_group_header_block(self, parent_node, gen_args, context=None):
        group_header_1_0 = etree.SubElement(parent_node, 'GrpHdr')
        message_identification_1_1 = etree.SubElement(
            group_header_1_0, 'MsgId')
        message_identification_1_1.text = self._prepare_field(
            'Message Identification',
            'self.payment_order_ids[0].reference',
            {'self': self}, 35,
            gen_args=gen_args, context=context)
        creation_date_time_1_2 = etree.SubElement(group_header_1_0, 'CreDtTm')
        creation_date_time_1_2.text = datetime.strftime(
            datetime.today(), '%Y-%m-%dT%H:%M:%S')
        if gen_args.get('pain_flavor') == 'pain.001.001.02':
            # batch_booking is in "Group header" with pain.001.001.02
            # and in "Payment info" in pain.001.001.03/04
            batch_booking = etree.SubElement(group_header_1_0, 'BtchBookg')
            batch_booking.text = unicode(self.batch_booking).lower()
        nb_of_transactions_1_6 = etree.SubElement(
            group_header_1_0, 'NbOfTxs')
        control_sum_1_7 = etree.SubElement(group_header_1_0, 'CtrlSum')
        # Grpg removed in pain.001.001.03
        if gen_args.get('pain_flavor') == 'pain.001.001.02':
            grouping = etree.SubElement(group_header_1_0, 'Grpg')
            grouping.text = 'GRPD'
        self.generate_initiating_party_block(group_header_1_0, gen_args,
                                             context=context)
        return group_header_1_0, nb_of_transactions_1_6, control_sum_1_7

    @api.model
    def generate_start_payment_info_block(
            self, parent_node, payment_info_ident,
            priority, local_instrument, sequence_type, requested_date,
            eval_ctx, gen_args, context=None):
        payment_info_2_0 = etree.SubElement(parent_node, 'PmtInf')
        payment_info_identification_2_1 = etree.SubElement(
            payment_info_2_0, 'PmtInfId')
        payment_info_identification_2_1.text = self._prepare_field(
            'Payment Information Identification',
            payment_info_ident, eval_ctx, 35,
            gen_args=gen_args, context=context)
        payment_method_2_2 = etree.SubElement(payment_info_2_0, 'PmtMtd')
        payment_method_2_2.text = gen_args['payment_method']
        nb_of_transactions_2_4 = False
        control_sum_2_5 = False
        if gen_args.get('pain_flavor') != 'pain.001.001.02':
            batch_booking_2_3 = etree.SubElement(payment_info_2_0, 'BtchBookg')
            batch_booking_2_3.text = unicode(self.batch_booking).lower()
        # The "SEPA Customer-to-bank
        # Implementation guidelines" for SCT and SDD says that control sum
        # and nb_of_transactions should be present
        # at both "group header" level and "payment info" level
        # But not for Italy!?
            if gen_args.get('variant_xsd') != 'CBI-IT':
                nb_of_transactions_2_4 = etree.SubElement(
                    payment_info_2_0, 'NbOfTxs')
                control_sum_2_5 = etree.SubElement(payment_info_2_0, 'CtrlSum')
        payment_type_info_2_6 = etree.SubElement(
            payment_info_2_0, 'PmtTpInf')
        if priority and gen_args['payment_method'] != 'DD':
            instruction_priority_2_7 = etree.SubElement(
                payment_type_info_2_6, 'InstrPrty')
            instruction_priority_2_7.text = priority
        service_level_2_8 = etree.SubElement(
            payment_type_info_2_6, 'SvcLvl')
        service_level_code_2_9 = etree.SubElement(service_level_2_8, 'Cd')
        service_level_code_2_9.text = 'SEPA'
        if local_instrument:
            local_instrument_2_11 = etree.SubElement(
                payment_type_info_2_6, 'LclInstrm')
            local_instr_code_2_12 = etree.SubElement(
                local_instrument_2_11, 'Cd')
            local_instr_code_2_12.text = local_instrument
        if sequence_type:
            sequence_type_2_14 = etree.SubElement(
                payment_type_info_2_6, 'SeqTp')
            sequence_type_2_14.text = sequence_type

        if gen_args['payment_method'] == 'DD':
            request_date_tag = 'ReqdColltnDt'
        else:
            request_date_tag = 'ReqdExctnDt'
        requested_date_2_17 = etree.SubElement(
            payment_info_2_0, request_date_tag)
        requested_date_2_17.text = requested_date
        return payment_info_2_0, nb_of_transactions_2_4, control_sum_2_5

    @api.model
    def _must_have_initiating_party(self, gen_args):
        '''This method is designed to be inherited in localization modules for
        countries in which the initiating party is required'''
        return False

    @api.model
    def generate_initiating_party_block(self, parent_node, gen_args,
                                        context=None):
        context = {} if context is None else context
        country_code = gen_args.get('country', '')
        if country_code:
            context['country'] = country_code
        my_company_name = self._prepare_field(
            'Company Name',
            'self.payment_order_ids[0].mode.bank_id.partner_id.name',
            {'self': self}, gen_args.get('name_maxsize'), gen_args=gen_args,
            context=context)
        initiating_party_1_8 = etree.SubElement(parent_node, 'InitgPty')
        initiating_party_name = etree.SubElement(initiating_party_1_8, 'Nm')
        initiating_party_name.text = my_company_name
        payment = self.payment_order_ids[0]
        initiating_party_identifier = (
            payment.mode.initiating_party_identifier or
            payment.company_id.initiating_party_identifier)
        initiating_party_issuer = (
            payment.mode.initiating_party_issuer or
            payment.company_id.initiating_party_issuer)
        if not initiating_party_issuer:
            initiating_party_issuer = self.env['res.company'].\
                _initiating_party_issuer_default(
                context=context)
        if initiating_party_identifier and initiating_party_issuer:
            iniparty_id = etree.SubElement(initiating_party_1_8, 'Id')
            iniparty_org_id = etree.SubElement(iniparty_id, 'OrgId')
            iniparty_org_other = etree.SubElement(iniparty_org_id, 'Othr')
            iniparty_org_other_id = etree.SubElement(iniparty_org_other, 'Id')
            iniparty_org_other_id.text = initiating_party_identifier
            iniparty_org_other_issuer = etree.SubElement(
                iniparty_org_other, 'Issr')
            iniparty_org_other_issuer.text = initiating_party_issuer
        elif self._must_have_initiating_party(gen_args):
            raise Warning(
                _("Missing 'Initiating Party Issuer' and/or "
                    "'Initiating Party Identifier' for the company '%s'. "
                    "Both fields must have a value.")
                % payment.company_id.name)
        return True

    @api.model
    def generate_party_agent(
            self, parent_node, party_type, party_type_label,
            order, party_name, iban, bic, eval_ctx, gen_args, context=None):
        """Generate the piece of the XML file corresponding to BIC
        This code is mutualized between TRF and DD"""
        assert order in ('B', 'C'), "Order can be 'B' or 'C'"
        try:
            if gen_args.get('variant_xsd') == 'CBI-IT':
                if (party_type == 'Dbtr' and
                        gen_args.get('payment_method') != 'DD') or \
                        (party_type == 'Cdtr' and
                         gen_args.get('payment_method') == 'DD'):
                    party_agent = etree.SubElement(
                        parent_node, '%sAgt' % party_type)
                    party_agent_institution = etree.SubElement(
                        party_agent, 'FinInstnId')
                    party_agent_other = etree.SubElement(
                        party_agent_institution, 'ClrSysMmbId')
                    party_agent_other_identification = etree.SubElement(
                        party_agent_other, 'MmbId')
                    # TODO: insert actual ABI
                    party_agent_other_identification.text = iban[5:10]
                # Foreign Credit Transfer (bonifico Sepa Estero)
                if party_type == 'Cdtr' and iban[0:2].upper() != 'IT':
                    bic = self._prepare_field(
                        '%s BIC' % party_type_label, bic, eval_ctx,
                        gen_args=gen_args, context=context)
                    party_agent = etree.SubElement(parent_node,
                                                   '%sAgt' % party_type)
                    party_agent_institution = etree.SubElement(
                        party_agent, 'FinInstnId')
                    party_agent_bic = etree.SubElement(
                        party_agent_institution, 'BIC')
                    party_agent_bic.text = bic
            else:
                bic = self._prepare_field(
                    '%s BIC' % party_type_label, bic, eval_ctx,
                    gen_args=gen_args, context=context)
                party_agent = etree.SubElement(parent_node,
                                               '%sAgt' % party_type)
                party_agent_institution = etree.SubElement(
                    party_agent, 'FinInstnId')
                party_agent_bic = etree.SubElement(
                    party_agent_institution, gen_args.get('bic_xml_tag'))
                party_agent_bic.text = bic
        except Warning:
            if order == 'C':
                if iban[0:2] != gen_args['initiating_party_country_code']:
                    raise Warning(
                        _('Error:'),
                        _("The bank account with IBAN '%s' of partner '%s' "
                            "must have an associated BIC because it is a "
                            "cross-border SEPA operation.")
                        % (iban, party_name))
            if order == 'B' or (
                    order == 'C' and gen_args['payment_method'] == 'DD'):
                party_agent = etree.SubElement(
                    parent_node, '%sAgt' % party_type)
                party_agent_institution = etree.SubElement(
                    party_agent, 'FinInstnId')
                party_agent_other = etree.SubElement(
                    party_agent_institution, 'Othr')
                party_agent_other_identification = etree.SubElement(
                    party_agent_other, 'Id')
                party_agent_other_identification.text = 'NOTPROVIDED'
            # for Credit Transfers, in the 'C' block, if BIC is not provided,
            # we should not put the 'Creditor Agent' block at all,
            # as per the guidelines of the EPC
        return True

    @api.model
    def generate_party_block(
            self, parent_node, party_type, order, name, iban, bic,
            eval_ctx, gen_args, sepa_credid=None, partner=None, context=None):
        """Generate the piece of the XML file corresponding to Name+IBAN+BIC
        This code is mutualized between TRF and DD"""
        assert order in ('B', 'C'), "Order can be 'B' or 'C'"
        if party_type == 'Cdtr':
            party_type_label = 'Creditor'
        elif party_type == 'Dbtr':
            party_type_label = 'Debtor'
        party_name = self._prepare_field(
            '%s Name' % party_type_label, name, eval_ctx,
            gen_args.get('name_maxsize'), gen_args=gen_args,
            context=context)
        piban = self._prepare_field(
            '%s IBAN' % party_type_label, iban, eval_ctx, gen_args=gen_args)
        viban = self._validate_iban(piban)
        # At C level, the order is : BIC, Name, IBAN
        # At B level, the order is : Name, IBAN, BIC
        if order == 'B':
            gen_args['initiating_party_country_code'] = viban[0:2]
        elif order == 'C':
            self.generate_party_agent(
                parent_node, party_type, party_type_label,
                order, party_name, viban, bic, eval_ctx, gen_args,
                context=context)
        party = etree.SubElement(parent_node, party_type)
        party_nm = etree.SubElement(party, 'Nm')
        party_nm.text = party_name

        if gen_args.get('variant_xsd') == 'CBI-IT':
            company_obj = self.payment_order_ids[0].company_id
            initiating_party_identifier = self.env['res.company'].\
                _get_initiating_party_identifier(
                    company_obj.id,
                    party_type=party_type,
                    context=context)
            if initiating_party_identifier:
                if viban[0:2] != gen_args['initiating_party_country_code'] or\
                        (partner and
                         partner.vat and
                         partner.vat[0:2].upper() != 'IT'):
                    SCT = 'crossborder'
                else:
                    SCT = 'domestic'
                if sepa_credid:
                    self.generate_creditor_scheme_identification(
                        party,
                        sepa_credid,
                        'SEPA Creditor Identifier', {'self': self},
                        'SEPA', gen_args)
                elif party_type != 'Cdtr' and \
                        gen_args.get('payment_method') != 'DD':
                    party_id = etree.SubElement(party, 'Id')
                    party_org_id = etree.SubElement(party_id, 'OrgId')
                    party_org_other = etree.SubElement(party_org_id, 'Othr')
                    party_org_other_id = etree.SubElement(party_org_other,
                                                          'Id')
                    party_org_other_id.text = initiating_party_identifier
                elif SCT == 'crossborder':
                    if partner and partner.vat:
                        party_id = etree.SubElement(party, 'Id')
                        party_org_id = etree.SubElement(party_id, 'OrgId')
                        party_org_other = etree.SubElement(party_org_id,
                                                           'Othr')
                        party_org_other_id = etree.SubElement(party_org_other,
                                                              'Id')
                        party_org_other_id.text = partner.vat
                    else:
                        party_pstladr = etree.SubElement(party, 'PstlAdr')
                        street = self._cvt2bankcodeset(partner.street,
                                                       gen_args,
                                                       context=context)
                        if street:
                            party_strt = etree.SubElement(party_pstladr,
                                                          'StrtNm')
                            party_strt.text = street
                        party_twn = etree.SubElement(party_pstladr, 'TwnNm')
                        town = self._cvt2bankcodeset(partner.city,
                                                     gen_args,
                                                     context=context)
                        party_twn.text = town
                        if not town:
                            raise Warning(
                                _('Error:'),
                                _("Partner %s w/o town" % partner.name))
                else:
                    if partner and partner.vat:
                        party_id = etree.SubElement(party, 'Id')
                        party_org_id = etree.SubElement(party_id, 'OrgId')
                        party_org_other = etree.SubElement(party_org_id,
                                                           'Othr')
                        party_org_other_id = etree.SubElement(party_org_other,
                                                              'Id')
                        party_org_other_id.text = partner.vat
                        party_org_other_issr = etree.SubElement(
                            party_org_other, 'Issr')
                        party_org_other_issr.text = 'ADE'
                    elif hasattr(partner, 'fiscalcode') and\
                            partner.fiscalcode:
                        party_id = etree.SubElement(party, 'Id')
                        party_org_id = etree.SubElement(party_id, 'OrgId')
                        party_org_other = etree.SubElement(party_org_id,
                                                           'Othr')
                        party_org_other_id = etree.SubElement(party_org_other,
                                                              'Id')
                        party_org_other_id.text = partner.fiscalcode
                        party_org_other_issr = etree.SubElement(
                            party_org_other, 'Issr')
                        party_org_other_issr.text = 'ADE'
                    else:
                        pass

        party_account = etree.SubElement(
            parent_node, '%sAcct' % party_type)
        party_account_id = etree.SubElement(party_account, 'Id')
        party_account_iban = etree.SubElement(
            party_account_id, 'IBAN')
        party_account_iban.text = viban
        if order == 'B':
            self.generate_party_agent(
                parent_node, party_type, party_type_label,
                order, party_name, viban, bic, eval_ctx, gen_args,
                context=context)
        return True

    @api.model
    def generate_remittance_info_block(self, parent_node, line, gen_args,
                                       context=None):
        remittance_info_2_91 = etree.SubElement(
            parent_node, 'RmtInf')
        if line.state == 'normal':
            remittance_info_unstructured_2_99 = etree.SubElement(
                remittance_info_2_91, 'Ustrd')
            remittance_info_unstructured_2_99.text = \
                self._prepare_field(
                    'Remittance Unstructured Information',
                    'line.communication', {'line': line}, 140,
                    gen_args=gen_args, context=context)
        else:
            if not line.struct_communication_type:
                raise Warning(
                    _("Missing 'Structured Communication Type' on payment "
                        "line with reference '%s'.")
                    % line.name)
            remittance_info_structured_2_100 = etree.SubElement(
                remittance_info_2_91, 'Strd')
            creditor_ref_information_2_120 = etree.SubElement(
                remittance_info_structured_2_100, 'CdtrRefInf')
            if gen_args.get('pain_flavor') == 'pain.001.001.02':
                creditor_ref_info_type_2_121 = etree.SubElement(
                    creditor_ref_information_2_120, 'CdtrRefTp')
                creditor_ref_info_type_code_2_123 = etree.SubElement(
                    creditor_ref_info_type_2_121, 'Cd')
                creditor_ref_info_type_issuer_2_125 = etree.SubElement(
                    creditor_ref_info_type_2_121, 'Issr')
                creditor_reference_2_126 = etree.SubElement(
                    creditor_ref_information_2_120, 'CdtrRef')
            else:
                creditor_ref_info_type_2_121 = etree.SubElement(
                    creditor_ref_information_2_120, 'Tp')
                creditor_ref_info_type_or_2_122 = etree.SubElement(
                    creditor_ref_info_type_2_121, 'CdOrPrtry')
                creditor_ref_info_type_code_2_123 = etree.SubElement(
                    creditor_ref_info_type_or_2_122, 'Cd')
                creditor_ref_info_type_issuer_2_125 = etree.SubElement(
                    creditor_ref_info_type_2_121, 'Issr')
                creditor_reference_2_126 = etree.SubElement(
                    creditor_ref_information_2_120, 'Ref')

            creditor_ref_info_type_code_2_123.text = 'SCOR'
            creditor_ref_info_type_issuer_2_125.text = \
                line.struct_communication_type
            creditor_reference_2_126.text = \
                self._prepare_field(
                    'Creditor Structured Reference',
                    'line.communication', {'line': line}, 35,
                    gen_args=gen_args, context=context)
        return True

    @api.model
    def generate_creditor_scheme_identification(
            self, parent_node, identification, identification_label,
            eval_ctx, scheme_name_proprietary, gen_args, context=None):
        csi_id = etree.SubElement(parent_node, 'Id')
        csi_privateid = etree.SubElement(csi_id, 'PrvtId')
        csi_other = etree.SubElement(csi_privateid, 'Othr')
        csi_other_id = etree.SubElement(csi_other, 'Id')
        csi_other_id.text = self._prepare_field(
            identification_label, identification, eval_ctx,
            gen_args=gen_args, context=context)
        if gen_args.get('variant_xsd') != 'CBI-IT':
            csi_scheme_name = etree.SubElement(csi_other, 'SchmeNm')
            csi_scheme_name_proprietary = etree.SubElement(
                csi_scheme_name, 'Prtry')
            csi_scheme_name_proprietary.text = scheme_name_proprietary
        return True
