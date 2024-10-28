# -*- coding: utf-8 -*-

from odoo import models, fields, api



class SaleOrder(models.Model):
    _inherit = 'purchase.order'

    order_date = fields.Date(
        string="Order Date",
        required=True,
        tracking=True,
    )