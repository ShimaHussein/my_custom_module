# -*- coding: utf-8 -*-
# from odoo import http


# class ReturnToDraft(http.Controller):
#     @http.route('/return_to_draft/return_to_draft', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/return_to_draft/return_to_draft/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('return_to_draft.listing', {
#             'root': '/return_to_draft/return_to_draft',
#             'objects': http.request.env['return_to_draft.return_to_draft'].search([]),
#         })

#     @http.route('/return_to_draft/return_to_draft/objects/<model("return_to_draft.return_to_draft"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('return_to_draft.object', {
#             'object': obj
#         })

