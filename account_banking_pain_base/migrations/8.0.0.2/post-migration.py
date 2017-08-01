# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion <alexis.delattre@akretion.com>
# Copyright (C) 2014-2017 Serv. Tecnol. Avanzados - Pedro M. Baeza
# Copyright (C) 2016-2017 Antiun Ingenieria S.L. - Antonio Espinosa
# Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp.addons.account_banking_pain_base.post_install\
    import set_default_initiating_party
from openerp import pooler


def migrate(cr, version):
    if not version:
        return

    pool = pooler.get_pool(cr.dbname)
    set_default_initiating_party(cr, pool)
