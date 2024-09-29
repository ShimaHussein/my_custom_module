# -*- coding: utf-8 -*-

from odoo import models, fields, api


class DeviceFromDelivery(models.Model):
    _name = "device.from.delivery"
    _rec_name = 'order_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Device From Delivery'

    partner_id = fields.Many2one('res.partner', required=True, string='Customer', tracking=True)
    order_id = fields.Many2one('sale.order', string="Sale Order", required=True, ondelete='cascade',
                               domain='[("partner_id", "=", partner_id)]', tracking=True)
    picking_id = fields.Many2one('stock.picking', string="Stock Picking", ondelete='cascade',
                                 readonly=True)
    device_line_ids = fields.One2many('device.from.delivery.line', 'device_id', string="Device Lines")

    @api.onchange('order_id')
    def onchange_order_id(self):
        order_picking = self.env['stock.picking'].search([('origin', '=', self.order_id.name)])
        if self.order_id:
            if order_picking.name:
                self.picking_id = order_picking

    @api.onchange('picking_id')
    def onchange_picking_id(self):
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.picking_id.move_line_ids:
                line.date = self.picking_id.date_done
                val = {
                    "product_id": line.product_id,
                    "lot_id": line.lot_id,
                    "date": self.picking_id.date_done
                }
                lines.append((0, 0, val))
            rec.device_line_ids = lines


class DeviceFromDeliveryLine(models.Model):
    _name = "device.from.delivery.line"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Line of Device From Delivery'

    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Device Type",
        change_default=True, ondelete='restrict', index='btree_not_null',
    )
    date = fields.Date(string="Issue Date", required=True)
    lot_id = fields.Many2one(
        'stock.lot', 'Lot/Serial Number',
        domain="[('product_id', '=', product_id)]"
    )
    device_id = fields.Many2one('device.from.delivery', string='Device')


