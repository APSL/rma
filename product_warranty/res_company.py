# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright 2013 Camptocamp
#    Copyright 2009-2013 Akretion, 
#    Author: Emmanuel Samyn, Raphaël Valyi, Sébastien Beau, Joel Grand-Guillaume
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, orm, osv


class res_company(orm.Model):
    
    _inherit = "res.company"

    _columns = {
        'crm_return_address_id': fields.many2one('res.partner', 
            'Return address',
            help="Default address where the customers has to send back the "
                 "returned product. If empty, the address is the "
                 "company address"),
    }

