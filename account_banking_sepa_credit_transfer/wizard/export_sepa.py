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
from lxml import etree

from openerp import addons, netsvc
from openerp.osv import fields, orm
from openerp.tools.translate import _


class BankingExportSepaWizard(orm.TransientModel):
    _name = 'banking.export.sepa.wizard'
    _inherit = ['banking.export.pain']
    _description = 'Export SEPA Credit Transfer File'

    _columns = {
        'state': fields.selection(
            [
                ('create', 'Create'),
                ('finish', 'Finish'),
            ],
            'State', readonly=True),
        'batch_booking': fields.boolean(
            'Batch Booking',
            help="If true, the bank statement will display only one debit "
            "line for all the wire transfers of the SEPA XML file ; if "
            "false, the bank statement will display one debit line per wire "
            "transfer of the SEPA XML file."),
        'charge_bearer': fields.selection(
            [
                ('SLEV', 'Following Service Level'),
                ('SHAR', 'Shared'),
                ('CRED', 'Borne by Creditor'),
                ('DEBT', 'Borne by Debtor'),
            ],
            'Charge Bearer', required=True,
            help="Following service level : transaction charges are to be "
            "applied following the rules agreed in the service level and/or "
            "scheme (SEPA Core messages must use this). Shared : transaction "
            "charges on the debtor side are to be borne by the debtor, "
            "transaction charges on the creditor side are to be borne by "
            "the creditor. Borne by creditor : all transaction charges are "
            "to be borne by the creditor. Borne by debtor : all transaction "
            "charges are to be borne by the debtor."),
        'nb_transactions': fields.related(
            'file_id', 'nb_transactions', type='integer',
            string='Number of Transactions', readonly=True),
        'total_amount': fields.related(
            'file_id', 'total_amount', type='float', string='Total Amount',
            readonly=True),
        'file_id': fields.many2one(
            'banking.export.sepa', 'SEPA XML File', readonly=True),
        'file': fields.related(
            'file_id', 'file', string="File", type='binary', readonly=True),
        'filename': fields.related(
            'file_id', 'filename', string="Filename", type='char',
            size=256, readonly=True),
        'payment_order_ids': fields.many2many(
            'payment.order', 'wiz_sepa_payorders_rel', 'wizard_id',
            'payment_order_id', 'Payment Orders', readonly=True),
    }

    _defaults = {
        'charge_bearer': 'SLEV',
        'state': 'create',
    }

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
        module_path = 'account_banking_sepa_credit_transfer'
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
        xsd_file = addons.\
            get_module_resource(module_path,
                                'data',
                                xsd_file)
        if xsd_file:
            pain_xsd_file = xsd_file
        else:
            pain_xsd_file = '%s/%s/%s.xsd' % (module_path, 'data', pain_flavor)
        return pain_xsd_file, variant

    def _get_pain_tags(self, pain_flavor, variant=None):
        if pain_flavor == 'pain.001.001.02':
            bic_xml_tag = 'BIC'
            name_maxsize = 70
            root_xml_tag = 'pain.001.001.02'
        elif pain_flavor == 'pain.001.001.03':
            bic_xml_tag = 'BIC'
            # size 70 -> 140 for <Nm> with pain.001.001.03
            # BUT the European Payment Council, in the document
            # "SEPA Credit Transfer Scheme Customer-to-bank
            # Implementation guidelines" v6.0 available on
            # http://www.europeanpaymentscouncil.eu/knowledge_bank.cfm
            # says that 'Nm' should be limited to 70
            # so we follow the "European Payment Council"
            # and we put 70 and not 140
            name_maxsize = 70
            root_xml_tag = 'CstmrCdtTrfInitn'
        elif pain_flavor == 'pain.001.001.04':
            bic_xml_tag = 'BICFI'
            name_maxsize = 140
            root_xml_tag = 'CstmrCdtTrfInitn'
        elif pain_flavor == 'pain.001.001.05':
            bic_xml_tag = 'BICFI'
            name_maxsize = 140
            root_xml_tag = 'CstmrCdtTrfInitn'
        # added pain.001.003.03 for German Banks
        # it is not in the offical ISO 20022 documentations, but nearly all
        # german banks are working with this instead 001.001.03
        elif pain_flavor == 'pain.001.003.03':
            bic_xml_tag = 'BIC'
            name_maxsize = 70
            root_xml_tag = 'CstmrCdtTrfInitn'
        else:
            raise orm.except_orm(
                _('Error:'),
                _("Payment Type Code '%s' is not supported. The only "
                    "Payment Type Codes supported for SEPA Credit Transfers "
                    "are 'pain.001.001.02', 'pain.001.001.03', "
                    "'pain.001.001.04', 'pain.001.001.05' "
                    "and 'pain.001.003.03'.")
                % pain_flavor)
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

    def _get_trx_info(self, cr, uid, line, payment_info_2_0, gen_args,
                      variant=None, context=None):
        # C. Credit Transfer Transaction Info
        credit_transfer_transaction_info_2_27 = etree.SubElement(
            payment_info_2_0, 'CdtTrfTxInf')
        payment_identification_2_28 = etree.SubElement(
            credit_transfer_transaction_info_2_27, 'PmtId')
        if variant == 'CBI-IT':
            IT_instrid_2_30 = etree.SubElement(
                payment_identification_2_28, 'InstrId')
            IT_instrid_2_30.text = self._prepare_field(
                cr, uid, 'Instructions', 'line.name',
                {'line': line}, 35, gen_args=gen_args,
                context=context)
        end2end_identification_2_30 = etree.SubElement(
            payment_identification_2_28, 'EndToEndId')
        end2end_identification_2_30.text = self._prepare_field(
            cr, uid, 'End to End Identification', 'line.name',
            {'line': line}, 35, gen_args=gen_args,
            context=context)
        currency_name = self._prepare_field(
            cr, uid, 'Currency Code', 'line.currency.name',
            {'line': line}, 3, gen_args=gen_args,
            context=context)
        if variant == 'CBI-IT':
            IT_credit_transfer_transaction_info = etree.SubElement(
                credit_transfer_transaction_info_2_27, 'PmtTpInf')
            IT_catpurp_2_27 = etree.SubElement(
                IT_credit_transfer_transaction_info, 'CtgyPurp')
            IT_catpurpid_2_27 = etree.SubElement(
                IT_catpurp_2_27, 'Cd')
            # TODO: Category for other SCT type
            IT_catpurpid_2_27.text = 'SUPP'
        amount_2_42 = etree.SubElement(
            credit_transfer_transaction_info_2_27, 'Amt')
        instructed_amount_2_43 = etree.SubElement(
            amount_2_42, 'InstdAmt', Ccy=currency_name)
        instructed_amount_2_43.text = '%.2f' % line.amount_currency
        return credit_transfer_transaction_info_2_27

    def create(self, cr, uid, vals, context=None):
        payment_order_ids = context.get('active_ids', [])
        vals.update({
            'payment_order_ids': [[6, 0, payment_order_ids]],
        })
        return super(BankingExportSepaWizard, self).create(
            cr, uid, vals, context=context)

    def create_sepa(self, cr, uid, ids, context=None):
        """Creates the SEPA Credit Transfer file. That's the important code!"""
        context = {} if context is None else context
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        # Get country id for any customization
        country_id, country_code = self.pool['res.company'].\
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
            'payment_method': 'TRF',
            'pain_flavor': pain_flavor,
            'sepa_export': sepa_export,
            'file_obj': self.pool['banking.export.sepa'],
            'pain_xsd_file': pain_xsd_file,
            'variant_xsd': variant,
            'country': country_code
        }
        # pain_ns = {
        #     'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        #     None: 'urn:iso:std:iso:20022:tech:xsd:%s' % pain_flavor,
        # }
        pain_ns, root_name = self._get_nsmap(pain_xsd_file, pain_flavor)
        xml_root = etree.Element(root_name, nsmap=pain_ns)
        if root_xml_tag:
            pain_root = etree.SubElement(xml_root, root_xml_tag)
        else:
            pain_root = xml_root
        pain_03_to_05 = [
            'pain.001.001.03',
            'pain.001.001.04',
            'pain.001.001.05',
            'pain.001.003.03'
        ]
        # A. Group header
        group_header_1_0, nb_of_transactions_1_6, control_sum_1_7 = \
            self.generate_group_header_block(
                cr, uid, pain_root, gen_args, context=context)

        transactions_count_1_6 = 0
        total_amount = 0.0
        amount_control_sum_1_7 = 0.0
        lines_per_group = {}
        # key = (requested_date, priority)
        # values = list of lines as object
        today = fields.date.context_today(self, cr, uid, context=context)
        for payment_order in sepa_export.payment_order_ids:
            total_amount = total_amount + payment_order.total
            for line in payment_order.line_ids:
                priority = line.priority
                if payment_order.date_prefered == 'due':
                    requested_date = line.ml_maturity_date or today
                elif payment_order.date_prefered == 'fixed':
                    requested_date = payment_order.date_scheduled or today
                else:
                    requested_date = today
                # [antoniov: 2015-07-14] no date in past
                if requested_date < today:
                    requested_date = today
                key = (requested_date, priority)
                if key in lines_per_group:
                    lines_per_group[key].append(line)
                else:
                    lines_per_group[key] = [line]
                # Write requested_date on 'Payment date' of the pay line
                if requested_date != line.date:
                    self.pool['payment.line'].write(
                        cr, uid, line.id,
                        {'date': requested_date}, context=context)

        for (requested_date, priority), lines in lines_per_group.items():
            # B. Payment info
            payment_info_2_0, nb_of_transactions_2_4, control_sum_2_5 = \
                self.generate_start_payment_info_block(
                    cr, uid, pain_root,
                    "sepa_export.payment_order_ids[0].reference + '-' "
                    "+ requested_date.replace('-', '')  + '-' + priority",
                    priority, False, False, requested_date, {
                        'sepa_export': sepa_export,
                        'priority': priority,
                        'requested_date': requested_date,
                    }, gen_args, context=context)
            self.generate_party_block(
                cr, uid, payment_info_2_0, 'Dbtr', 'B',
                'sepa_export.payment_order_ids[0].mode.bank_id.partner_id.'
                'name',
                'sepa_export.payment_order_ids[0].mode.bank_id.acc_number',
                'sepa_export.payment_order_ids[0].mode.bank_id.bank.bic',
                {'sepa_export': sepa_export},
                gen_args, context=context)
            charge_bearer_2_24 = etree.SubElement(payment_info_2_0, 'ChrgBr')
            charge_bearer_2_24.text = sepa_export.charge_bearer
            transactions_count_2_4 = 0
            amount_control_sum_2_5 = 0.0
            for line in lines:
                transactions_count_1_6 += 1
                transactions_count_2_4 += 1
                # C. Credit Transfer Transaction Info
                # credit_transfer_transaction_info_2_27 = etree.SubElement(
                #     payment_info_2_0, 'CdtTrfTxInf')
                # payment_identification_2_28 = etree.SubElement(
                #     credit_transfer_transaction_info_2_27, 'PmtId')
                # if variant == 'CBI-IT':
                #     IT_instrid_2_30 = etree.SubElement(
                #         payment_identification_2_28, 'InstrId')
                #     IT_instrid_2_30.text = self._prepare_field(
                #         cr, uid, 'Instructions', 'line.name',
                #         {'line': line}, 35, gen_args=gen_args,
                #         context=context)
                # end2end_identification_2_30 = etree.SubElement(
                #     payment_identification_2_28, 'EndToEndId')
                # end2end_identification_2_30.text = self._prepare_field(
                #     cr, uid, 'End to End Identification', 'line.name',
                #     {'line': line}, 35, gen_args=gen_args,
                #     context=context)
                # currency_name = self._prepare_field(
                #     cr, uid, 'Currency Code', 'line.currency.name',
                #     {'line': line}, 3, gen_args=gen_args,
                #     context=context)
                # if variant == 'CBI-IT':
                #     IT_credit_transfer_transaction_info = etree.SubElement(
                #         credit_transfer_transaction_info_2_27, 'PmtTpInf')
                #     IT_catpurp_2_27 = etree.SubElement(
                #         IT_credit_transfer_transaction_info, 'CtgyPurp')
                #     IT_catpurpid_2_27 = etree.SubElement(
                #         IT_catpurp_2_27, 'Cd')
                #     # TODO: Category for other SCT type
                #     IT_catpurpid_2_27.text = 'SUPP'
                # amount_2_42 = etree.SubElement(
                #     credit_transfer_transaction_info_2_27, 'Amt')
                # instructed_amount_2_43 = etree.SubElement(
                #     amount_2_42, 'InstdAmt', Ccy=currency_name)
                # instructed_amount_2_43.text = '%.2f' % line.amount_currency
                credit_transfer_transaction_info_2_27 = self._get_trx_info(
                    cr, uid, line, payment_info_2_0, gen_args,
                    variant=variant, context=context)
                amount_control_sum_1_7 += line.amount_currency
                amount_control_sum_2_5 += line.amount_currency

                if not line.bank_id:
                    raise orm.except_orm(
                        _('Error:'),
                        _("Missing Bank Account on invoice '%s' (payment "
                            "order line reference '%s').")
                        % (line.ml_inv_ref.number, line.name))
                self.generate_party_block(
                    cr, uid, credit_transfer_transaction_info_2_27, 'Cdtr',
                    'C', 'line.partner_id.name', 'line.bank_id.acc_number',
                    'line.bank_id.bank.bic', {'line': line}, gen_args,
                    context=context)

                self.generate_remittance_info_block(
                    cr, uid, credit_transfer_transaction_info_2_27,
                    line, gen_args, context=context)

            if pain_flavor in pain_03_to_05 and variant != 'CBI-IT':
                nb_of_transactions_2_4.text = str(transactions_count_2_4)
                control_sum_2_5.text = '%.2f' % amount_control_sum_2_5

        if pain_flavor in pain_03_to_05:
            nb_of_transactions_1_6.text = str(transactions_count_1_6)
            control_sum_1_7.text = '%.2f' % amount_control_sum_1_7
        else:
            nb_of_transactions_1_6.text = str(transactions_count_1_6)
            control_sum_1_7.text = '%.2f' % amount_control_sum_1_7

        return self.finalize_sepa_file_creation(
            cr, uid, ids, xml_root, total_amount, transactions_count_1_6,
            gen_args, context=context)

    def cancel_sepa(self, cr, uid, ids, context=None):
        '''
        Cancel the SEPA file: just drop the file
        '''
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.sepa').unlink(
            cr, uid, sepa_export.file_id.id, context=context)
        return {'type': 'ir.actions.act_window_close'}

    def save_sepa(self, cr, uid, ids, context=None):
        '''
        Save the SEPA file: send the done signal to all payment
        orders in the file. With the default workflow, they will
        transition to 'done', while with the advanced workflow in
        account_banking_payment they will transition to 'sent' waiting
        reconciliation.
        '''
        sepa_export = self.browse(cr, uid, ids[0], context=context)
        self.pool.get('banking.export.sepa').write(
            cr, uid, sepa_export.file_id.id, {'state': 'sent'},
            context=context)
        wf_service = netsvc.LocalService('workflow')
        for order in sepa_export.payment_order_ids:
            wf_service.trg_validate(uid, 'payment.order', order.id, 'done', cr)
        return {'type': 'ir.actions.act_window_close'}
