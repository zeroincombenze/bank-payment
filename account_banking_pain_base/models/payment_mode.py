# -*- coding: utf-8 -*-
#    Copyright (C) 2013-2017 Akretion (http://www.akretion.com)
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp.osv import orm, fields


class payment_mode(orm.Model):
    _inherit = 'payment.mode'

    _columns = {
        'convert_to_ascii': fields.boolean(
            'Convert to ASCII',
            help="If active, OpenERP will convert each accented character to "
            "the corresponding unaccented caracter, so that only ASCII "
            "caracters are used in the generated PAIN file."),
    }

    _defaults = {
        'convert_to_ascii': True,
    }
