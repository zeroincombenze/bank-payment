[![Build Status](https://travis-ci.org/zeroincombenze/bank-payment.svg?branch=7.0)](https://travis-ci.org/zeroincombenze/bank-payment)
[![license agpl](https://img.shields.io/badge/licence-AGPL--3-blue.svg)](http://www.gnu.org/licenses/agpl-3.0.html)
[![Coverage Status](https://coveralls.io/repos/github/zeroincombenze/bank-payment/badge.svg?branch=7.0)](https://coveralls.io/github/zeroincombenze/bank-payment?branch=7.0)
[![codecov](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0/graph/badge.svg)](https://codecov.io/gh/zeroincombenze/bank-payment/branch/7.0)
[![OCA_project](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-oca-7.svg)](https://github.com/OCA/bank-payment/tree/7.0)
[![Tech Doc](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-docs-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/dev)
[![Help](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-help-7.svg)](http://wiki.zeroincombenze.org/en/Odoo/7.0/man/FI)
[![try it](http://www.zeroincombenze.it/wp-content/uploads/ci-ct/prd/button-try-it-7.svg)](http://erp7.zeroincombenze.it)


[![en](https://github.com/zeroincombenze/grymb/blob/master/flags/en_US.png)](https://www.facebook.com/groups/openerp.italia/)

Account Banking PAIN Base Module
================================

This module contains fields and functions that are used by the module for SEPA Credit Transfer (account_banking_sepa_credit_transfer) and SEPA Direct Debit (account_banking_sepa_direct_debit).
This module doesn’t provide any functionality by itself.

This module was started during the Akretion-Noviat code sprint of November 21st 2013 in Epiais les Louvres (France).

It was updated by Antonio Maria Vigliotti in order to work in Italy.


[![it](https://github.com/zeroincombenze/grymb/blob/master/flags/it_IT.png)](https://www.facebook.com/groups/openerp.italia/)

Account Banking PAIN Base Module
================================

Questo modulo contiene le funzioni base utilizzate dai moduli Bonifico SEPA (account_banking_sepa_credit_transfer) e SEPA Direct Debit (account_banking_sepa_direct_debit).

Modificato Antonio Maria Vigliotti per la localizzazione italiana standard CBI.


### Funzionalità & Certificati

Funzione | Status | Note
--- | --- | ---
Standard CBI 4.0 | :white_check_mark: | File xml bonifici Italia
Standard CBI 2.0 | :white_check_mark: | File xml SDD Italia


Logo | Ente/Certificato | Data inizio | Da fine | Note
--- | --- | --- | --- | ---
[![xml_schema](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/icons/xml-schema.png)](https://github.com/zeroincombenze/grymb/blob/master/certificates/iso/scope/xml-schema.md) | [ISO + CBI + ABI](http://www.cbi-org.eu/Engine/RAServePG.php/P/250210010307) | 26-06-2015 | 31-12-2017 | Validazione contro schema xml


Installation
------------

Install this module from Odoo Control Panel.

These instruction are just an example to remember what you have to do:

    pip install unidecode
    pip install lxml
    git clone https://github.com/zeroincombenze/bank-payment
    for module in account_banking_mandate account_banking_pain_base account_banking_sepa_credit_transfer account_banking_sepa_direct_debit; do
        mv ODOO_DIR/bank-payment/$module BACKUP_DIR/
        cp -R bank-payment/$module ODOO_DIR/l10n-italy/
    sudo service odoo-server restart -i account_banking_pain_base -d MYDB

From UI: go to Setup > Module > Install



Configuration
-------------

:it:

* Richiedere alla banca codici CUC e SEPA Creditor Identifier
* Configurazione > Aziende > Aziende :point_right: Inserire codici CUC in SEPA Initiating Party Identifier e SEPA Creditor Identifier
* Configurazione > Aziende > Aziende :point_right: Inserire IBAN c/c su cui operare
* Configurazione > Technical > Sequenze e identificatori > Sequenze :point_right: Inserire sequenza distinte
* Contabilità > Varie > Modalità di pagamento :point_right: Creare modalità di pagamento SDD e/o BB per ogni c/c
* Contabilità > Clienti > Clienti :point_right: Inserire IBAN e mandato per clienti con pagamento SDD
* Contabilità > Fornitori > Fornitori :point_right: Inserire IBAN per fornitori con pagamento BB
* Contabilità > Pagamento > Direct Debit Orders :point_right: Gestione distinte incasso SDD
* Contabilità > Pagamento > Ordini di pagamento :point_right: Gestione pagamento BB


Usage
-----


For furthermore information, please visit http://wiki.zeroincombenze.org/it/Odoo/7.0/man/FI



Known issues / Roadmap
----------------------

:ticket: This module replaces OCA module; PR have to be issued.
In order to use this module you have to use:

:warning: Use [account_banking_mandate](account_banking_mandate/) replacing OCA module

:warning: Use [account_banking_pain_base](account_banking_pain_base/) module does not exist in OCA repository

:warning: Use [account_banking_sepa_credit_transfer](account_banking_sepa_credit_transfer/) replacing OCA module

:warning: Use [account_banking_sepa_direct_debit](account_banking_sepa_direct_debit/) replacing OCA module


Bug Tracker
-----------

Have a bug? Please visit https://odoo-italia.org/index.php/kunena/home


Credits
-------

### Contributors

* Alexis de Lattre
* Pedro M. Baeza
* Stéphane Bidoul <stephane.bidoul@acsone.eu>
* Ignacio Ibeas - Acysos S.L.
* Alexandre Fayolle
* Raphaël Valyi
* Sandy Carter
* Stefan Rijnhart (Therp)
* Antonio Espinosa <antonioea@antiun.com>
* Antonio Maria Vigliotti <antoniomaria.vigliotti@gmail.com>

### Funders

This module has been financially supported by

* Akretion (http://www.akretion.com)
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
