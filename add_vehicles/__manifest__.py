# -*- coding: utf-8 -*-
{
    'name': "add_vehicles",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Shima",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'sale', 'stock', 'report_xlsx', 'report_xlsx_helper'],

    'data': [
        'security/ir.model.access.csv',
        'wizard/device_report_view.xml',
        'views/menu.xml',
        'views/vehicle_view.xml',
        'views/sale.xml',
        'views/device.xml',
        'report/device_report.xml'

    ],

}
