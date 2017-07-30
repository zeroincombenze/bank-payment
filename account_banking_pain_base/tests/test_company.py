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
INIT_PARTY_ISSUE = '1234567A'

COMPANY_BE_VAT = 'BE0123456749'
BNK_BE_BIC = 'ABERBE22'
BNK_BE_NAME = 'ABK Bank - Antwerpen'
BNK_BE_IBAN = 'BE71096123456769'
BNK_BE_CCI = 'BE81ZZZ0123456749'
BNK_BE = {
    'vat': COMPANY_BE_VAT,
    'bic': BNK_BE_BIC,
    'name': BNK_BE_NAME,
    'iban': BNK_BE_IBAN,
    'cci': BNK_BE_CCI,
}

COMPANY_CH_VAT = 'CHE123456789'
BNK_CH_BIC = 'AXIPCHZZARG'
BNK_CH_NAME = 'AXA Versicherungen AG - Zurich'
BNK_CH_IBAN = 'CH5604835012345678009'
BNK_CH_CCI = 'CH13ZZZ00000012345'
BNK_CH = {
    'vat': COMPANY_CH_VAT,
    'bic': BNK_CH_BIC,
    'name': BNK_CH_NAME,
    'iban': BNK_CH_IBAN,
    'cci': BNK_CH_CCI,
}

COMPANY_DE_VAT = 'DE123456788'
BNK_DE_BIC = 'DEUTDEDD310'
BNK_DE_NAME = 'Deutsche Bank AG - Moenchengladbach'
BNK_DE_IBAN = 'DE91100000000123456789'
BNK_DE_CCI = 'DE50ZZZ00123456789'
BNK_DE = {
    'vat': COMPANY_DE_VAT,
    'bic': BNK_DE_BIC,
    'name': BNK_DE_NAME,
    'iban': BNK_DE_IBAN,
    'cci': BNK_DE_CCI,
}

COMPANY_ES_VAT = 'ESA12345674'
BNK_ES_BIC = 'BSCHESMMCLS'
BNK_ES_NAME = 'Banco Santander S.A. - Madrid'
BNK_ES_IBAN = 'ES7921000813610123456789'
BNK_ES_CCI = 'ES02ZZZA01234567'
BNK_ES = {
    'vat': COMPANY_ES_VAT,
    'bic': BNK_ES_BIC,
    'name': BNK_ES_NAME,
    'iban': BNK_ES_IBAN,
    'cci': BNK_ES_CCI,
}

COMPANY_FR_VAT = 'FR11123456782'
BNK_FR_BIC = 'BNABFRPPOST'
BNK_FR_NAME = 'BNP Paribas Arbitrage - Paris'
BNK_FR_IBAN = 'FR7630006000011234567890189'
BNK_FR_CCI = 'FR92ZZZ0012345678'
BNK_FR = {
    'vat': COMPANY_FR_VAT,
    'bic': BNK_FR_BIC,
    'name': BNK_FR_NAME,
    'iban': BNK_FR_IBAN,
    'cci': BNK_FR_CCI,
}

COMPANY_IT_VAT = 'IT12345670017'
BNK_IT_BIC = 'BCITITMM300'
BNK_IT_NAME = 'Intesa San Paolo Ag.7 MI'
BNK_IT_IBAN = 'IT60X0542811101000000123456'
BNK_IT_CCI = 'IT45ZZZ12345670017'
BNK_IT = {
    'vat': COMPANY_IT_VAT,
    'bic': BNK_IT_BIC,
    'name': BNK_IT_NAME,
    'iban': BNK_IT_IBAN,
    'cci': BNK_IT_CCI,
}

COMPANY_NL_VAT = 'NL123456782B90'
BNK_NL_BIC = 'INGBNL2ACLS'
BNK_NL_NAME = 'ING Bank - Amsterdam'
BNK_NL_IBAN = 'NL02ABNA0123456789'
BNK_NL_CCI = 'NL72ZZZ012345670123'
BNK_NL = {
    'vat': COMPANY_NL_VAT,
    'bic': BNK_NL_BIC,
    'name': BNK_NL_NAME,
    'iban': BNK_NL_IBAN,
    'cci': BNK_NL_CCI,
}

BNK_XX = {
    'vat': '',
    'bic': BNK_BE_BIC,
    'name': BNK_BE_NAME,
    'iban': BNK_BE_IBAN,
    'cci': BNK_BE_CCI,
}

BNK = {
    '': BNK_XX,
    'be': BNK_BE,
    'ch': BNK_CH,
    'de': BNK_DE,
    'es': BNK_ES,
    'fr': BNK_FR,
    'it': BNK_IT,
    'nl': BNK_NL,
}


class Test_company(SingleTransactionCase):
    def env789(self, model):
        """Return model pool [7.0]"""
        return self.registry(model)

    def ref789(self, model):
        """Return reference id [7.0]"""
        return self.ref(model)

    def write789(self, model, id, values):
        """Write existent record [7.0]"""
        model_pool = self.registry(model)
        return model_pool.write(self.cr, self.uid, [id], values)

    def write_ref(self, xid, values):
        """Browse and write existent record"""
        obj = self.browse_ref(xid)
        return obj.write(values)

    def create789(self, model, values):
        """Create a new record for test [7.0]"""
        return self.env789(model).create(self.cr,
                                         self.uid,
                                         values)

    def setup_company(self, country_code=None):
        """Setup company (should be customized for specific country)
        """
        self.partner_id = self.ref789('base.main_partner')
        self.company_id = self.ref789('base.main_company')
        if country_code:
            self.country_code = country_code
            xcountry = 'base.' + self.country_code
            self.country_id = self.ref789(xcountry)
        else:
            self.country_code = ''
            country_code = ''
            self.country_id = False
        vals = {'initiating_party_issuer': INIT_PARTY_ISSUE,
                'vat': BNK[country_code]['vat']}
        self.company = self.write_ref('base.main_company',
                                      vals)
        self.currency_id = self.ref789('base.EUR')
        vals = {
            'name': BNK[country_code]['name'],
            'bic': BNK[country_code]['bic'],
            'country': self.country_id,
        }
        self.bank_id = self.create789('res.bank',
                                      vals)
        vals = {
            'state': 'iban',
            'acc_number': BNK[country_code]['iban'],
            'bank': self.bank_id,
            'bank_bic': BNK[country_code]['bic'],
            'partner_id': self.partner_id,
            'company_id': self.company_id,
        }
        self.partner_bank_id = self.create789('res.partner.bank',
                                              vals)
        self.write789('res.users',
                      self.uid,
                      {'company_ids': [(4, self.company_id)]})
        self.write789('res.users',
                      self.uid,
                      {'company_id': self.company_id})
        self.partner_id = self.ref('base.res_partner_2')

    def setUp(self):
        self.setup_company()

    def test_company(self):
        cr, uid = self.cr, self.uid
        company_model = self.env789('res.company')
        for country_code in ('', 'it',):
            if country_code:
                self.setup_company(country_code=country_code)
            if self.country_code == 'be':
                val = COMPANY_BE_VAT[2:]
            elif self.country_code == 'es':
                val = BNK_ES_CCI
            else:
                val = False
            res = company_model.\
                _get_initiating_party_identifier(cr,
                                                 uid,
                                                 self.company_id)
            assert res == val, \
                'Invalid party issuer value "%s": expected "%s"' % (res,
                                                                    val)
