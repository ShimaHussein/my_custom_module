# -*- coding: utf-8 -*-
#
from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean("Instructor", default=False)
    # add from me to error
    channel_ids = fields.Many2many('mail.channel', 'mail_channel_profile_partner', 'partner_id', 'channel_id',
                                   copy=False)
    session_ids = fields.Many2many('openacademy.session', string="Attended Session", readonly=True)

