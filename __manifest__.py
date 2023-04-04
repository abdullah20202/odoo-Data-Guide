# -*- coding: utf-8 -*-
{
    'name': "Odoo Data Guide",

    'summary': """
        in this example will monubliate product data from code in odoo version 15""",

    'description': """
        contain * Special Patterns for X2Many(One2many, Many2Many)
    """,

    'author': "Abdullah",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/product.xml',
        'views/views.xml',
    ],

}
