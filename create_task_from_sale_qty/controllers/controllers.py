# -*- coding: utf-8 -*-
# from odoo import http


# class CreateTaskFromSaleQty(http.Controller):
#     @http.route('/create_task_from_sale_qty/create_task_from_sale_qty', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_task_from_sale_qty/create_task_from_sale_qty/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_task_from_sale_qty.listing', {
#             'root': '/create_task_from_sale_qty/create_task_from_sale_qty',
#             'objects': http.request.env['create_task_from_sale_qty.create_task_from_sale_qty'].search([]),
#         })

#     @http.route('/create_task_from_sale_qty/create_task_from_sale_qty/objects/<model("create_task_from_sale_qty.create_task_from_sale_qty"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_task_from_sale_qty.object', {
#             'object': obj
#         })

