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
            help="If active, Odoo will convert each accented character to "
            "the corresponding unaccented caracter, so that only ASCII "
            "caracters are used in the generated PAIN file."),
        'initiating_party_issuer': fields.char(
            'Initiating Party Issuer',
            siez=35,
            help="This will be used as the 'Initiating Party Issuer' in the "
                 "PAIN files generated by Odoo. If not defined, "
                 "Initiating Party Issuer from company will be used.\n"
                 "Common format (13): \n"
                 "- Country code (2, optional)\n"
                 "- Company idenfier (N, VAT)\n"
                 "- Service suffix (N, issued by bank)",
            ),
        'initiating_party_identifier': fields.char(
            'Initiating Party Identifier',
            siez=35,
            help="This will be used as the 'Initiating Party Identifier' in "
                 "the PAIN files generated by Odoo. If not defined,"
                 " Initiating Party Identifier from company will be used.\n"
                 "Common format (13): \n"
                 "- Country code (2, optional)\n"
                 "- Company idenfier (N, VAT)\n"
                 "- Service suffix (N, issued by bank)",
            ),
    }

    _defaults = {
        'convert_to_ascii': True,
    }
