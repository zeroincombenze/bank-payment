# -*- coding: utf-8 -*-
# Copyright 2014, Compassion CH (http://www.compassion.ch)
# Copyright 2017, Antonio M. Vigliotti <antoniomaria.vigliotti@gmail.com>
# Copyright 2017, Associazione Odoo Italia <https://odoo-italia.org>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
from openerp.osv import fields, orm
from openerp.tools.translate import _


class PaymentLine(orm.Model):
    _inherit = 'payment.line'

    _columns = {
        'mandate_id': fields.many2one(
            'account.banking.mandate', 'Direct Debit Mandate',
            domain=[('state', '=', 'valid')]),
    }

    def create(self, cr, uid, vals, context=None):
        ''' If the customer invoice has a mandate, take it
        otherwise, take the first valid mandate of the bank account
        '''
        context = {} if context is None else context
        if not vals:
            vals = {}
        partner_bank_id = vals.get('bank_id')
        move_line_id = vals.get('move_line_id')
        if (context.get('search_payment_order_type') == 'debit' and
                'mandate_id' not in vals):
            if move_line_id:
                line = self.pool['account.move.line'].browse(
                    cr, uid, move_line_id, context=context)
                if (line.invoice and line.invoice.type == 'out_invoice' and
                        line.invoice.mandate_id):
                    vals.update({
                        'mandate_id': line.invoice.mandate_id.id,
                        'bank_id':
                        line.invoice.mandate_id.partner_bank_id.id,
                    })
            if partner_bank_id and 'mandate_id' not in vals:
                mandate_ids = self.pool['account.banking.mandate'].search(
                    cr, uid, [
                        ('partner_bank_id', '=', partner_bank_id),
                        ('state', '=', 'valid'),
                    ], context=context)
                if mandate_ids:
                    vals['mandate_id'] = mandate_ids[0]
        return super(PaymentLine, self).create(cr, uid, vals, context=context)

    def _check_mandate_bank_link(self, cr, uid, ids):
        for payline in self.browse(cr, uid, ids):
            if (payline.mandate_id and payline.bank_id and
                    payline.mandate_id.partner_bank_id.id !=
                    payline.bank_id.id):
                raise orm.except_orm(
                    _('Error:'),
                    _("The payment line with reference '%s' has the bank "
                        "account '%s' which is not attached to the mandate "
                        "'%s' (this mandate is attached to the bank account "
                        "'%s').") %
                    (payline.name,
                     self.pool['res.partner.bank'].name_get(
                         cr, uid, [payline.bank_id.id])[0][1],
                     payline.mandate_id.unique_mandate_reference,
                     self.pool['res.partner.bank'].name_get(
                         cr, uid,
                         [payline.mandate_id.partner_bank_id.id])[0][1],)
                )
        return True

    _constraints = [
        (_check_mandate_bank_link, 'Error msg in raise',
            ['mandate_id', 'bank_id']),
    ]
