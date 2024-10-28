# -*- coding: utf-8 -*-
# from odoo import http


# class PreventsGapsSequence(http.Controller):
#     @http.route('/prevents_gaps_sequence/prevents_gaps_sequence', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prevents_gaps_sequence/prevents_gaps_sequence/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prevents_gaps_sequence.listing', {
#             'root': '/prevents_gaps_sequence/prevents_gaps_sequence',
#             'objects': http.request.env['prevents_gaps_sequence.prevents_gaps_sequence'].search([]),
#         })

#     @http.route('/prevents_gaps_sequence/prevents_gaps_sequence/objects/<model("prevents_gaps_sequence.prevents_gaps_sequence"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prevents_gaps_sequence.object', {
#             'object': obj
#         })

