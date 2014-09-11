 # -*- coding: utf-8 -*-
##############################################################################
#    
# Module : cd_unique_product
# Créé le : 2014-03-28 G Lopez
#
# Modulo que permite definir una clave unica para el producto
#
##############################################################################

import openerp
from openerp.osv import osv, fields

class product_product(osv.osv) :
    #_name = "product.product",
    _inherit = "product.product"

    _sql_constraints = [
        ('name_uniq', 'unique(default_code)', 'La clave del producto debe ser unica, ya existe un producto con esa clave'),
    ]

    _columns = {
    	"default_code" : fields.char('Clave', size=13, required=True, help="Clave del Producto"),    	
    }

product_product();