# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion <alexis.delattre@akretion.com>
# Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp import models, api


class BankPaymentLine(models.Model):
    _inherit = 'bank.payment.line'

    @api.multi
    def move_line_transfer_account_hashcode(self):
        """
        From my experience, even when you ask several direct debits
        at the same date with enough delay, you will have several credits
        on your bank statement: one for each mandate types.
        So we split the transfer move lines by mandate type, so easier
        reconciliation of the bank statement.
        """
        hashcode = super(BankPaymentLine, self).\
            move_line_transfer_account_hashcode()
        hashcode += '-' + unicode(self.mandate_id.recurrent_sequence_type)
        return hashcode
