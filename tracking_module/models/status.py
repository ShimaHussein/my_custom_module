# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Status(models.Model):
    _name = "tracking.status"
    _rec_name = 'name'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Card'


    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="description")
    model = fields.Selection([('device', 'Device'),
                              ('vehicle', 'Vehicle'),
                              ('card', 'Card'),
                              ('technical', 'Technical'),
                              ('task', 'Task')],
                             string='Model')