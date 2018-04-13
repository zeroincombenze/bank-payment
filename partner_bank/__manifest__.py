# -*- coding: utf-8 -*-
#
# Copyright 2018,      Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2018,      Associazione Odoo Italia <https://odoo-italia.org>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'partner_bank',

    'summary': '''
        Add bank account sheet in partner view
    ''',
    'description': '''
        Add bank account sheet in partner view
    ''',

    'author': 'SHS-AV s.r.l.',
    'website': 'http://www.zeroincombenze.it',

    'category': 'Accounting & Finance',
    'version': '10.0.0.1',

    'depends': ['base', 'account'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/res_partner.xml',
    ],
}
