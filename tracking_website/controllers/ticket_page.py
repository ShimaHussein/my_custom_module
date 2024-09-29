# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TicketPage(http.Controller):
    @http.route('/ticket', auth='public', website=True)
    def index(self):
        return request.render('tracking_website.ticket_data')

#     @http.route('/tracking_website/tracking_website/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tracking_website.listing', {
#             'root': '/tracking_website/tracking_website',
#             'objects': http.request.env['tracking_website.tracking_website'].search([]),
#         })

#     @http.route('/tracking_website/tracking_website/objects/<model("tracking_website.tracking_website"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tracking_website.object', {
#             'object': obj
#         })

