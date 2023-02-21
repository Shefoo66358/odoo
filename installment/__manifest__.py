# -*- coding: utf-8 -*-
{
    'name': "Installment",

    'summary': """
        Odoo 15 module which handle customer installments and payments """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Eng: Mahmoud Sherif ",
    'website': "http://www.linkedin.com/in/mahmoud-sherif-",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/securityInstallment.xml',
        'views/views.xml',
        'views/menu.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
