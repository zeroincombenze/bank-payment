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
    'name': 'Account Banking PAIN Base Module',
    'summary': 'Base module for PAIN file generation',
    'version': '8.0.0.4.0',
    'license': 'AGPL-3',
    'author': "Akretion, "
              "Serv. Tecnol. Avanzados, "
              "Odoo Community Association (OCA), "
              "Odoo Italia Associazione",
    'website': 'https://odoo-italia.org',
    'contributors': [
        'Alexis de Lattre <alexis.delattre@akretion.com>',
        'Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>',
        'Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>'
    ],
    'category': 'Hidden',
    'depends': ['account_banking_payment_export'],
    'external_dependencies': {
        'python': ['unidecode', 'lxml'],
    },
    'data': [
        'views/payment_line_view.xml',
        'views/bank_payment_line_view.xml',
        'views/payment_mode_view.xml',
        'views/res_company_view.xml',
    ],
    'description': '''
Base module for PAIN file generation
====================================

This module contains fields and functions that are used by the module for
SEPA Credit Transfer (account_banking_sepa_credit_transfer) and
SEPA Direct Debit (account_banking_sepa_direct_debit).

This module doesn’t provide any functionality by itself.

This module was started during the Akretion-Noviat code sprint of
November 21st 2013 in Epiais les Louvres (France).

It was updated by Antonio Maria Vigliotti in order to work in Italy.
    ''',
    'post_init_hook': 'set_default_initiating_party',
    'installable': True,
}
