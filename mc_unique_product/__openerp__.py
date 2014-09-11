# -*- coding: utf-8 -*-
{
    'name': 'Clave Unica de Producto',
    'version': '1.0.0',
    'category': 'Producto',
    'sequence': 3,
    'author': 'Gerardo A Lopez Vega @glopzvega',
    'website': 'http://www.codetodev.com',
    'summary': 'Limita el registro de productos con la misma clave.',
    'description': "Este modulo permite agregar referencias unicas para los productos",
    'depends': ["product"],
    'data': [        
        'unique_product_view.xml',
    ],    
    'installable': True,
    'application': False,
    'auto_install': False,
}