# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    order_date = fields.Date(
        string="Order Date",
        required=True,
        tracking=True,
    )

    def _get_monthly_sequence_name(self, order_date):
        # Ensure order_date is a date object
        if isinstance(order_date, str):
            order_date = datetime.strptime(order_date, '%Y-%m-%d').date()

        # Define the base sequence code
        base_sequence_code = 'purchase.order'

        # Retrieve the base sequence for prefix and configuration
        base_sequence = self.env['ir.sequence'].sudo().search([('code', '=', base_sequence_code)], limit=1)
        if not base_sequence:
            raise ValueError(f"Base sequence with code '{base_sequence_code}' not found.")

        # Define a unique code for the sequence for the given year and month
        sequence_code = f'{base_sequence_code}.{order_date.strftime("%Y_%m")}'

        # Use the prefix from the base sequence, but formatted with the current year/month
        dynamic_prefix = base_sequence.prefix.replace(
            '%(year)s', order_date.strftime('%Y')
        ).replace(
            '%(month)s', order_date.strftime('%m')
        )

        # Lock the sequence record for this month/year to prevent gaps
        self._cr.execute("SELECT id FROM ir_sequence WHERE code = %s FOR UPDATE", (sequence_code,))
        sequence = self.env['ir.sequence'].sudo().search([('code', '=', sequence_code)], limit=1)

        if not sequence:
            # Create a new sequence if it does not exist, using the dynamic prefix
            sequence = self.env['ir.sequence'].sudo().create({
                'name': f'Purchase Order {order_date.strftime("%B %Y")}',
                'code': sequence_code,
                'prefix': dynamic_prefix,
                'padding': base_sequence.padding,  # Use padding from base sequence
                'implementation': 'standard',
                'use_date_range': True,  # Enable date range to reset monthly
                'date_range_ids': [(0, 0, {
                    'date_from': order_date.replace(day=1),
                    'date_to': (order_date.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1),
                })]
            })

        # Generate the next sequence number for this specific month in a safe way to avoid gaps
        sequence_number = sequence.with_context(ir_sequence_date=order_date).next_by_id()

        # Return the sequence name with the dynamic prefix and sequence number
        return sequence_number

    def create(self, vals):
        # Set order_date to the provided date or default to today
        order_date = vals.get('order_date', fields.Date.context_today(self))

        # Generate the name using the monthly sequence
        vals['name'] = self._get_monthly_sequence_name(order_date)

        # Create the record with the modified vals
        return super(PurchaseOrder, self).create(vals)

   