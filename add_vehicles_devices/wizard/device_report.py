# -*- coding: utf-8 -*-
from contextlib import nullcontext

# from numpy.doc.constants import lines
from odoo import api, fields, models


class DeviceReportWizard(models.TransientModel):
    _name = "device.report.wizard"
    _description = 'Print device report for customer'

    partner_id = fields.Many2one('res.partner', required=True, string='Customer')

    def action_print_report(self):
        domain = []
        partner_id = self.partner_id.id
        customer = self.partner_id.name
        if partner_id:
            domain += [('device_id.partner_id.id', '=', partner_id)]
        print(domain)
        devices = self.env['customer.device.line'].search_read(domain)
        data = {
            # 'form_data': self.read()[0],
            'devices': devices,
            'partner_id':customer
        }
        return self.env.ref('add_vehicles_devices.action_device_report_xlsx').report_action(self, data=data)
        # print( self.read()[0])
        # devices = self.env['customer.device.line'].search_read([])

        # return self.env.ref('add_vehicles.action_device_report_xlsx').report_action(self,data=data)
