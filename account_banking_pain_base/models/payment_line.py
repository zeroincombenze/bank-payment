# -*- coding: utf-8 -*-
#    Copyright (C) 2013-2017 Akretion (http://www.akretion.com)
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp.osv import orm, fields


class payment_line(orm.Model):
    _inherit = 'payment.line'

    def _get_struct_communication_types(self, cr, uid, context=None):
        return [('ISO', 'ISO')]

    _columns = {
        'priority': fields.selection(
            [
                ('NORM', 'Normal'),
                ('HIGH', 'High'),
            ],
            'Priority',
            help="This field will be used as the 'Instruction Priority' in "
            "the generated PAIN file."),
        # Update size from 64 to 140, because PAIN allows 140 caracters
        'communication': fields.char(
            'Communication', size=140, required=True,
            help="Used as the message between ordering customer and current "
            "company. Depicts 'What do you want to say to the recipient "
            "about this order ?'"),
        'struct_communication_type': fields.selection(
            _get_struct_communication_types, 'Structured Communication Type'),
    }

    _defaults = {
        'priority': 'NORM',
        'struct_communication_type': 'ISO',
    }
