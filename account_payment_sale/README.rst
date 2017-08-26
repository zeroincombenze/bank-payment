[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-8.svg)](https://github.com/OCA/bank-payment/tree/8.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-8.svg)](http://wiki.zeroincombenze.org/en/Odoo/8.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

    :alt: License: AGPL-3
=========================

Account Payment Sale

This module should be used when the invoice is based on the sale order.

This modules adds one field on sale orders: *Payment Mode*.
This field is copied from partner to sale order and then from sale order to
customer invoice.

This module is similar to the *sale_payment* module; the main difference is
that it doesn't depend on the *account_payment_extension* module (it's not the
only module to conflict with *account_payment_extension*; all the SEPA
modules in the banking addons conflict with *account_payment_extension*.

Installation
------------



This module depends on :
* purchase
* account_payment_partner

This module is part of the OCA/bank-payment suite.

Configuration
-------------



There is nothing to configure.

Usage
-----

-----

=====

You are able to add a payment mode directly on a partner.
This payment mode is automatically associated to the sale order, then on related invoice. 
This default value could be change in a draft sale order or draft invoice.
When you create an direct debit order, only invoices related to chosen payment mode are displayed.
Invoices without any payment mode are displayed to.

For further information, please visit:

 * https://www.odoo.com/forum/help-1

Known issues / Roadmap
----------------------



 * No known issues.
 
Bug Tracker
-----------



Bugs are tracked on `GitHub Issues <https://github.com/OCA/bank-payment/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smashing it by providing a detailed and welcomed feedback
`here <https://github.com/OCA/bank-payment/issues/new?body=module:%20account_payment_sale%0Aversion:%208.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Credits
-------



[![Odoo Italia Associazione]]


### Contributors



* Pedro M. Baeza
* Alexis de Lattre
* Alexandre Fayolle
* Danimar Ribeiro
* Raphaël Valyi

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

**Odoo Italia Associazione**, or the [Associazione Odoo Italia](https://www.odoo-italia.org/)
is the nonprofit Italian Community Association whose mission
is to support the collaborative development of Odoo designed for Italian law and markeplace.
Since 2017, Odoo Italia Associazione replaces OCA members of Italy are developping code under legacy license.
Odoo Italia Associazione distributes code only under A-GPL free license.

[//]: # (end copyright)

[//]: # (addons)

[//]: # (end addons)

