# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Technical(models.Model):
    _inherit = ['hr.employee']

    state_id = fields.Many2one('tracking.status', string='Status', tracking=True, domain = "[('model', '=', 'technical')]")
