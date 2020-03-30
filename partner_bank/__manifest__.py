# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
{
    'name': 'partner_bank',
    'summary': 'Add bank account sheet in partner view',
    'version': '10.0.0.2',
    'category': 'Accounting & Finance',
    'author': 'SHS-AV s.r.l.',
    'website': 'https://www.zeroincombenze.it/servizi-le-imprese/',
    'depends': [
        'base',
        'base_iban',
        'account',
    ],
    'data': ['views/res_partner.xml'],
    'development_status': 'Beta',
}
