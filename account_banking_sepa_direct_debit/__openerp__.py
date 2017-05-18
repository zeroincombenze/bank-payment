# -*- coding: utf-8 -*-
# © 2013-2016 Akretion (www.akretion.com)
# © 2014 Tecnativa - Pedro M. Baeza
# © 2016 Tecnativa - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Account Banking SEPA Direct Debit',
    'summary': 'Create SEPA files for Direct Debit',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'author': "Akretion, "
              "Tecnativa, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/bank-payment',
    'category': 'Banking addons',
    'depends': [
        'account_banking_pain_base',
        'account_banking_mandate',
    ],
    'data': [
        'views/account_banking_mandate_view.xml',
        'views/res_company_view.xml',
        'views/res_config.xml',
        'views/account_payment_mode.xml',
        'data/mandate_expire_cron.xml',
        'data/account_payment_method.xml',
        'data/report_paperformat.xml',
        'reports/sepa_direct_debit_mandate.xml',
        'views/report_sepa_direct_debit_mandate.xml',
    ],
    'demo': ['demo/sepa_direct_debit_demo.xml'],
    'post_init_hook': 'update_bank_journals',
    'installable': True,
}
