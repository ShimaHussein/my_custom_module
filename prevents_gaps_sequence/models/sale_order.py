# -*- coding: utf-8 -*-

from odoo import models, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        # Retrieve the global sale order sequence object (without company restriction)
        sale_order_sequence = self.env['ir.sequence'].sudo().search([
            ('code', '=', 'sale.order'),
            ('company_id', '=', False)  # Sequence shared across all companies
        ], limit=1)

        if not sale_order_sequence:
            raise exceptions.UserError(
                "Global sale order sequence not found. Please create a sequence with code 'sale.order' and no specific company.")

        # Retry mechanism to ensure a unique sale order number globally
        unique = False
        while not unique:
            # Generate the next sequence number
            sale_order_number = 'S' + str(sale_order_sequence.number_next_actual).zfill(5)

            # Check if the generated sequence number is unique globally
            if not self.env['sale.order'].sudo().search_count([('name', '=', sale_order_number)]):
                # If unique, set it in vals and exit loop
                vals['name'] = sale_order_number
                unique = True
            else:
                # Increment `number_next_actual` manually to avoid duplicates
                sale_order_sequence.write({'number_next_actual': sale_order_sequence.number_next_actual + 1})

        # Create the sale order with the unique serial number
        sale_order = super(SaleOrder, self).create(vals)

        # After creation, adjust the sequence to the next number
        sale_order_number_int = int(sale_order.name.replace('S', '').lstrip('0'))
        sale_order_sequence.write({'number_next_actual': sale_order_number_int + 1})

        return sale_order

    def unlink(self):
        # Get the global sequence (not company-specific)
        sequence = self.env['ir.sequence'].sudo().search([
            ('code', '=', 'sale.order'),
            ('company_id', '=', False)
        ], limit=1)

        # Collect the numbers of orders to be deleted
        order_numbers = []
        for sale_order in self:
            order_numbers.append(int(sale_order.name.replace('S', '').lstrip('0')))

        # Sort order numbers in ascending order
        order_numbers.sort()

        # Check each number if it's globally unique (not used elsewhere)
        for number in order_numbers:
            sale_order_name = 'S' + str(number).zfill(5)
            is_sequence_in_use = self.env['sale.order'].sudo().search_count([
                ('name', '=', sale_order_name)
            ]) > 1  # More than one means it is in use elsewhere

            # Update `number_next_actual` only if the number is not in use globally
            if sequence and not is_sequence_in_use and sequence.number_next_actual > number:
                sequence.write({'number_next_actual': number})
            else:
                # Stop if we encounter an order number that is still in use
                break

        # Call the original unlink method to delete the sale orders
        return super(SaleOrder, self).unlink()
