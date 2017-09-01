# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion <alexis.delattre@akretion.com>
# Copyright (C) 2014-2017 Serv. Tecnol. Avanzados - Pedro M. Baeza
# Copyright (C) 2016-2017 Antiun Ingenieria S.L. - Antonio Espinosa
# Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

{
    'name': 'Account Banking SEPA Direct Debit',
    'summary': 'Create SEPA files for Direct Debit',
    'version': '8.0.0.5.1',
    'license': 'AGPL-3',
    'author': "Akretion, "
              "Serv. Tecnol. Avanzados - Pedro M. Baeza, "
              "Antiun Ingeniería S.L., "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/bank-payment',
    'category': 'Banking addons',
    'depends': [
        'account_direct_debit',
        'account_banking_pain_base',
        'account_banking_mandate',
    ],
    'data': [
        'views/account_banking_mandate_view.xml',
        'views/res_company_view.xml',
        'views/payment_mode_view.xml',
        'wizard/export_sdd_view.xml',
        'data/mandate_expire_cron.xml',
        'data/payment_type_sdd.xml',
        'data/report_paperformat.xml',
        'reports/sepa_direct_debit_mandate.xml',
        'views/report_sepa_direct_debit_mandate.xml',
    ],
    'demo': ['demo/sepa_direct_debit_demo.xml'],
    'installable': True,
}
