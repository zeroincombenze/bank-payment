# -*- coding: utf-8 -*-
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2017: SHS-AV] Italian localization

from openerp.tests.common import SingleTransactionCase
import logging

__version__ = "0.1.1"
_logger = logging.getLogger(__name__)

RES_BIC_TAG = {
    'pain.001.001.02': 'BIC',
    'pain.001.001.03': 'BIC',
    'pain.001.001.04': 'BICFI',
    'pain.001.001.05': 'BICFI',
    'pain.001.001.04-CBI-IT': 'BICFI',
    'pain.001.003.03': 'BIC',
}

RES_MAXSIZE = {
    'pain.001.001.02': 70,
    'pain.001.001.03': 70,
    'pain.001.001.04': 140,
    'pain.001.001.05': 140,
    'pain.001.001.04-CBI-IT': 140,
    'pain.001.003.03': 70,
}

RES_ROOT_TAG = {
    'pain.001.001.02': 'pain.001.001.02',
    'pain.001.001.03': 'CstmrCdtTrfInitn',
    'pain.001.001.04': 'CstmrCdtTrfInitn',
    'pain.001.001.05': 'CstmrCdtTrfInitn',
    'pain.001.001.04-CBI-IT': 'CstmrCdtTrfInitn',
    'pain.001.003.03': 'CstmrCdtTrfInitn',
}

RES_NSMAP = {
    'pain.001.001.02': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.02'
    },
    'pain.001.001.03': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.03'
    },
    'pain.001.001.04': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.04'
    },
    'pain.001.001.05': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.001.001.05'
    },
    'pain.001.001.04-CBI-IT': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:CBI:xsd:CBIPaymentRequest.00.04.00',
    },
    'pain.001.003.03': {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        None: 'urn:iso:std:iso:20022:tech:xsd:pain.001.003.03'
    },
}

RES_ROOTNAME = {
    'pain.001.001.02': 'Document',
    'pain.001.001.03': 'Document',
    'pain.001.001.04': 'Document',
    'pain.001.001.05': 'Document',
    'pain.001.001.04-CBI-IT': 'CBIPaymentRequest',
    'pain.001.003.03': 'Document',
}


class Test_company(SingleTransactionCase):
    def env789(self, model):
        """Return model pool [8.0]"""
        return self.env[model]

    def ref789(self, model):
        """Return reference id [8.0]"""
        return self.env.ref(model).id

    def write789(self, model, id, values):
        """Write existent record [8.0]"""
        model_pool = self.env[model]
        obj = model_pool.search([('id', '=', id)])
        return obj.write(values)

    def write_ref(self, xid, values):
        """Browse and write existent record"""
        obj = self.browse_ref(xid)
        return obj.write(values)

    def create789(self, model, values):
        """Create a new record for test [8.0]"""
        model_pool = self.env[model]
        return model_pool.create(values).id

    # def setUp(self):
    #     self.setup_company()

    def test_export(self):
        export_model = self.env789('banking.export.sepa.wizard')
        for pain_id in ('pain.001.001.02', 'pain.001.001.03',
                        'pain.001.001.04', 'pain.001.001.05',
                        'pain.001.001.04-CBI-IT', 'pain.001.003.03'):
            if pain_id[-7:] == '-CBI-IT':
                pain_flavor = pain_id[0:-7]
                tvariant = pain_id[-6:]
                pain_name = '%s(%s)' % (pain_flavor, tvariant)
            else:
                pain_flavor = pain_id
                tvariant = ''
                pain_name = '%s' % pain_flavor
            tres = 'account_banking_sepa_credit_transfer/data/%s.xsd' % pain_id
            pain_xsd_file, variant = export_model._get_pain_file_name(
                pain_name, pain_flavor)
            assert pain_xsd_file.endswith(tres), \
                'Invalid pain filename "%s": expected "%s"' % (
                    pain_xsd_file, tres)
            assert variant == tvariant, \
                'Invalid variant "%s": expected "%s"' % (
                    variant, tvariant)

            bic_xml_tag, name_maxsize, root_xml_tag = \
                export_model._get_pain_tags(pain_flavor)
            assert bic_xml_tag == RES_BIC_TAG[pain_id], \
                'Invalid bic tag "%s": expected "%s"' % (
                    bic_xml_tag, RES_BIC_TAG[pain_id])
            assert root_xml_tag == RES_ROOT_TAG[pain_id], \
                'Invalid MAX SIZE "%s": expected "%s"' % (
                    root_xml_tag, RES_ROOT_TAG[pain_id])

            pain_ns, root_name = export_model._get_nsmap(pain_xsd_file,
                                                         pain_flavor)
            assert pain_ns == RES_NSMAP[pain_id], \
                'Invalid nsmap "%s": expected "%s"' % (
                    pain_ns, RES_NSMAP[pain_id])
            assert root_name == RES_ROOTNAME[pain_id], \
                'Invalid root name "%s": expected "%s"' % (
                    root_name, RES_ROOTNAME[pain_id])
