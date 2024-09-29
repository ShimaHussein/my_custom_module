# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrackingVehicle(models.Model):
    _name = "tracking.vehicle"
    _rec_name = 'license_plate_number'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Add Vehicle'

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
    partner_id = fields.Many2one('res.partner', required=True, string='Customer', tracking=True)
    device_count = fields.Integer(string="Device Count", compute='_compute_device_count')
    state_id = fields.Many2one('tracking.status', string='Status', tracking=True, domain = "[('model', '=', 'vehicle')]")

    def _compute_device_count(self):
        for rec in self:
            device_count = self.env['stock.lot'].search_count([('vehicle_id', '=', rec.id)])
            rec.device_count = device_count

    def open_related_device(self):
        return {
            'name': 'Device',
            'view_mode': 'tree,form',
            'res_model': 'stock.lot',
            'type': 'ir.actions.act_window',
            'domain': [('vehicle_id', '=', self.id)],
            'target': 'current',
        }

