# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models
from orca.orca_state import device


class CustomerVehicles(models.Model):
    _name = "customer.vehicles"
    _description = 'Add Button Customer Vehicles'

    owner = fields.Char(string="Owner", required=True)
    owner_id = fields.Char(string="Owner Id", required=True)
    chassis_number = fields.Char(string="Chassis Number", required=True)
    license_plate_number = fields.Char(string="License Plate Number", required=True)
    brand = fields.Char(string="Brand", required=True)
    vehicle_weight = fields.Integer(string="Vehicle Weight", required=True)
    color = fields.Char(string="Color", required=True)
    serial_number = fields.Char(string="Sequence Number", required=True)
    registration_type = fields.Char(string="Registration Type")
    vehicle_model = fields.Char(string="Vehicle Model")
    vehicle_load_capacity = fields.Integer(string="Vehicle Load Capacity")
    year_of_manufacture = fields.Char(string="Year of Manufacture", required=True)
    partner_id = fields.Many2one('res.partner', required=True, string='Customer', readonly=True)


class CustomerDevice(models.Model):
    _name = "customer.device"
    _description = 'Add Button Customer Device'

    partner_id = fields.Many2one('res.partner', required=True, string='Customer', readonly=True)
    product_id = fields.Many2one(
        comodel_name='product.product',
        string="Device Type",
        change_default=True, ondelete='restrict', index='btree_not_null',
        domain='[("sale_ok", "=", True)]'
    )
    device_line_ids = fields.One2many('customer.device.line', 'device_id', string="Device Lines")
    order_id = fields.Many2one('sale.order', string="Sale Order", required=True, ondelete='cascade',
                               domain='[("partner_id", "=", partner_id)]')
    picking_id = fields.Many2one('stock.picking', string="Stock Picking", ondelete='cascade',
                                 readonly=True)

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


class CustomerDeviceLine(models.Model):
    _name = "customer.device.line"
    _description = 'Add Customer Device Line'

    picking_id = fields.Many2one(
        'stock.picking', 'Transfer', auto_join=True,
        check_company=True,
        index=True,
        help='The stock operation where the packing has been made')

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
    device_id = fields.Many2one('customer.device', string='Device')



class Partner(models.Model):
    _inherit = ['res.partner']

    vehicles_count = fields.Integer(compute='_compute_vehicles_count')
    device_count = fields.Integer(compute='_compute_device_count')
    picking_count = fields.Integer(compute='_compute_picking_count')

    def _compute_vehicles_count(self):
        for rec in self:
            vehicles_count = self.env['customer.vehicles'].search_count([('partner_id', '=', rec.id)])
            rec.vehicles_count = vehicles_count

    def _compute_device_count(self):
        for rec in self:
            device_count = self.env['customer.device'].search_count([('partner_id', '=', rec.id)])
            rec.device_count = device_count

    def _compute_picking_count(self):
        for rec in self:
            picking_count = self.env['stock.picking'].search_count([('partner_id', '=', rec.id)])
            rec.picking_count = picking_count

    def open_related_vehicles(self):
        print("#" * 50)
        return {
            'name': 'Vehicles',
            'view_mode': 'tree,form',
            'res_model': 'customer.vehicles',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }

    def open_related_device(self):
        print("#" * 50)
        return {
            'name': 'Device',
            'view_mode': 'tree,form',
            'res_model': 'customer.device',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }

    def open_related_device_from_delivery(self):
        print("#" * 50)
        context = dict(self.env.context)
        context.update({"create": False})
        return {
            'name': 'Device Delivery',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'type': 'ir.actions.act_window',
            'context': context,
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }
