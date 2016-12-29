[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-green.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment)
[![Tech Doc](https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/dev/)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/)
[![try it](https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)

Banking addons for OpenERP
==========================

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

----

OCA, or the Odoo Community Association, is a nonprofit organization whose 
mission is to support the collaborative development of Odoo features and 
promote its widespread use.

http://odoo-community.org/


[//]: # (copyright)

----

**Odoo** is a trademark of [Odoo S.A.](https://www.odoo.com/)

**OCA**, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

**zeroincombenze®** is a trademark of [SHS-AV s.r.l.](http://www.shs-av.com/)
which distributes and promotes **Odoo** ready-to-use on its own cloud infrastructure.
[Zeroincombenze® distribution](http://wiki.zeroincombenze.org/en/Odoo)
is mainly designed for Italian law and markeplace.
Everytime, every Odoo DB and customized code can be replicated on local server.

[//]: # (end copyright)

[![chat with us](http://www.shs-av.com/wp-content/chat_with_us.png)](https://www.zeroincombenze.it/chi-siamo/contatti/)
