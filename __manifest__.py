# -*- coding: utf-8 -*-
{
    'name': "proxity_custom",

    'summary': """
        GAIN & PERTE 

    """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Index Consulting Madagascar",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/template.xml',
        "views/res_partner.xml",
        'views/pos_views.xml',
        'views/product_pricelist.xml',
    ],
    "qweb": [
        "static/src/xml/pos.xml",
    ],
}