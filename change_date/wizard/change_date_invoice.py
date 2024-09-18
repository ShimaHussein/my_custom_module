# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models


class ChangeDateInvoice(models.TransientModel):
    _name = "change.date.invoice"
    _description = 'Change date invoice'

    confirm_date = fields.Datetime(
        string="Invoice Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    invoice_order= fields.Many2one('account.move', string='Invoice / Bill', required=True)


    def action_change_date_invoice(self):
        print("Success")
        invoice_order =  self.env['account.move'].search([('name', '=', self.invoice_order.name)])
        vals = {
            'invoice_date': self.confirm_date,
            'name':self.invoice_order.name,
        }
        invoice_order.write(vals)
        print(vals)
