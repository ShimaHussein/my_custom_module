# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models


class ChangeDateDelivery(models.TransientModel):
    _name = "change.date.delivery"
    _description = 'Change date delivery'

    confirm_date = fields.Date(
        string="Delivery Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    order_picking = fields.Many2one('stock.picking', string='Picking Delivery', required=True)


    def action_change_date_delivery(self):
        order_picking =  self.env['stock.picking'].search([('name', '=', self.order_picking.name)])
        vals = {
            'date_done': self.confirm_date,
            'name':self.order_picking.name,
        }
        order_picking.write(vals)
