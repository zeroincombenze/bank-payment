==================================
|Zeroincombenze| bank-payment 10.0
==================================

.. contents::



Overview / Panoramica
=====================

|en| On version 10.0, this project focus on payment interface. The indentation below indicates the dependency graph of the main modules.

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
| account_banking_mandate              | 10.0.2.0.2 | 10.0.2.1.0 | Banking mandates                                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_mandate_sale         | 10.0.1.0.1 | |same|     | Adds mandates on sale orders                                                     |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_pain_base            | 10.0.1.1.3 | |same|     | Base module for PAIN file generation                                             |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_banking_sepa_credit_transfer | 10.0.1.1.0 | |same|     | Create SEPA XML files for Credit Transfers                                       |
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
| account_payment_order                | 10.0.1.6.0 | 10.0.1.7.0 | Account Payment Order                                                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_partner              | 10.0.1.2.0 | |same|     | Adds payment mode on partners and invoices                                       |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_purchase             | 10.0.1.0.0 | |same|     | Adds Bank Account and Payment Mode on Purchase Orders                            |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_payment_sale                 | 10.0.1.1.0 | |same|     | Adds payment mode on sale orders                                                 |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| account_voucher_killer               | 10.0.1.0.0 | |same|     | Accounting Payment Access                                                        |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| bank_statement_instant_voucher       | |halt|     | |halt|     | Bank statement instant voucher                                                   |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+
| portal_payment_mode                  | |halt|     | |halt|     | Adds payment mode ACL's for portal users                                         |
+--------------------------------------+------------+------------+----------------------------------------------------------------------------------+




Getting started / Come iniziare
===============================

|Try Me|


Prerequisites / Prerequisiti
----------------------------

* python 2.7+ (best 2.7.5+)
* postgresql 9.2+ (best 9.5)

::

    cd $HOME
    # Follow statements activate deployment, installation and upgrade tools
    cd $HOME
    [[ ! -d ./tools ]] && git clone https://github.com/zeroincombenze/tools.git
    cd ./tools
    ./install_tools.sh -pUT
    source $HOME/devel/activate_tools


Installation / Installazione
----------------------------

+---------------------------------+------------------------------------------+
| |en|                            | |it|                                     |
+---------------------------------+------------------------------------------+
| These instructions are just an  | Istruzioni di esempio valide solo per    |
| example; use on Linux CentOS 7+ | distribuzioni Linux CentOS 7+,           |
| Ubuntu 14+ and Debian 8+        | Ubuntu 14+ e Debian 8+                   |
|                                 |                                          |
| Installation is built with:     | L'installazione è costruita con:         |
+---------------------------------+------------------------------------------+
| `Zeroincombenze Tools <https://zeroincombenze-tools.readthedocs.io/>`__ |
+---------------------------------+------------------------------------------+
| Suggested deployment is:        | Posizione suggerita per l'installazione: |
+---------------------------------+------------------------------------------+
| $HOME/10.0 |
+----------------------------------------------------------------------------+

::

    # Odoo repository installation; OCB repository must be installed
    deploy_odoo clone -r bank-payment -b 10.0 -G zero -p $HOME/10.0
    # Upgrade virtual environment
    vem amend $HOME/10.0/venv_odoo


Upgrade / Aggiornamento
-----------------------

::

    deploy_odoo update -r bank-payment -b 10.0 -G zero -p $HOME/10.0
    vem amend $HOME/10.0/venv_odoo
    # Adjust following statements as per your system
    sudo systemctl restart odoo


Support / Supporto
------------------

|Zeroincombenze| This project is mainly supported by the `SHS-AV s.r.l. <https://www.zeroincombenze.it/>`__



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


ChangeLog History / Cronologia modifiche
----------------------------------------




Credits / Ringraziamenti
========================

Copyright
---------

Odoo is a trademark of `Odoo S.A. <https://www.odoo.com/>`__ (formerly OpenERP)


----------------

|en| **zeroincombenze®** is a trademark of `SHS-AV s.r.l. <https://www.shs-av.com/>`__
which distributes and promotes ready-to-use **Odoo** on own cloud infrastructure.
`Zeroincombenze® distribution of Odoo <https://www.zeroincombenze.it/>`__
is mainly designed to cover Italian law and markeplace.

|it| **zeroincombenze®** è un marchio registrato da `SHS-AV s.r.l. <https://www.shs-av.com/>`__
che distribuisce e promuove **Odoo** pronto all'uso sulla propria infrastuttura.
La distribuzione `Zeroincombenze® <https://www.zeroincombenze.it/>`__ è progettata per le esigenze del mercato italiano.

|
|


Last Update / Ultimo aggiornamento: 2024-06-03

.. |Maturity| image:: https://img.shields.io/badge/maturity-Alfa-red.png
    :target: https://odoo-community.org/page/development-status
    :alt: 
.. |license gpl| image:: https://img.shields.io/badge/licence-LGPL--3-7379c3.svg
    :target: http://www.gnu.org/licenses/lgpl-3.0-standalone.html
    :alt: License: LGPL-3
.. |license opl| image:: https://img.shields.io/badge/licence-OPL-7379c3.svg
    :target: https://www.odoo.com/documentation/user/14.0/legal/licenses/licenses.html
    :alt: License: OPL
.. |Try Me| image:: https://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-10.svg
    :target: https://erp10.zeroincombenze.it
    :alt: Try Me
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
