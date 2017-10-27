[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=7.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=7.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/bank-payment/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Banking addons for Odoo
=======================

This project focuses on in- and export of banking communication.

This version is customized for Italian users.

[//]: # (addons)


Available addons
----------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_banking](account_banking/) | 7.0.0.0.6 | 7.0.0.0.5 | Account Banking
[account_banking_mandate](account_banking_mandate/) | 7.0.0.1.1 | :repeat: | Banking mandates
[account_banking_pain_base](account_banking_pain_base/) | 7.0.0.2.0 | 0.1 | Base module for PAIN file generation
[account_banking_payment](account_banking_payment/) | 0.1.164 | :repeat: | Account Banking - Payments
[account_banking_payment_export](account_banking_payment_export/) | 7.0.0.1.167 | 7.0.0.1.166 | Account Banking - Payments Export Infrastructure
[account_banking_sepa_credit_transfer](account_banking_sepa_credit_transfer/) | 7.0.0.2.1 | :repeat: | Create SEPA XML files for Credit Transfers
[account_banking_sepa_direct_debit](account_banking_sepa_direct_debit/) | 7.0.0.2.1 | :repeat: | Create SEPA files for Direct Debit
[account_banking_tests](account_banking_tests/) | 7.0.0.1.0 | 0.1 | Banking Addons - Tests
[account_direct_debit](account_direct_debit/) | 7.0.2.134 | :repeat: | Direct Debit
[account_iban_preserve_domestic](account_iban_preserve_domestic/) | 0.1.163 | :repeat: | Domestic bank account number
[account_payment_blocking](account_payment_blocking/) | 0.1 | :repeat: | account banking payment blocking
[account_payment_multicurrency_extension](account_payment_multicurrency_extension/) | 1.1 | :repeat: | Add an improved view for payment order
[account_payment_partner](account_payment_partner/) | 0.1 | :repeat: | Adds payment mode on partners and invoices
[account_payment_purchase](account_payment_purchase/) | 1.0 | :repeat: | Adds Bank Account and Payment Mode on Purchase Orders
[account_payment_sale](account_payment_sale/) | 1.0 | :repeat: | Adds Payment Mode on Sale Orders
[account_payment_sale_stock](account_payment_sale_stock/) | 1.0 | :repeat: | Manage Payment Mode when invoicing from picking
[account_payment_shortcut](account_payment_shortcut/) | 1.134 | :repeat: | Account Payment Invoice Selection Shortcut
[bank_statement_instant_voucher](bank_statement_instant_voucher/) | 1.0r028 | :repeat: | Bank statement instant voucher
[base_iban_bic_not_required](base_iban_bic_not_required/) | 0.1 | :repeat: | IBAN - Bic not required


Unported addons
---------------
addon | version | OCA version | summary
--- | --- | --- | ---
[account_bank_statement_tax](__unported__/account_bank_statement_tax/) | 0.1 (unported) | 0.1 | Apply a tax on bank statement lines
[account_banking_camt](__unported__/account_banking_camt/) | 0.2 (unported) | 0.2 | CAMT Format Bank Statements Import
[account_banking_fi_patu](__unported__/account_banking_fi_patu/) | 0.62 (unported) | 7.0.0.62.1 | Account Banking PATU module
[account_banking_fr_lcr](__unported__/account_banking_fr_lcr/) | 0.1 (unported) | 7.0.0.1.1 | Create French LCR CFONB files
[account_banking_iban_lookup](__unported__/account_banking_iban_lookup/) | 0.1 (unported) | 0.1 | Banking Addons - Iban lookup (legacy)
[account_banking_make_deposit](__unported__/account_banking_make_deposit/) | 1.4 (unported) | 7.0.1.4.1 | Bank Deposit Ticket
[account_banking_mt940](__unported__/account_banking_mt940/) | 1.0 (unported) | 7.0.1.0.1 | MT940
[account_banking_nl_abnamro](__unported__/account_banking_nl_abnamro/) | 0.1 (unported) | 0.1 | abnamro (NL) Bank Statements Import
[account_banking_nl_clieop](__unported__/account_banking_nl_clieop/) | 0.92 (unported) | 0.92 | Account Banking NL ClieOp
[account_banking_nl_girotel](__unported__/account_banking_nl_girotel/) | 0.62 (unported) | 0.62 | Account Banking - Girotel
[account_banking_nl_ing](__unported__/account_banking_nl_ing/) | 0.1.140 (unported) | 7.0.0.1.141 | ING (NL) Bank Statements Import
[account_banking_nl_ing_mt940](__unported__/account_banking_nl_ing_mt940/) | 1.1 (unported) | 7.0.1.1.1 | MT940 import for Dutch ING
[account_banking_nl_multibank](__unported__/account_banking_nl_multibank/) | 0.62 (unported) | 0.62 | Account Banking - NL Multibank import
[account_banking_nl_rabo_mt940](__unported__/account_banking_nl_rabo_mt940/) | 1.1 (unported) | 1.1 | MT940 import for dutch Rabobank
[account_banking_nl_triodos](__unported__/account_banking_nl_triodos/) | 0.92 (unported) | 0.92 | Triodos (NL) Bank Statements Import
[account_banking_partner_journal_account](__unported__/account_banking_partner_journal_account/) | 0.1 (unported) | 0.1 | Banking Addons - Default partner journal accounts for bank transactions
[account_banking_uk_hsbc](__unported__/account_banking_uk_hsbc/) | 0.5 (unported) | 7.0.0.5.1 | HSBC Account Banking
[account_banking_reconciliation](account_banking_reconciliation/) | 1.7 (unported) | 1.7 | Bank Account Reconciliation

[//]: # (end addons)


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Moduli aggiuntivi per Banche
============================

Progetto per la gestione dell'interfacciamento con le banche.

Differenze rispetto localizzazione ufficiale Odoo/OCA

Descrizione | Odoo Italia | OCA
--- | --- | ---
Coverage |  [![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/7.0) | [![Coverage Status](https://coveralls.io/repos/OCA/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/r/OCA/bank-payment?branch=7.0)
Test compatibilità OCA e Odoo | :x: | [Errore import decimal precision](https://github.com/OCA/OCB/issues/629)
Bonifici Italia | Si, standard CBI | No
SDD Italia | Si, standard CBI | No
account_banking_pain_base | Modifiche per CBI (Italia) | Solo EU

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under Odoo Proprietary License.
Odoo Italia Associazione distributes only code under AGPL free license.

[Odoo Italia Associazione](https://www.odoo-italia.org/) è un'Associazione senza fine di lucro
che dal 2017 sostituisce gli sviluppatori italiani di OCA che sviluppano
con Odoo Proprietary License a pagamento.

Odoo Italia Associazione distribuisce il codice esclusivamente con licenza [AGPL](http://www.gnu.org/licenses/agpl-3.0.html)

[//]: # (end copyright)


