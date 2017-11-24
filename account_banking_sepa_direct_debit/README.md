[![Build Status](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment.svg?branch=8.0)](https://travis-ci.org/Odoo-Italia-Associazione/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/Odoo-Italia-Associazione/bank-payment/badge.svg?branch=8.0)](https://coveralls.io/github/Odoo-Italia-Associazione/bank-payment?branch=8.0)
[![codecov](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0/graph/badge.svg)](https://codecov.io/gh/Odoo-Italia-Associazione/bank-payment/branch/8.0)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-8.svg)](http://erp8.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Sepa Direct Debit
=================

Module to export direct debit payment orders in SEPA XML file format.

SEPA PAIN (PAyment INitiation) is the new european standard for
Customer-to-Bank payment instructions.

This module implements SEPA Direct Debit (SDD), more specifically PAIN
versions 008.001.02, 008.001.03 and 008.001.04.
It is part of the ISO 20022 standard, available on http://www.iso20022.org.

The Implementation Guidelines for SEPA Direct Debit published by the European
Payments Council (http://http://www.europeanpaymentscouncil.eu) use PAIN
version 008.001.02. So if you don't know which version your bank supports,
you should try version 008.001.02 first.


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Sepa Direct Debit
=================

Modulo per esportare gli ordini di incasso SDD in formato XML per le banche italiane.

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
    for module in account_banking_mandate account_direct_debit account_banking_pain_base account_banking_sepa_direct_debit; do
        mv ODOO_DIR/l10n-italy/$module BACKUP_DIR/
        cp -R l10n-italy/$module ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i account_banking_sepa_direct_debit -d MYDB

From UI: go to Setup > Module > Install


Configuration
-------------

:it:

* Configurazione > Aziende > Aziende :point_right: Inserire in Initiating Party Identifier il codice CUC ricevuto dalla banca
* Configurazione > Aziende > Aziende :point_right: Inserire in Creditor Identifier il codice SEPA Creditor Identifier rivevuto dalla banca
* Configurazione > Aziende > Aziende :point_right: Inserire il codice IBAN del c/c su cui incassare gli SDD
* Contabilità > Varie > Termini di pagamento :point_right: Inserire termini di pagamento SDD con tipo pagamento SEPA Direct Debit v02 (Italy)
* Contabilità > Varie > Modalità di pagamento :point_right: Inserire incasso SDD su c/c aziendale
* Configurazione > Technical > Sequenze e Identificatori > sequenze :point_right: Impostare Numeratori ordini
* Contabilità > Clienti > Clienti :point_right: Inserire mandato firmato da cliente
* Contabilità > Pagamento > Mandati SEPA :point_right: Validare mandato SEPA
* Contabilità > Clienti > Fatture a clienti :point_right: Emettere fatture
* Contabilità > Pagamento > Ordine pagamento SDD :point_right: Inserire dati


Usage
-----

For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI


Known issues / Roadmap
----------------------

:ticket: This module replaces OCA module; PR have to be issued.
In order to use this module you have to use:

:warning: Use [account_banking_mandate](account_banking_mandate/) replacing OCA module

:warning: Use [account_direct_debit](account_direct_debit/) replacing OCA module

:warning: Use [account_banking_pain_base](account_banking_pain_base/) replacing OCA module



Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


Credits
-------

### Contributors

* Alexis de Lattre
* Pedro M. Baeza
* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Alexandre Fayolle
* Raphaël Valyi
* Sandy Carter
* Antonio Espinosa <antonioea@antiun.com>
* Sergio Teruel <sergio.teruel@tecnativa.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* Akretion <http://www.akretion.com>
* Gruppo 2B s.r.l. <info@dbs.it>
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

[//]: # (addons)

[//]: # (end addons)
[![chat with us](https://www.shs-av.com/wp-content/chat_with_us.gif)](https://tawk.to/85d4f6e06e68dd4e358797643fe5ee67540e408b)
