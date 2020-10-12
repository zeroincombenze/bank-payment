
==================================
|Zeroincombenze| bank-payment 10.0
==================================
|Build Status| |Codecov Status| |license gpl| |Try Me|


.. contents::


Overview / Panoramica
=====================

|en| OCA banking payment addons for Odoo
========================================

On version 10.0, this project focus on payment interface. The indentation below indicates the dependency graph of the main modules.

    * account_banking_payment_export - Basic export functionality of payment orders
    * account_banking_sepa_credit_transfer - Export of payment orders in SEPA format
    * account_direct_debit - Debit order infrastructure analogous to Odoo native payment orders
    * account_banking_sepa_direct_debit - Export of debit orders in SEPA format

Other features can now be found in these repositories:

 * https://github.com/OCA/bank-statement-import
 * https://github.com/OCA/bank-statement-reconcile



|it| Pagamenti bancari

Moduli per la gestione dei pagamenti bancari, principalmente Sepa.


Avaiable Addons / Moduli disponibili
------------------------------------

+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| Name / Nome                          | Version    | OCA Ver.   | Description / Descrizione                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_mandate              | 10.0.2.0.1 | |same|     | Banking mandates                                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_mandate_sale         | 10.0.1.0.1 | |same|     | Adds mandates on sale orders                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_pain_base            | 10.0.1.1.3 | |same|     | Base module for PAIN file generation                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_sepa_credit_transfer | |halt|     | |same|     | Create SEPA XML files for Credit Transfers                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_sepa_direct_debit    | 10.0.1.1.3 | |same|     | Create SEPA files for Direct Debit                                               |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_tests                | |halt|     | |halt|     | Banking Addons - Tests                                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_import_line_multicurrency_ex | |halt|     | |halt|     | Add an improved view for move line import in bank statement                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_blocking             | |halt|     | |halt|     |  Prevent invoices under litigation to be proposed in payment orders.             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_line_cancel          | 10.0.1.0.0 | |same|     | Account payment line cancel                                                      |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_mode                 | 10.0.1.0.2 | |same|     | Account Payment Mode                                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_mode_term            | |halt|     | |halt|     | Account Banking - Payments Term Filter                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_order                | 10.0.1.6.0 | |same|     | Account Payment Order                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_partner              | |halt|     | |same|     | Adds payment mode on partners and invoices                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_purchase             | 10.0.1.0.0 | |same|     | Adds Bank Account and Payment Mode on Purchase Orders                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_sale                 | 10.0.1.1.0 | |same|     | Adds payment mode on sale orders                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_voucher_killer               | 10.0.1.0.0 | |same|     | Accounting Payment Access                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| bank_statement_instant_voucher       | |halt|     | |halt|     | Bank statement instant voucher                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| partner_bank                         | 10.0.0.2   | |no_check| | Add bank account sheet in partner view                                           |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| portal_payment_mode                  | |halt|     | |halt|     | Adds payment mode ACL's for portal users                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+



OCA comparation / Confronto con OCA
-----------------------------------


+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Description / Descrizione                                       | Zeroincombenze    | OCA            | Notes / Note                   |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+
| Coverage / Copertura test                                       |  |Codecov Status| | |OCA Codecov|  |                                |
+-----------------------------------------------------------------+-------------------+----------------+--------------------------------+



Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------


* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)
* openupgradelib>=2.0.0
* unidecode


Installation / Installazione
----------------------------


+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instruction are just an   | Istruzioni di esempio valide solo per    |
| example to remember what        | distribuzioni Linux CentOS 7, Ubuntu 14+ |
| you have to do on Linux.        | e Debian 8+                              |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__    |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| /home/odoo/10.0/bank-payment/                                              |
+----------------------------------------------------------------------------+

::

    cd $HOME
    # Tools installation & activation: skip if you have installed this tool
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    # Odoo installation
    odoo_install_repository bank-payment -b 10.0 -O zero
    vem create /opt/odoo/VENV-10.0 -O 10.0 -DI



Upgrade / Aggiornamento
-----------------------


