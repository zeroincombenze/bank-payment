# -*- coding: utf-8 -*-
#
# Copyright 2010-2017, Akretion (http://www.akretion.com)
# Copyright 2016-2017, SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization
#
from datetime import datetime

from lxml import etree

from openerp import netsvc
from openerp.modules.module import get_module_resource
from openerp.osv import fields, orm
from openerp.tools.translate import _


class BankingExportSddWizard(orm.TransientModel):
    _name = 'banking.export.sdd.wizard'
    _inherit = ['banking.export.pain']
    _description = 'Export SEPA Direct Debit File'
    _columns = {
        'state': fields.selection([
            ('create', 'Create'),
            ('finish', 'Finish'),
        ], 'State', readonly=True),
        'batch_booking': fields.boolean(
            'Batch Booking',
            help="If true, the bank statement will display only one credit "
            "line for all the direct debits of the SEPA file ; if false, "
            "the bank statement will display one credit line per direct "
            "debit of the SEPA file."),
        'charge_bearer': fields.selection([
            ('SLEV', 'Following Service Level'),
            ('SHAR', 'Shared'),
            ('CRED', 'Borne by Creditor'),
            ('DEBT', 'Borne by Debtor'),
        ], 'Charge Bearer', required=True,
            help="Following service level : transaction charges are to be "
            "applied following the rules agreed in the service level and/or "
            "scheme (SEPA Core messages must use this). Shared : transaction "
            "charges on the creditor side are to be borne by the creditor, "
            "transaction charges on the debtor side are to be borne by the "
            "debtor. Borne by creditor : all transaction charges are to be "
            "borne by the creditor. Borne by debtor : all transaction "
            "charges are to be borne by the debtor."),
        'nb_transactions': fields.related(
            'file_id', 'nb_transactions', type='integer',
            string='Number of Transactions', readonly=True),
        'total_amount': fields.related(
            'file_id', 'total_amount', type='float', string='Total Amount',
            readonly=True),
        'file_id': fields.many2one(
            'banking.export.sdd', 'SDD File', readonly=True),
        'file': fields.related(
            'file_id', 'file', string="File", type='binary', readonly=True),
        'filename': fields.related(
            'file_id', 'filename', string="Filename", type='char', size=256,
            readonly=True),
        'payment_order_ids': fields.many2many(
            'payment.order', 'wiz_sdd_payorders_rel', 'wizard_id',
            'payment_order_id', 'Payment Orders', readonly=True),
    }

    _defaults = {
        'charge_bearer': 'SLEV',
        'state': 'create',
    }

    def _get_trx_info(self, cr, uid, line, payment_info_2_0, sequence_type,
                      gen_args, sepa_export, bic_xml_tag,
                      variant=None, context=None):
        # C. Direct Debit Transaction Info
        dd_transaction_info_2_28 = etree.SubElement(
            payment_info_2_0, 'DrctDbtTxInf')
        payment_identification_2_29 = etree.SubElement(
            dd_transaction_info_2_28, 'PmtId')
        if variant == 'CBI-IT':
            instrid_identification_2_31 = etree.SubElement(
                payment_identification_2_29, 'InstrId')
            instrid_identification_2_31.text = self._prepare_field(
                cr, uid,
                'Instring Identification', 'line.id',
                {'line': line}, 6, gen_args=gen_args)
        end2end_identification_2_31 = etree.SubElement(
            payment_identification_2_29, 'EndToEndId')
        end2end_identification_2_31.text = self._prepare_field(
            cr, uid, 'End to End Identification', 'line.name',
            {'line': line}, 35,
            gen_args=gen_args)
        currency_name = self._prepare_field(
            cr, uid, 'Currency Code', 'line.currency.name',
            {'line': line}, 3, gen_args=gen_args,
            context=context)
        instructed_amount_2_44 = etree.SubElement(
            dd_transaction_info_2_28, 'InstdAmt', Ccy=currency_name)
        instructed_amount_2_44.text = '%.2f' % line.amount_currency
        dd_transaction_2_46 = etree.SubElement(
            dd_transaction_info_2_28, 'DrctDbtTx')
        mandate_related_info_2_47 = etree.SubElement(
            dd_transaction_2_46, 'MndtRltdInf')
        mandate_identification_2_48 = etree.SubElement(
            mandate_related_info_2_47, 'MndtId')
        mandate_identification_2_48.text = self._prepare_field(
            cr, uid, 'Unique Mandate Reference',
            'line.mandate_id.unique_mandate_reference',
            {'line': line}, 35,
            gen_args=gen_args)
        mandate_signature_date_2_49 = etree.SubElement(
            mandate_related_info_2_47, 'DtOfSgntr')
        mandate_signature_date_2_49.text = self._prepare_field(
            cr, uid, 'Mandate Signature Date',
            'line.mandate_id.signature_date',
            {'line': line}, 10,
            gen_args=gen_args)
        if sequence_type == 'FRST' and (
                line.mandate_id.last_debit_date or
                not line.mandate_id.sepa_migrated):
            previous_bank = self._get_previous_bank(
                cr, uid, line, context=context)
            if previous_bank or not line.mandate_id.sepa_migrated:
                amendment_indicator_2_50 = etree.SubElement(
                    mandate_related_info_2_47, 'AmdmntInd')
                amendment_indicator_2_50.text = 'true'
                amendment_info_details_2_51 = etree.SubElement(
                    mandate_related_info_2_47, 'AmdmntInfDtls')
            if previous_bank:
                if previous_bank.bank.bic == line.bank_id.bank.bic:
                    ori_debtor_account_2_57 = etree.SubElement(
                        amendment_info_details_2_51, 'OrgnlDbtrAcct')
                    ori_debtor_account_id = etree.SubElement(
                        ori_debtor_account_2_57, 'Id')
                    ori_debtor_account_iban = etree.SubElement(
                        ori_debtor_account_id, 'IBAN')
                    ori_debtor_account_iban.text = self._validate_iban(
                        cr, uid, self._prepare_field(
                            cr, uid, 'Original Debtor Account',
                            'previous_bank.acc_number',
                            {'previous_bank': previous_bank},
                            gen_args=gen_args,
                            context=context),
                        context=context)
                else:
                    ori_debtor_agent_2_58 = etree.SubElement(
                        amendment_info_details_2_51, 'OrgnlDbtrAgt')
                    ori_debtor_agent_institution = etree.SubElement(
                        ori_debtor_agent_2_58, 'FinInstnId')
                    ori_debtor_agent_bic = etree.SubElement(
                        ori_debtor_agent_institution, bic_xml_tag)
                    ori_debtor_agent_bic.text = self._prepare_field(
                        cr, uid, 'Original Debtor Agent',
                        'previous_bank.bank.bic',
                        {'previous_bank': previous_bank},
                        gen_args=gen_args,
                        context=context)
                    ori_debtor_agent_other = etree.SubElement(
                        ori_debtor_agent_institution, 'Othr')
                    ori_debtor_agent_other_id = etree.SubElement(
                        ori_debtor_agent_other, 'Id')
                    ori_debtor_agent_other_id.text = 'SMNDA'
                    # SMNDA = Same Mandate New Debtor Agent
            elif not line.mandate_id.sepa_migrated:
                ori_mandate_identification_2_52 = etree.SubElement(
                    amendment_info_details_2_51, 'OrgnlMndtId')
                ori_mandate_identification_2_52.text = \
                    self._prepare_field(
                        cr, uid, 'Original Mandate Identification',
                        'line.mandate_id.'
                        'original_mandate_identification',
                        {'line': line},
                        gen_args=gen_args,
                        context=context)
                ori_creditor_scheme_id_2_53 = etree.SubElement(
                    amendment_info_details_2_51, 'OrgnlCdtrSchmeId')
                self.generate_creditor_scheme_identification(
                    cr, uid, ori_creditor_scheme_id_2_53,
                    'sepa_export.payment_order_ids[0].company_id.'
                    'original_creditor_identifier',
                    'Original Creditor Identifier',
                    {'sepa_export': sepa_export},
                    'SEPA', gen_args, context=context)
        return dd_transaction_info_2_28

    def create(self, cr, uid, vals, context=None):
        payment_order_ids = context.get('active_ids', [])
        vals.update({
            'payment_order_ids': [[6, 0, payment_order_ids]],
        })
        return super(BankingExportSddWizard, self).create(
            cr, uid, vals, context=context)

    def _get_previous_bank(self, cr, uid, payline, context=None):
        payline_obj = self.pool['payment.line']
        previous_bank = False
        payline_ids = payline_obj.search(
            cr, uid, [
                ('mandate_id', '=', payline.mandate_id.id),
                ('bank_id', '!=', payline.bank_id.id),
            ],
            context=context)
        if payline_ids:
            older_lines = payline_obj.browse(
                cr, uid, payline_ids, context=context)
            previous_date = False
            previous_payline_id = False
            for older_line in older_lines:
                older_line_date_sent = older_line.order_id.date_sent
                if (older_line_date_sent and
                        older_line_date_sent > previous_date):
                    previous_date = older_line_date_sent
                    previous_payline_id = older_line.id
            if previous_payline_id:
                previous_payline = payline_obj.browse(
                    cr, uid, previous_payline_id, context=context)
                previous_bank = previous_payline.bank_id
        return previous_bank

    def _get_name_n_params(self, name, deflt=None):
        """Extract name and params from string like 'name(params)'"""
        deflt = '' if deflt is None else deflt
        i = name.find('(')
        j = name.rfind(')')
        if i >= 0 and j >= i:
            n = name[:i]
            p = name[i + 1:j]
        else:
            n = name
            p = deflt
        return n, p

    def _get_pain_file_name(self, pain_name, pain_flavor):
        """Manage variant schema (i.e. Italian banks in CBI)
        based on pain xsd file name.
        Pain_name MUST BE in form 'pain' or 'pain(variant)'
        Standard pain name is 'pain.001.001.VV.xsd' where VV is pain version,
        variant name is 'pain.001.001.VV-LLL.xsd' where LLL is variant name.
        If variant file does not exist, standard file is used"""
        xsd_file, variant = self._get_name_n_params(pain_name)
        module_path = 'account_banking_sepa_direct_debit'
        if not variant or variant == 'recommended':
            variant = ''
            xsd_file = '%s.xsd' % pain_flavor
        else:
            if variant.find('used') >= 0:
                x = variant.split(' ')
                variant = x[-1]
            if variant == 'Italy':
                variant = 'CBI-IT'
            xsd_file = '%s-%s.xsd' % (pain_flavor, variant)
        xsd_file = get_module_resource(module_path,
                                       'data',
                                       xsd_file)
        if xsd_file:
            pain_xsd_file = xsd_file
        else:
            pain_xsd_file = '%s/%s/%s.xsd' % (module_path, 'data', pain_flavor)
        return pain_xsd_file, variant

    def _get_pain_tags(self, pain_flavor, variant=None):
        if pain_flavor == 'pain.008.001.02':
            bic_xml_tag = 'BIC'
            name_maxsize = 70
            root_xml_tag = 'CstmrDrctDbtInitn'
        elif pain_flavor == 'pain.008.001.03':
            bic_xml_tag = 'BICFI'
            name_maxsize = 140
            root_xml_tag = 'CstmrDrctDbtInitn'
        elif pain_flavor == 'pain.008.001.04':
            bic_xml_tag = 'BICFI'
            name_maxsize = 140
            root_xml_tag = 'CstmrDrctDbtInitn'
        else:
            raise orm.except_orm(
                _('Error:'),
                _("Payment Type Code '%s' is not supported. The only "
                    "Payment Type Code supported for SEPA Direct Debit "
                    "are 'pain.008.001.02', 'pain.008.001.03' and "
                    "'pain.008.001.04'.") % pain_flavor)
        if variant == 'CBI-IT':
            root_xml_tag = False
        return bic_xml_tag, name_maxsize, root_xml_tag

    def _get_nsmap(self, pain_xsd_file, pain_flavor):
        """Read nsmap from xsd file TODO: best code"""
        root_name = 'Document'
        pain_ns = {
            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            None: 'urn:iso:std:iso:20022:tech:xsd:%s' % pain_flavor,
        }
        try:
            fd = open(pain_xsd_file, 'r')
            schema = fd.read()
            fd.close()
            i = schema.find('xmlns:xs=')
            j = schema.find('"', i) + 1
            k = schema.find('"', j)
            pain_ns['xsi'] = '%s-instance' % schema[j:k]
            i = schema.find('targetNamespace=')
            j = schema.find('"', i) + 1
            k = schema.find('"', j)
            pain_ns[None] = schema[j:k]
            i = schema.find('<xs:element name=')
            j = schema.find('"', i) + 1
            k = schema.find('"', j)
            root_name = schema[j:k]
        except BaseException:
            pass
        return pain_ns, root_name

    def create_sepa(self, cr, uid, ids, context=None):
        """Creates the SEPA Direct Debit file. That's the important code !"""
        context = {} if context is None else context
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        # Get country id for any customization
        country_id, country_code = self.pool.get('res.company').\
            _get_country(cr, uid,
                         sepa_export.payment_order_ids[0].company_id.id)
        pain_flavor = sepa_export.payment_order_ids[0].mode.type.code
        pain_name = sepa_export.payment_order_ids[0].mode.type.name
        convert_to_ascii = \
            sepa_export.payment_order_ids[0].mode.convert_to_ascii
        # code to manage variant schema (i.e. Italian banks in CBI)
        pain_xsd_file, variant = self._get_pain_file_name(
            pain_name, pain_flavor)
        bic_xml_tag, name_maxsize, root_xml_tag = self._get_pain_tags(
            pain_flavor, variant=variant)
        gen_args = {
            'bic_xml_tag': bic_xml_tag,
            'name_maxsize': name_maxsize,
            'convert_to_ascii': convert_to_ascii,
            'payment_method': 'DD',
            'pain_flavor': pain_flavor,
            'sepa_export': sepa_export,
            'file_obj': self.pool['banking.export.sdd'],
            'pain_xsd_file': pain_xsd_file,
            'variant_xsd': variant,
            'country': country_code
        }
        pain_ns, root_name = self._get_nsmap(pain_xsd_file, pain_flavor)
        xml_root = etree.Element(root_name, nsmap=pain_ns)
        if root_xml_tag:
            pain_root = etree.SubElement(xml_root, root_xml_tag)
        else:
            pain_root = xml_root
        # A. Group header
        group_header_1_0, nb_of_transactions_1_6, control_sum_1_7 = \
            self.generate_group_header_block(
                cr, uid, pain_root, gen_args)
        transactions_count_1_6 = 0
        total_amount = 0.0
        amount_control_sum_1_7 = 0.0
        lines_per_group = {}
        # key = (requested_date, priority, sequence type)
        # value = list of lines as objects
        # Iterate on payment orders
        today = fields.date.context_today(self, cr, uid, context=context)
        for payment_order in sepa_export.payment_order_ids:
            total_amount = total_amount + payment_order.total
            # Iterate each payment lines
            for line in payment_order.line_ids:
                transactions_count_1_6 += 1
                priority = line.priority
                if payment_order.date_prefered == 'due':
                    requested_date = line.ml_maturity_date or today
                elif payment_order.date_prefered == 'fixed':
                    requested_date = payment_order.date_scheduled or today
                else:
                    requested_date = today
                if not line.mandate_id:
                    raise orm.except_orm(
                        _('Error:'),
                        _("Missing SEPA Direct Debit mandate on the payment "
                            "line with partner '%s' and Invoice ref '%s'.")
                        % (line.partner_id.name,
                            line.ml_inv_ref.number))
                scheme = line.mandate_id.scheme
                if line.mandate_id.state != 'valid':
                    raise orm.except_orm(
                        _('Error:'),
                        _("The SEPA Direct Debit mandate with reference '%s' "
                            "for partner '%s' has expired.")
                        % (line.mandate_id.unique_mandate_reference,
                            line.mandate_id.partner_id.name))
                if line.mandate_id.type == 'oneoff':
                    if not line.mandate_id.last_debit_date:
                        seq_type = 'OOFF'
                    else:
                        raise orm.except_orm(
                            _('Error:'),
                            _("The mandate with reference '%s' for partner "
                                "'%s' has type set to 'One-Off' and it has a "
                                "last debit date set to '%s', so we can't use "
                                "it.")
                            % (line.mandate_id.unique_mandate_reference,
                                line.mandate_id.partner_id.name,
                                line.mandate_id.last_debit_date))
                elif line.mandate_id.type == 'recurrent':
                    seq_type_map = {
                        'recurring': 'RCUR',
                        'first': 'FRST',
                        'final': 'FNAL',
                    }
                    seq_type_label = \
                        line.mandate_id.recurrent_sequence_type
                    assert seq_type_label is not False
                    seq_type = seq_type_map[seq_type_label]

                key = (requested_date, priority, seq_type, scheme)
                if key in lines_per_group:
                    lines_per_group[key].append(line)
                else:
                    lines_per_group[key] = [line]
                # Write requested_exec_date on 'Payment date' of the pay line
                if requested_date != line.date:
                    self.pool['payment.line'].write(
                        cr, uid, line.id,
                        {'date': requested_date}, context=context)

        for (requested_date, priority, sequence_type, scheme), lines in \
                lines_per_group.items():
            # B. Payment info
            payment_info_2_0, nb_of_transactions_2_4, control_sum_2_5 = \
                self.generate_start_payment_info_block(
                    cr, uid, pain_root,
                    "sepa_export.payment_order_ids[0].reference + '-' + "
                    "sequence_type + '-' + requested_date.replace('-', '')  "
                    "+ '-' + priority",
                    priority, scheme, sequence_type, requested_date, {
                        'sepa_export': sepa_export,
                        'sequence_type': sequence_type,
                        'priority': priority,
                        'requested_date': requested_date,
                    }, gen_args, context=context)

            if variant == 'CBI-IT':
                self.generate_party_block(
                    cr, uid, payment_info_2_0, 'Cdtr', 'B',
                    'sepa_export.payment_order_ids[0].mode.bank_id.partner_id.'
                    'name',
                    'sepa_export.payment_order_ids[0].mode.bank_id.acc_number',
                    'sepa_export.payment_order_ids[0].mode.bank_id.bank.bic',
                    {'sepa_export': sepa_export},
                    gen_args,
                    sepa_credid='sepa_export.payment_order_ids[0].company_id.'
                                'sepa_creditor_identifier',
                    context=context)
            else:
                charge_bearer_2_24 = etree.SubElement(payment_info_2_0,
                                                      'ChrgBr')
                charge_bearer_2_24.text = sepa_export.charge_bearer
                self.generate_party_block(
                    cr, uid, payment_info_2_0, 'Cdtr', 'B',
                    'sepa_export.payment_order_ids[0].mode.bank_id.partner_id.'
                    'name',
                    'sepa_export.payment_order_ids[0].mode.bank_id.acc_number',
                    'sepa_export.payment_order_ids[0].mode.bank_id.bank.bic',
                    {'sepa_export': sepa_export},
                    gen_args,
                    context=context)
            creditor_scheme_identification_2_27 = etree.SubElement(
                payment_info_2_0, 'CdtrSchmeId')
            self.generate_creditor_scheme_identification(
                cr, uid, creditor_scheme_identification_2_27,
                'sepa_export.payment_order_ids[0].company_id.'
                'sepa_creditor_identifier',
                'SEPA Creditor Identifier', {'sepa_export': sepa_export},
                'SEPA', gen_args)
            transactions_count_2_4 = 0
            amount_control_sum_2_5 = 0.0
            for line in lines:
                transactions_count_2_4 += 1
                amount_control_sum_1_7 += line.amount_currency
                amount_control_sum_2_5 += line.amount_currency
                dd_transaction_info_2_28 = self._get_trx_info(
                    cr, uid,
                    line, payment_info_2_0, sequence_type, gen_args,
                    sepa_export, bic_xml_tag,
                    variant=variant, context=context)
                self.generate_party_block(
                    cr, uid, dd_transaction_info_2_28, 'Dbtr', 'C',
                    'line.partner_id.name',
                    'line.bank_id.acc_number',
                    'line.bank_id.bank.bic',
                    {'line': line}, gen_args)

                self.generate_remittance_info_block(
                    cr, uid, dd_transaction_info_2_28,
                    line, gen_args)
            if nb_of_transactions_2_4:
                nb_of_transactions_2_4.text = unicode(transactions_count_2_4)
            if control_sum_2_5:
                control_sum_2_5.text = '%.2f' % amount_control_sum_2_5
        nb_of_transactions_1_6.text = unicode(transactions_count_1_6)
        control_sum_1_7.text = '%.2f' % amount_control_sum_1_7

        return self.finalize_sepa_file_creation(
            cr, uid, ids, xml_root, total_amount, transactions_count_1_6,
            gen_args, context=context)

    def cancel_sepa(self, cr, uid, ids, context=None):
        '''
        Cancel the SEPA file: just drop the file
        '''
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.sdd').unlink(
            cr, uid, sepa_export.file_id.id, context=context)
        return {'type': 'ir.actions.act_window_close'}

    def save_sepa(self, cr, uid, ids, context=None):
        """Save the SEPA Direct Debit file: mark all payments in the file
        as 'sent'. Write 'last debit date' on mandate and set oneoff
        mandate to expired.
        """
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.sdd').write(
            cr, uid, sepa_export.file_id.id, {'state': 'sent'},
            context=context)
        wf_service = netsvc.LocalService('workflow')
        for order in sepa_export.payment_order_ids:
            wf_service.trg_validate(uid, 'payment.order', order.id, 'done', cr)
            mandate_ids = [line.mandate_id.id for line in order.line_ids]
            self.pool['account.banking.mandate'].write(
                cr, uid, mandate_ids,
                {'last_debit_date': datetime.today().strftime('%Y-%m-%d')},
                context=context)
            to_expire_ids = []
            first_mandate_ids = []
            for line in order.line_ids:
                if line.mandate_id.type == 'oneoff':
                    to_expire_ids.append(line.mandate_id.id)
                elif line.mandate_id.type == 'recurrent':
                    seq_type = line.mandate_id.recurrent_sequence_type
                    if seq_type == 'final':
                        to_expire_ids.append(line.mandate_id.id)
                    elif seq_type == 'first':
                        first_mandate_ids.append(line.mandate_id.id)
            self.pool['account.banking.mandate'].write(
                cr, uid, to_expire_ids, {'state': 'expired'}, context=context)
            self.pool['account.banking.mandate'].write(
                cr, uid, first_mandate_ids, {
                    'recurrent_sequence_type': 'recurring',
                    'sepa_migrated': True,
                }, context=context)
        return {'type': 'ir.actions.act_window_close'}
