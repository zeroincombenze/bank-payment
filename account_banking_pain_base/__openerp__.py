# -*- coding: utf-8 -*-
#    Copyright (C) 2013-2017 Akretion (http://www.akretion.com)
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization
{
    'name': 'Account Banking PAIN Base Module',
    'summary': 'Base module for PAIN file generation',
    'version': '7.0.0.1.1',
    'license': 'AGPL-3',
    'author': "Akretion, Noviat,Odoo Community Association (OCA)",
    'website': 'http://openerp-community-association.org/',
    'category': 'Hidden',
    'depends': ['account_banking_payment_export',
                'account_payment'],
    'external_dependencies': {
        'python': ['unidecode', 'lxml'],
    },
    'data': [
        'views/payment_line_view.xml',
        'views/payment_mode_view.xml',
        'views/res_company_view.xml',
    ],
    'description': '''
Base module for PAIN file generation
====================================

This module contains fields and functions that are used by the module for SEPA
Credit Transfer (account_banking_sepa_credit_transfer) and SEPA Direct Debit
(account_banking_sepa_direct_debit). This module doesn't provide any
functionality by itself.

This module is part of the banking addons:
    https://www.github.com/OCA/banking-addons

This module was started during the Akretion-Noviat code sprint of
November 21st 2013 in Epiais les Louvres (France).

Module contains some pieces of code not ISO 20022 but used by Italian Banks.
    ''',
    'active': False,
    'installable': True,
}
