# -*- coding: utf-8 -*-
# © 2014 Compassion CH - Cyril Sester <csester@compassion.ch>
# © 2014 Serv. Tecnol. Avanzados - Pedro M. Baeza
# © 2015 Akretion - Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Account Banking Mandate',
    'summary': 'Banking mandates',
    'version': '7.0.0.1.1',
    'license': 'AGPL-3',
    'author': "Compassion CH, Odoo Community Association (OCA)",
    'website': 'https://github.com/OCA/bank-payment',
    'category': 'Banking addons',
    'depends': ['account_payment'],
    'external_dependencies': {},
    'data': [
        'views/account_banking_mandate_view.xml',
        'views/account_invoice_view.xml',
        'views/account_payment_view.xml',
        'views/res_partner_bank_view.xml',
        'data/mandate_reference_sequence.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'test': ['test/banking_mandate.yml'],
    'description': '''
    This module adds a generic model for banking mandates.
    These mandates can be specialized to fit any banking mandates (such as
    sepa or lsv).

    A banking mandate is attached to a bank account and represents an
    authorization that the bank account owner gives to a company for a
    specific operation (such as direct debit).
    You can setup mandates from the accounting menu or directly from a bank
    account.
''',
    'installable': True,
}
