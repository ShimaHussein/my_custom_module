# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import AccessError


class ChangeDatePurchase(models.TransientModel):
    _name = "change.date.purchase"
    _description = 'Confirm Date of Purchase Order'

    confirm_date = fields.Date(
        string="Order Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)

    #action_confirm_purchase_order
    def action_confirm_purchase_order(self):
        # Check if the current user is in the 'Settings' admin group
        if not self.env.user.has_group('base.group_system'):
            raise AccessError("Only administrators are allowed to change the order date.")

        for wizard in self:
            # Set order_date to today's date if it is not set
            if not wizard.order_id.order_date:
                wizard.order_id.order_date = fields.Date.context_today(wizard)

            # Check if the month of confirm_date is different from the current order_date
            current_order_month = wizard.order_id.order_date.strftime('%Y-%m')
            confirm_date_month = wizard.confirm_date.strftime('%Y-%m')

            # Update the order date
            wizard.order_id.order_date = wizard.confirm_date

            if current_order_month != confirm_date_month:
                # Update the name based on the new order date if the month has changed
                wizard.order_id.name = wizard.order_id._get_monthly_sequence_name(wizard.confirm_date)

        return {'type': 'ir.actions.act_window_close'}
