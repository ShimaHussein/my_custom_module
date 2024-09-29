# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrackingCard(models.Model):
    _name = "tracking.card"
    _rec_name = 'num_1'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Card'


    num_1 = fields.Char(string="Number No 1", required=True)
    num_2 = fields.Char(string="Number No 2")
    type = fields.Char(string="Type", required=True)
    device_id = fields.Many2one('product.product', string='Device', tracking=True)
    state_id = fields.Many2one('tracking.status', string='Status', tracking=True, domain = "[('model', '=', 'card')]")

