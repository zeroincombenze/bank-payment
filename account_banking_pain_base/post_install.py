# -*- coding: utf-8 -*-
# Copyright (C) 2013-2017 Akretion <alexis.delattre@akretion.com>
# Copyright (C) 2014-2017 Serv. Tecnol. Avanzados - Pedro M. Baeza
# Copyright (C) 2016-2017 Antiun Ingenieria S.L. - Antonio Espinosa
# Copyright (C) 2016-2017 SHS-AV s.r.l. <https://www.zeroincombenze.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization

from openerp import SUPERUSER_ID


def set_default_initiating_party(cr, pool):
    company_ids = pool['res.company'].search(cr, SUPERUSER_ID, [])
    companies = pool['res.company'].browse(cr, SUPERUSER_ID, company_ids)
    for company in companies:
        pool['res.company']._default_initiating_party(
            cr, SUPERUSER_ID, company)
        # pool['res.company']._initiating_party_issuer_default(
        #     cr, SUPERUSER_ID, company=company)
    return
