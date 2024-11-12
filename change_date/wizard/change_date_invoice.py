# -*- coding: utf-8 -*-

from odoo import api, fields, models
import logging

_logger = logging.getLogger(__name__)


class ChangeDateInvoice(models.TransientModel):
    _name = "change.date.invoice"
    _description = 'Change date invoice'

    confirm_date = fields.Date(
        string="Invoice Date",
        required=True, copy=False,
        help="Creation date of draft/sent orders,\nConfirmation date of confirmed orders.",
    )

    invoice_order = fields.Many2one('account.move', string='Invoice / Bill', required=True)

    def action_change_date_invoice(self):
        if not self.invoice_order:
            _logger.warning("Invoice Order is not set.")
            return

        # Search for the invoice based on the name
        invoice_order = self.env['account.move'].search([('name', '=', self.invoice_order.name)], limit=1)

        if invoice_order:
            if invoice_order.state == 'posted':
                # Revert to draft to make changes
                invoice_order.button_draft()

            vals = {
                'invoice_date': self.confirm_date,
                'name': False  # Clear the sequence to allow date change
            }
            invoice_order.write(vals)
            _logger.info(f"Invoice updated with values: {vals}")

            # If needed, post the invoice again
            if invoice_order.state == 'draft':
                invoice_order.action_post()
        else:
            _logger.warning(f"No invoice found with the name: {self.invoice_order.name}")
