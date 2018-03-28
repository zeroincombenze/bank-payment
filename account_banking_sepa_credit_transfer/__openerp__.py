# -*- coding: utf-8 -*-
#    Copyright (C) 2010-2017 Akretion (http://www.akretion.com)
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

{
    'name': 'Account Banking SEPA Credit Transfer',
    'summary': 'Create SEPA XML files for Credit Transfers',
    'version': '7.0.0.2.1',
    'license': 'AGPL-3',
    'author': "Akretion,Odoo Community Association (OCA)",
    'website': 'http://www.akretion.com',
    'category': 'Banking addons',
    'depends': ['account_banking_pain_base'],
    'external_dependencies': {
        'python': ['unidecode', 'lxml'],
    },
    'data': [
        'views/account_banking_sepa_view.xml',
        'wizard/export_sepa_view.xml',
        'data/payment_type_sepa_sct.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['sepa_credit_transfer_demo.xml'],
    'description': '''
Module to export payment orders in SEPA XML file format.

SEPA PAIN (PAyment INitiation) is the new european standard for
Customer-to-Bank payment instructions.

This module implements SEPA Credit Transfer (SCT), more specifically PAIN
versions 001.001.02, 001.001.03, 001.001.04 and 001.001.05.
It is part of the ISO 20022 standard, available on http://www.iso20022.org.

The Implementation Guidelines for SEPA Credit Transfer published by the
European Payments Council (http://http://www.europeanpaymentscouncil.eu)
use PAIN version 001.001.03, so it's probably the version of PAIN that you
should try first.

This module uses the framework provided by the banking addons,
cf https://www.github.com/OCA/banking-addons

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com>
for any help or question about this module.
    ''',
    'test': ['test/pay_invoice.yml', ],
    'installable': True,
}
