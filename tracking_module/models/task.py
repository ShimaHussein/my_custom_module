# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Task(models.Model):
    _inherit = ['project.task']

    tech_name = fields.Many2one('hr.employee', string='Technical Name', tracking=True)
