[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=8.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/bank-payment/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

    :alt: License: AGPL-3
=========================

Account Banking - Payments Export Infrastructure

This module provide an infrastructure to export payment orders.
It includes some bug fixes and obvious enhancements to payment orders that will hopefully land in offical addons one
day.
This technical module provides the base infrastructure to export payment orders
for electronic banking. It provides the following technical features:

* a new payment.mode.type model
* payment.mode now has a mandatory type
* a better implementation of payment_mode.suitable_bank_types() based on
  payment.mode.type
* the "make payment" button launches a wizard depending on the
  payment.mode.type
* a manual payment mode type is provided as an example, with a default "do
  nothing" wizard
  
To enable the use of payment order to collect money for customers,
it adds a payment_order_type (payment|debit) as a basis of direct debit support
(this field becomes visible when account_direct_debit is installed).

Installation
------------


This module depends on:

* account_payment
* base_iban

This modules is part of the OCA/bank-payment suite.

Configuration
-------------


No configuration required.

Usage
-----

=====

This module provides a menu to configure payment order types : Accounting > Configuration > Miscellaneous > Payment Export Types 

For further information, please visit:

 * https://www.odoo.com/forum/help-1

Known issues / Roadmap
----------------------


 * no known issues
 
Bug Tracker
-----------


Bugs are tracked on `GitHub Issues <https://github.com/OCA/bank-payment/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/bank-payment/issues/new?body=module:%20account_banking_payment_export%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.


Credits
-------


[![Odoo Italia Associazione]]

### Contributors


* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Alexis de Lattre		
* Pedro M. Baeza     
* Adrien Peiffer <adrien.peiffer@acsone.eu>
* Stefan Rijnhart
* Laurent Mignon <laurent.mignon@acsone.eu>
* Alexandre Fayolle
* Danimar Ribeiro
* Erwin van der Ploeg
* Raphaël Valyi
* Sandy Carter
* Angel Moya <angel.moya@domatix.com>

### Funders

### Maintainer


.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose mission is to support the collaborative development of Odoo features and promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.

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

[//]: # (addons)

[//]: # (end addons)

[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
