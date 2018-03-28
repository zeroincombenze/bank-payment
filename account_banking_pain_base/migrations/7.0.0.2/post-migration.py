# -*- coding: utf-8 -*-
#    Copyright (C) 2013-2017 Akretion (http://www.akretion.com)
#    Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp.addons.account_banking_pain_base.post_install\
    import set_default_initiating_party
from openerp import pooler


def migrate(cr, version):
    """Post-install script.
    If version is not set, we are called at installation time."""
    if not version:
        return

    pool = pooler.get_pool(cr.dbname)
    set_default_initiating_party(cr, pool)
