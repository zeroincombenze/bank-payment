# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion <alexis.delattre@akretion.com>
# Copyright (C) 2014-2017 Serv. Tecnol. Avanzados - Pedro M. Baeza
# Copyright (C) 2016-2017 Antiun Ingenieria S.L. - Antonio Espinosa
# Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp import models, fields, api, exceptions, _
from .common import is_sepa_creditor_identifier_valid


class ResCompany(models.Model):
    _inherit = 'res.company'

    sepa_creditor_identifier = fields.Char(
        string='SEPA Creditor Identifier', size=35,
        help="Enter the Creditor Identifier that has been attributed to your "
             "company to make SEPA Direct Debits. This identifier is composed "
             "of :\n- your country ISO code (2 letters)\n- a 2-digits "
             "checkum\n- a 3-letters business code\n- a country-specific "
             "identifier")

    @api.multi
    @api.constrains('sepa_creditor_identifier')
    def _check_sepa_creditor_identifier(self):
        for company in self:
            if company.sepa_creditor_identifier:
                if not is_sepa_creditor_identifier_valid(
                        company.sepa_creditor_identifier):
                    raise exceptions.Warning(
                        _('Error'),
                        _("Invalid SEPA Creditor Identifier."))
