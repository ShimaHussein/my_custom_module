# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import AccessError


class ChangeDateOrder(models.TransientModel):
    _name = "change.date.order"
    _description = 'Confirm Date of Sale Order'

    confirm_date = fields.Date(
        string="Order Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    order_id = fields.Many2one('sale.order', string='Sale Order', required=True)

    #action_confirm_order
    def action_confirm_order(self):
        # Check if the current user is in the 'Settings' admin group
        if not self.env.user.has_group('base.group_system'):
            raise AccessError("Only administrators are allowed to change the order date.")

        for wizard in self:
            # Set date_order to today's datetime if it is not set
            if not wizard.order_id.date_order:
                wizard.order_id.date_order = fields.Datetime.context_timestamp(wizard, fields.Datetime.now())

            # Check if the month of confirm_date is different from the current date_order
            current_order_month = wizard.order_id.date_order.strftime('%Y-%m')
            confirm_date_month = wizard.confirm_date.strftime('%Y-%m')

            # Update the order date
            wizard.order_id.date_order = wizard.confirm_date

            if current_order_month != confirm_date_month:
                # Update the name based on the new date_order if the month has changed
                wizard.order_id.name = wizard.order_id._get_monthly_sequence_name(wizard.confirm_date)

        return {'type': 'ir.actions.act_window_close'}