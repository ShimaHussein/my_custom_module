# -*- coding: utf-8 -*-

import logging
from odoo import models, fields, api
from datetime import datetime, timedelta

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    order_date = fields.Date(
        string="Order Date",
    )


    def _get_monthly_sequence_name(self, date_order):
        # Ensure date_order is a datetime object, then convert to date
        if isinstance(date_order, str):
            date_order = datetime.strptime(date_order, '%Y-%m-%d %H:%M:%S')
        if isinstance(date_order, datetime):
            date_order = date_order.date()

        # Define the base sequence code
        base_sequence_code = 'sale.order'

        # Retrieve the base sequence for prefix and configuration
        base_sequence = self.env['ir.sequence'].sudo().search([('code', '=', base_sequence_code)], limit=1)
        if not base_sequence:
            raise ValueError(f"Base sequence with code '{base_sequence_code}' not found.")

        # Define a unique code for the sequence for the given year and month
        sequence_code = f'{base_sequence_code}.{date_order.strftime("%Y_%m")}'

        # Use the prefix from the base sequence, but formatted with the current year/month
        dynamic_prefix = base_sequence.prefix.replace(
            '%(year)s', date_order.strftime('%Y')
        ).replace(
            '%(month)s', date_order.strftime('%m')
        )

        # Lock the sequence record for this month/year to prevent gaps
        self._cr.execute("SELECT id FROM ir_sequence WHERE code = %s FOR UPDATE", (sequence_code,))
        sequence = self.env['ir.sequence'].sudo().search([('code', '=', sequence_code)], limit=1)

        if not sequence:
            # Create a new sequence if it does not exist, using the dynamic prefix
            sequence = self.env['ir.sequence'].sudo().create({
                'name': f'Sale Order {date_order.strftime("%B %Y")}',
                'code': sequence_code,
                'prefix': dynamic_prefix,
                'padding': base_sequence.padding,  # Use padding from base sequence
                'implementation': 'standard',
                'use_date_range': True,  # Enable date range to reset monthly
                'date_range_ids': [(0, 0, {
                    'date_from': date_order.replace(day=1),
                    'date_to': (date_order.replace(day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1),
                })]
            })

        # Generate the next sequence number for this specific month in a safe way to avoid gaps
        sequence_number = sequence.with_context(ir_sequence_date=date_order).next_by_id()

        # Return the sequence name with the dynamic prefix and sequence number
        return sequence_number

    def create(self, vals):
        # Set date_order to the provided date or default to today
        date_order = vals.get('date_order', fields.Datetime.context_timestamp(self, fields.Datetime.now()))

        # Generate the name using the monthly sequence
        vals['name'] = self._get_monthly_sequence_name(date_order)

        # Create the record with the modified vals
        return super(SaleOrder, self).create(vals)
