# -*- coding: utf-8 -*-
#
# Copyright 2010-2017, Akretion (http://www.akretion.com)
# Copyright 2016-2017, SHS-AV s.r.l. <https://www.zeroincombenze.it>
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
# [2013: Akretion] First version
# [2017: SHS-AV] Italian localization
#
import logging

from openerp.osv import fields, orm

logger = logging.getLogger(__name__)


class ResCompany(orm.Model):
    _inherit = 'res.company'

    _columns = {
        'sepa_creditor_identifier': fields.char(
            'SEPA Creditor Identifier', size=35,
            help="Enter the Creditor Identifier that has been attributed "
            "to your company to make SEPA Direct Debits. This identifier "
            "is composed of :\n- your country ISO code (2 letters)\n- a "
            "2-digits checkum\n- a 3-letters business code\n- a "
            "country-specific identifier"),
        'original_creditor_identifier': fields.char(
            'Original Creditor Identifier', size=70),
    }

    def is_sepa_creditor_identifier_valid(
            self, cr, uid, sepa_creditor_identifier, context=None):
        """Check if SEPA Creditor Identifier is valid
        @param sepa_creditor_identifier: SEPA Creditor Identifier as str
            or unicode
        @return: True if valid, False otherwise
        """
        if not isinstance(sepa_creditor_identifier, (str, unicode)):
            return False
        try:
            sci_str = str(sepa_creditor_identifier)
        except BaseException:
            logger.warning(
                "SEPA Creditor ID should contain only ASCII caracters.")
            return False
        sci = sci_str.lower()
        if len(sci) < 9:
            return False
        before_replacement = sci[7:] + sci[0:2] + '00'
        logger.debug(
            "SEPA ID check before_replacement = %s" % before_replacement)
        after_replacement = ''
        for char in before_replacement:
            if char.isalpha():
                after_replacement += str(ord(char) - 87)
            else:
                after_replacement += char
        logger.debug(
            "SEPA ID check after_replacement = %s" % after_replacement)
        if int(sci[2:4]) == (98 - (int(after_replacement) % 97)):
            return True
        else:
            return False

    def _check_sepa_creditor_identifier(self, cr, uid, ids):
        for company in self.browse(cr, uid, ids):
            if company.sepa_creditor_identifier:
                if not self.is_sepa_creditor_identifier_valid(
                        cr, uid, company.sepa_creditor_identifier):
                    return False
        return True

    _constraints = [
        (_check_sepa_creditor_identifier,
            "Invalid SEPA Creditor Identifier.",
            ['sepa_creditor_identifier']),
    ]
