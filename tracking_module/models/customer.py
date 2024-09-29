# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = ['res.partner']

    contract_date = fields.Date(string="Contract Date", required=True, tracking=True)
    field_track = fields.Char(string="Field")
    sales_person_track = fields.Many2one('res.users', string='Salesperson', tracking=True)
    city_track = fields.Char(string="City")
    device_count = fields.Integer(string="Device Count", compute='_compute_device_count')
    picking_count = fields.Integer(string="Device Count",compute='_compute_picking_count')
    vehicle_count = fields.Integer(string="Vehicle Count",compute='_compute_vehicle_count')


    def _compute_device_count(self):
        for rec in self:
            device_count = self.env['stock.lot'].search_count([('partner_id', '=', rec.id)])
            rec.device_count = device_count

    def open_related_device(self):
        return {
            'name': 'Device',
            'view_mode': 'tree,form',
            'res_model': 'stock.lot',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }

    def _compute_picking_count(self):
        for rec in self:
            picking_count = self.env['device.from.delivery'].search_count([('partner_id', '=', rec.id)])
            rec.picking_count = picking_count

    def open_related_device_from_delivery(self):
        return {
            'name': 'Device Delivery',
            'view_mode': 'tree,form',
            'res_model': 'device.from.delivery',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }

    def _compute_vehicle_count(self):
        for rec in self:
            vehicle_count = self.env['tracking.vehicle'].search_count([('partner_id', '=', rec.id)])
            rec.vehicle_count = vehicle_count

    def open_related_vehicle(self):
        return {
            'name': 'Vehicle',
            'view_mode': 'tree,form',
            'res_model': 'tracking.vehicle',
            'type': 'ir.actions.act_window',
            'domain': [('partner_id', '=', self.id)],
            'target': 'current',
        }
