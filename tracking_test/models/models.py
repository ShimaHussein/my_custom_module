# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MyModel(models.Model):
    _name = 'my.model'
    _description = 'My Model'

    name = fields.Char(string='Name')
    order_lines = fields.One2many('my.model.lines', 'order_id', string='Order Lines')  # One2many field

class MyModelLines(models.Model):
    _name = 'my.model.lines'
    _description = 'Lines for My Model'

    product_name = fields.Char(string='Product Name')
    quantity = fields.Integer(string='Quantity')
    order_id = fields.Many2one('my.model', string='Order Reference')  # Many2one field to relate to parent model


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Your Model Description'

    # Selection field (dropdown in the form)
    x_type = fields.Selection([
        ('option_1', 'Option 1'),
        ('option_2', 'Option 2'),
        ('option_3', 'Option 3'),
    ], string='Type', required=True)

    # Field to be shown/hidden
    x_details = fields.Char(string='Details')

    # You can also add any other fields needed for your form
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')