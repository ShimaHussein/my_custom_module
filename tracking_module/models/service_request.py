# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ServiceRequest(models.Model):
    _name = "tracking.service.request"
    _rec_name = 'type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Service Request'


    type = fields.Char(string="Type", required=True)
    model = fields.Char(string="Service Model",  required=True)

class CustomerServiceRequest(models.Model):
    _name = "tracking.customer.service.request"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Customer Service Request'

    type = fields.Many2one('tracking.service.request', string='Type', tracking=True,  required=True, readonly=True)
    model = fields.Char(string="Service Model")
    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True,  required=True, readonly=True)
    order_id = fields.Many2one('sale.order', string='Sale Order', tracking=True,  required=True, readonly=True)
    vehicle_ids = fields.Many2many('tracking.vehicle', string="Vehicle", readonly=True)
    order_line_ids = fields.Many2many('sale.order.line', string="Order Line", readonly=True)



