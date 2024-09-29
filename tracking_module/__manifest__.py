# -*- coding: utf-8 -*-
{
    'name': "Tracking",

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
    'depends': ['base', 'web', 'sale', 'account', 'stock', 'mail', 'hr', ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/customer_view.xml',
        'views/card_view.xml',
        'views/device_view.xml',
        'views/device_from_delivery.xml',
        'views/vehicle_view.xml',
        'views/technical_view.xml',
        'views/service_request_view.xml',
        'views/task_view.xml',
        'views/sale_order_view.xml',
        'views/status_view.xml',
        'views/menu.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
