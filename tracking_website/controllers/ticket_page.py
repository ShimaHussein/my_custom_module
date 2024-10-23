# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class TicketPage(http.Controller):
    @http.route('/ticket/new-quotation', auth='public', website=True)
    def index(self,  **kw):
        device_rec = request.env['product.product'].sudo().search([])
        country_id = request.env['res.country'].sudo().search([('name', '=', "Saudi Arabia")])
        state_rec = request.env['res.country.state'].sudo().search([('country_id.name', '=', country_id.name)])
        return request.render('tracking_website.request_quot', {'device_rec':device_rec, 'state_rec':state_rec})

    @http.route('/ticket/make-installation', auth='public', website=True)
    def install(self, **kw):
        country_id = request.env['res.country'].sudo().search([('name', '=', "Saudi Arabia")])
        state_rec = request.env['res.country.state'].sudo().search([('country_id.name', '=', country_id.name)])
        return request.render('tracking_website.make_install', {'state_rec': state_rec})

    @http.route('/ticket/make-maintenance', auth='public', website=True)
    def maintenance(self, **kw):
        vehicle_rec = request.env['tracking.vehicle'].sudo().search([])
        return request.render('tracking_website.make_main', {'vehicle_rec': vehicle_rec})

    @http.route('/ticket/request-support', auth='public', website=True)
    def support(self, **kw):
        vehicle_rec = request.env['tracking.vehicle'].sudo().search([])
        model_fields = request.env['ir.model.fields'].sudo().search([('model', '=', 'tracking.vehicle')])
        return request.render('tracking_website.request_support_tpr', {'vehicle_rec': vehicle_rec, 'model_fields': model_fields})