+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| When you want upgrade and you   | Per aggiornare, se avete installato con  |
| installed using above           | le istruzioni di cui sopra:              |
| statements:                     |                                          |
+---------------------------------+------------------------------------------+

::

    cd $HOME
    # Tools installation & activation: skip if you have installed this tool
    git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -p
    source /opt/odoo/dev/activate_tools
    # Odoo upgrade
    odoo_install_repository bank-payment -b 10.0 -O zero -U
    vem amend /opt/odoo/VENV-10.0 -O 10.0 -DI
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------


|Zeroincombenze| This project is mainly maintained by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



Get involved / Ci mettiamo in gioco
===================================

Bug reports are welcome! You can use the issue tracker to report bugs,
and/or submit pull requests on `GitHub Issues
<https://github.com/zeroincombenze/bank-payment/issues>`_.

In case of trouble, please check there if your issue has already been reported.

Proposals for enhancement
-------------------------


|en| If you have a proposal to change on oh these modules, you may want to send an email to <cc@shs-av.com> for initial feedback.
An Enhancement Proposal may be submitted if your idea gains ground.

|it| Se hai proposte per migliorare uno dei moduli, puoi inviare una mail a <cc@shs-av.com> per un iniziale contatto.

Credits / Didascalie
====================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


----------------


|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://wiki.zeroincombenze.org/en/Odoo>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://wiki.zeroincombenze.org/en/Odoo>`__ è progettata per le esigenze del mercato italiano.


|chat_with_us|


|


Last Update / Ultimo aggiornamento: 2020-10-12

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: Alfa
.. |Build Status| image:: https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=10.0
    :target: https://travis-ci.org/zeroincombenze/bank-payment
    :alt: github.com
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/9.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Coverage Status| image:: https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=10.0
    :target: https://coveralls.io/github/zeroincombenze/bank-payment?branch=10.0
    :alt: Coverage
.. |Codecov Status| image:: https://codecov.io/gh/zeroincombenze/bank-payment/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/zeroincombenze/bank-payment/branch/10.0
    :alt: Codecov
.. |Tech Doc| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-10.svg
    :target: https://wiki.zeroincombenze.org/en/Odoo/10.0/dev
    :alt: Technical Documentation
.. |Help| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-10.svg
    :target: https://wiki.zeroincombenze.org/it/Odoo/10.0/man
    :alt: Technical Documentation
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
.. |OCA Codecov| image:: https://codecov.io/gh/OCA/bank-payment/branch/10.0/graph/badge.svg
    :target: https://codecov.io/gh/OCA/bank-payment/branch/10.0
    :alt: Codecov
.. |Odoo Italia Associazione| image:: https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png
   :target: https://odoo-italia.org
   :alt: Odoo Italia Associazione
.. |Zeroincombenze| image:: https://avatars0.githubusercontent.com/u/6972555?s=460&v=4
   :target: https://www.zeroincombenze.it/
   :alt: Zeroincombenze
.. |en| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/en_US.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |it| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/flags/it_IT.png
   :target: https://www.facebook.com/Zeroincombenze-Software-gestionale-online-249494305219415/
.. |check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/check.png
.. |no_check| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/no_check.png
.. |menu| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/menu.png
.. |right_do| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/right_do.png
.. |exclamation| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/exclamation.png
.. |warning| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/warning.png
.. |same| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/same.png
.. |late| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/late.png
.. |halt| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/halt.png
.. |info| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/awesome/info.png
.. |xml_schema| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/iso/icons/xml-schema.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md
.. |DesktopTelematico| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/DesktopTelematico.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/Desktoptelematico.md
.. |FatturaPA| image:: https://raw.githubusercontent.com/zeroincombenze/grymb/master/certificates/ade/icons/fatturapa.png
   :target: https://github.com/zeroincombenze/grymb/blob/master/certificates/ade/scope/fatturapa.md
.. |chat_with_us| image:: https://www.shs-av.com/wp-content/chat_with_us.gif
   :target: https://t.me/axitec_helpdesk

