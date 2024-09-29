# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ServiceRequest(models.Model):
    _name = "tracking.service.request"
    _rec_name = 'type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Service Request'


    type = fields.Char(string="Type", required=True)
    model = fields.Char(string="Service Model",  required=True)
