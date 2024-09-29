# -*- coding: utf-8 -*-
# from odoo import http


# class TrackingModule(http.Controller):
#     @http.route('/tracking_module/tracking_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tracking_module/tracking_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracking_module.listing', {
#             'root': '/tracking_module/tracking_module',
#             'objects': http.request.env['tracking_module.tracking_module'].search([]),
#         })

#     @http.route('/tracking_module/tracking_module/objects/<model("tracking_module.tracking_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracking_module.object', {
#             'object': obj
#         })

