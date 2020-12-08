# -*- coding: utf-8 -*-
#
# Copyright 2018-21 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
#
{
    'name': 'partner_bank',
    'summary': 'Add bank account sheet in partner view',
    'version': '10.0.0.3',
    'category': 'Accounting & Finance',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'depends': [
        'base',
        'base_iban',
        'account',
    ],
    'data': [
        'views/res_partner_view.xml',
        'views/account_invoice_view.xml',
        'views/bank_view.xml',
    ],
    'development_status': 'Beta',
}
