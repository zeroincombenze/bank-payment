# -*- coding: utf-8 -*-
#
# Copyright 2018-20 - SHS-AV s.r.l. <https://www.zeroincombenze.it/>
#
# Contributions to development, thanks to:
# * Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>
#
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from odoo import models, fields


class ResPartnerBank(models.Model):
    _inherit = 'res.partner.bank'

    acc_type = fields.Selection([
        ('bank', 'Bank'),
        ('iban', 'Iban'),
        ('normal', 'Normal')],
        string='Bank Account Type')
