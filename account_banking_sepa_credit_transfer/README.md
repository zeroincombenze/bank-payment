[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/bank-payment/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)











[![en](http://www.shs-av.com/wp-content/en_US.png)](http://wiki.zeroincombenze.org/it/Odoo/7.0/man)

Sepa Credit Transfer
====================

Module to export payment orders in SEPA XML file format.

SEPA PAIN (PAyment INitiation) is the new european standard for
Customer-to-Bank payment instructions.

This module implements SEPA Credit Transfer (SCT), more specifically PAIN
versions 001.001.02, 001.001.03, 001.001.04 and 001.001.05.
It is part of the ISO 20022 standard, available on http://www.iso20022.org.

The Implementation Guidelines for SEPA Credit Transfer published by the
European Payments Council (http://http://www.europeanpaymentscouncil.eu)
use PAIN version 001.001.03, so it's probably the version of PAIN that you
should try first.



Bonifici Sepa

Modulo per esportare gli ordini di bonifico in formato XML per le banche italiane.

Questo modulo è conforme allo standard CBI delle banche italiane,
ereditato dallo standard SEPA ISO 20022 ma modificato secondo le regole ABI


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Registrazione Ordine SD | :white_check_mark: | Come versione OCA
File XML per CBI | :white_check_mark: | Funzionalità non prevista in OCA
Formati XML EU | :white_check_mark: | Stesi formati modulo OCA


Logo | Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | --- | ---
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/icons/xml-schema.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md) | [ISO + CBI](http://www.cbi-org.eu/Engine/RAServePG.php/P/251610010305/) | 26-06-2017 | 31-12-2017 | Validazione contro schema xml


Installation
------------

These instruction are just an example to remember what you have to do:

    pip install unidecode
    pip install lxml
    git clone https://github.com/zeroincombenze/l10n-italy
    for module in account_banking_pain_base account_banking_sepa_direct_debit; do
        mv ODOO_DIR/l10n-italy/$module BACKUP_DIR/
        cp -R l10n-italy/$module ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i account_banking_sepa_direct_debit -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:it:

* Configurazione > Aziende > Aziende :point_right: Inserire in Initiating Party Identifier il codice CUC ricevuto dalla banca
banca
* Contabilità > Varie > Termini di pagamento :point_right: Inserire termini di pagamento SCT con tipo pagamento SEPA Credit Transfer v04 (CBI-IT)
* Contabilità > Varie > Modalità di pagamento :point_right: Inserire Bonifici bancari su c/c aziendale
* Configurazione > Technical > Sequenze e Identificatori > sequenze :point_right: Impostare Numeratori ordini
* Contabilità > Fornitori > Fornitori :point_right: Inserire il codice IBAN su cui pagare il fornitore
* Contabilità > Fornitori > Fatture da clienti :point_right: Registrare le fatture fornitori
* Contabilità > Pagamento > Ordine pagamento SCT :point_right: Inserire dati


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI


Known issues / Roadmap
----------------------

:ticket: This module replaces OCA module; PR have to be issued.
In order to use this module you have to use:

:warning: Use [account_banking_pain_base](account_banking_pain_base/) replacing OCA module



Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


Credits
-------

### Contributors

* Alexis de Lattre
* Pedro M. Baeza
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* Akretion <http://www.akretion.com>
* SHS-AV s.r.l. <https://www.zeroincombenze.it/>

### Maintainer

[![Odoo Italia Associazione](https://www.odoo-italia.org/images/Immagini/Odoo%20Italia%20-%20126x56.png)](https://odoo-italia.org)

Odoo Italia is a nonprofit organization whose develops Italian Localization for
Odoo.

To contribute to this module, please visit <https://odoo-italia.org/>.



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
