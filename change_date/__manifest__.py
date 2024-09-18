# -*- coding: utf-8 -*-
{
    'name': "Change Date",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/change_date_order_view.xml',
        'wizard/change_date_delivery_view.xml',
        'wizard/change_date_invoice_view.xml',
        'wizard/change_date_purchase_view.xml',
        'views/views.xml',
        'views/sale_form_inherit.xml',
        'views/delivery_form_inherit.xml',
        'views/invoice_form_inherit.xml',
        'views/purchase_form_inherit.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
