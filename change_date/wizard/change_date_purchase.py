# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models


class ChangeDatePurchase(models.TransientModel):
    _name = "change.date.purchase"
    _description = 'Confirm Date of Purchase Order'

    confirm_date = fields.Datetime(
        string="Order Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)


    def action_confirm_purchase_order(self):
        print("Success")
        purchace_order =  self.env['purchase.order'].search([('id', '=', self.order_id.id)])
        vals = {
            'date_approve': self.confirm_date,
            'id':self.order_id.id,
        }
        purchace_order.write(vals)
        print(vals)
