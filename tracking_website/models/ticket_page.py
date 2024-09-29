# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseData(models.Model):
    _name = 'base.data'
    _description = 'The model for Two Fields Name and Email'

    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Your Email", required=True)
    country_id = fields.Many2one('res.country', string="Country")
    rule = fields.Char(string="Rules")
    description = fields.Char(string="Description")


class DeviceLine(models.Model):
    _name = 'device.line'
    _description = 'Data for Device Line'

    device_id = fields.Many2one('product.product', required=True, string='Device Model')
    product_uom_qty = fields.Float(string='Quantity')
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    install_date = fields.Date(string="Installation Date")
    description = fields.Char(string="Description")
