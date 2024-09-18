# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models


class ChangeDateOrder(models.TransientModel):
    _name = "change.date.order"
    _description = 'Confirm Date of Sale Order'

    confirm_date = fields.Datetime(
        string="Order Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True)


    def action_confirm_order(self):
        print("Success")
        sale_order =  self.env['sale.order'].search([('id', '=', self.order_id.id)])
        vals = {
            'date_order': self.confirm_date,
            'id':self.order_id.id,
        }
        sale_order.write(vals)
        print(vals)
