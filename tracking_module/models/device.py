# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _inherit = ['stock.lot']

    partner_id = fields.Many2one('res.partner', string='Customer', tracking=True)
    vehicle_id = fields.Many2one('tracking.vehicle', string='Vehicle', tracking=True)
    num_device = fields.Char(string="Number of Device")
    brand = fields.Char(string="Brand")
    device_model = fields.Char(string="Device Model")
    add_date = fields.Date(string="Purchase Date", tracking=True)
    cancel_date = fields.Date(string="Cancellation Date", tracking=True)
    active_date = fields.Date(string="Activation Date", tracking=True)
    install_date = fields.Date(string="Installation Date", tracking=True)
    state_id = fields.Many2one('tracking.status', string='Status', tracking=True, domain = "[('model', '=', 'device')]")
    state = fields.Selection([('inStock', 'Free'),
                              ('confirm', 'Sold'),
                              ('ready', 'Ready To Install'),
                              ('install', 'Installed'),
                              ('cancel', 'Cancel')],
                             string='Status', tracking=True)
    card_count = fields.Integer(string="Card Count", compute='_compute_card_count')


    # def _compute_card_count(self):
    #     for rec in self:
    #         card_count = self.env['tracking.card'].search_count([('device_id', '=', rec.id)])
    #         rec.card_count = card_count
    #
    # def open_related_card(self):
    #     return {
    #         'name': 'Card',
    #         'view_mode': 'tree,form',
    #         'res_model': 'tracking.card',
    #         'type': 'ir.actions.act_window',
    #         'domain': [('device_id', '=', self.id)],
    #         'target': 'current',
    #     }
    #
    # def action_free(self):
    #     print("Button Free")
    #
    # def action_confirm(self):
    #     print("Button Sold")
    #
    # def action_ready(self):
    #     print("Button Ready")
    #
    # def action_install(self):
    #     print("Button Install")
    #
    # def action_cancel(self):
    #     print("Button Cancel")


