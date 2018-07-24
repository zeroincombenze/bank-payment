[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=9.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=9.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=9.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/9.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment/branch/9.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-9.svg)](https://github.com/OCA/bank-payment/tree/9.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-9.svg)](http://wiki.zeroincombenze.org/en/Odoo/9.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-9.svg)](http://erp9.zeroincombenze.it)












































































[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

OCA banking payment addons for Odoo
===================================

On version 9.0, this project focus on payment interface. The indentation below 
indicates the dependency graph of the main modules.

- account_banking_payment_export - Basic export functionality of payment orders

    - account_banking_sepa_credit_transfer - Export of payment orders in SEPA format

    - account_direct_debit - Debit order infrastructure analogous to Odoo native payment orders

        - account_banking_sepa_direct_debit - Export of debit orders in SEPA format
        
Other features can now be found in these repositories:

 * https://github.com/OCA/bank-statement-import
 * https://github.com/OCA/bank-statement-reconcile

[//]: # (addons)


Available addons
----------------
addon | version | summary
--- | --- | ---
[account_banking_mandate](account_banking_mandate/) | 9.0.1.1.0 | Banking mandates
[account_banking_mandate_sale](account_banking_mandate_sale/) | 9.0.1.0.0 | Adds mandates on sale orders
[account_banking_pain_base](account_banking_pain_base/) | 9.0.1.0.0 | Base module for PAIN file generation
[account_banking_sepa_credit_transfer](account_banking_sepa_credit_transfer/) | 9.0.1.0.0 | Create SEPA XML files for Credit Transfers
[account_banking_sepa_direct_debit](account_banking_sepa_direct_debit/) | 9.0.1.0.0 | Create SEPA files for Direct Debit
[account_payment_mode](account_payment_mode/) | 9.0.1.0.0 | Account Payment Mode
[account_payment_order](account_payment_order/) | 9.0.1.2.0 | Account Payment Order
[account_payment_partner](account_payment_partner/) | 9.0.1.1.0 | Adds payment mode on partners and invoices
[account_payment_purchase](account_payment_purchase/) | 9.0.1.0.0 | Adds Bank Account and Payment Mode on Purchase Orders
[account_payment_sale](account_payment_sale/) | 9.0.1.0.0 | Adds payment mode on sale orders
[account_payment_transfer_reconcile_batch](account_payment_transfer_reconcile_batch/) | 9.0.1.0.0 | Batch Reconciliation for transfer moves


Unported addons
---------------
addon | version | summary
--- | --- | ---
[account_banking_tests](account_banking_tests/) | 8.0.0.1.0 (unported) | Banking Addons - Tests
[account_import_line_multicurrency_extension](account_import_line_multicurrency_extension/) | 8.0.1.1.0 (unported) | Add an improved view for move line import in bank statement
[account_payment_blocking](account_payment_blocking/) | 8.0.1.0.0 (unported) | Prevent invoices under litigation to be proposed in payment orders.
[account_payment_mode_term](account_payment_mode_term/) | 8.0.0.1.2 (unported) | Account Banking - Payments Term Filter
[account_voucher_killer](account_voucher_killer/) | 8.0.1.0.0 (unported) | Accounting voucher killer
[bank_statement_instant_voucher](bank_statement_instant_voucher/) | 1.0r028 (unported) | Bank statement instant voucher
[portal_payment_mode](portal_payment_mode/) | 8.0.1.0.0 (unported) | Adds payment mode ACL's for portal users

[//]: # (end addons)

----

OCA, or the Odoo Community Association, is a nonprofit organization whose 
mission is to support the collaborative development of Odoo features and 
promote its widespread use.

http://odoo-community.org/

[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on own cloud infrastructure.
[Zeroincombenze® distribution of Odoo](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Users can download from [Zeroincombenze® distribution](https://github.com/zeroincombenze/OCB) and deploy on local server.

[//]: # (end copyright)



[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
