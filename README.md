[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/bank-payment/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)
================================================================================================
================================================================================================

Banking addons for Odoo

This project focuses on in- and export of banking communication. The indentation below indicates
the dependency graph of the main modules.

- account_banking_payment_export - Basic export functionality of payment orders

    - account_banking_sepa_credit_transfer - Export of payment orders in SEPA format

    - account_direct_debit - Debit order infrastructure analogous to Odoo native payment orders

        - account_banking_sepa_direct_debit - Export of debit orders in SEPA format

- account_banking - Infrastructure for importing bank statements in various formats and custom (manual)
reconciliation functionality. While advanced, this functionality will be deprecated in Odoo 8.0 in favour
of (an extension of) the new, native reconciliation functionality.

    - account_banking_camt - Import of bank statements in the SEPA CAMT.053 format

A number of other modules are available for legacy format bank statement files.


[![it](http://www.shs-av.com/wp-content/it_IT.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Moduli aggiuntivi per Banche
============================

Differenze rispetto localizzazione ufficiale Odoo/OCA:

- Moduli bonifici SEPA 7.0 modificati in quanto le banche italiane non usano lo standard Sepa ma una variante definita del consorzio CBI.
- [account_banking_pain_base](https://github.com/OCA/bank-payment/tree/7.0/account_banking_pain_base) sostituito
dal modulo in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/account_banking_pain_base)
- [account_banking_payment_export](https://github.com/OCA/bank-payment/tree/7.0/account_banking_payment_export) sostituito dal modulo in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/account_banking_payment_export)
- [account_banking_sepa_credit_transfer](https://github.com/OCA/bank-payment/tree/7.0/account_banking_sepa_credit_transfer) sostituito dal modulo in [l10n-italy-supplemental](https://github.com/zeroincombenze/l10n-italy-supplemental/tree/7.0/account_banking_sepa_credit_transfer)

Modificheremo al più presto posssibile questi moduli per integrarli con i moduli standard ma, al momento, se volete gestire i bonifici Sepa con Odoo in Italia, dovete sostituire i moduli sopra elencati.


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/) (formerly OpenERP, formerly TinyERP)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be deployed on local server too.

[//]: # (end copyright)


[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
