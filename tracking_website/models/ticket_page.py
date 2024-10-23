# -*- coding: utf-8 -*-

from odoo import models, fields, api

class RequestQuot(models.Model):
    _name = 'request.quot'
    _description = 'Request New Quotation'

    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Your Email", required=True)
    rule = fields.Char(string="Rules")
    description = fields.Char(string="Description")


class RequestQuot(models.Model):
    _name = 'request.quot.line'
    _description = 'Request New Quotation Line'

    device_id = fields.Many2one('product.product', required=True, string='Device Model')
    product_uom_qty = fields.Float(string='Quantity')
    state_id = fields.Many2one("res.country.state", string='City', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    install_date = fields.Date(string="Installation Date")
    description = fields.Char(string="Description")


class MakeInstall(models.Model):
    _name = 'make.install'
    _description = 'Make installation'

    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Your Email", required=True)
    date = fields.Date(string="Installation Date")
    file = fields.Binary('Attachment', attachment=True)



class MakeInstallLine(models.Model):
    _name = 'make.install.line'
    _description = 'Make installation Line'

    vehicle_id = fields.Many2one('tracking.vehicle', required=True)
    branch = fields.Char(string="Branch", required=True)
    state_id = fields.Many2one("res.country.state", string='City', ondelete='restrict',
                                 domain="[('country_id', '=?', country_id)]")
    vehicle_type = fields.Char(string="Vehicle Type", required=True)
    plate_no = fields.Char(string="Plate no", required=True)
    add_accessories = fields.Boolean(string='Add Accessories', default=True)
    accessories = fields.Char(string="Accessories", required=True)



class MakeMaintenance(models.Model):
    _name = 'make.maintenance'
    _description = 'Make Maintenance'

    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Your Email", required=True)
    vehicle_id = fields.Many2many('tracking.vehicle', required=True)
    reason = fields.Char(string="Branch", required=True)
    res_name = fields.Char(string="Vehicle Type", required=True)
    phone_num = fields.Char(string="Plate no", required=True)
    description = fields.Char(string="Description")


class RequestSupport(models.Model):
    _name = 'request.support'
    _description = 'Request Support'

    name = fields.Char(string="Your Name", required=True)
    email = fields.Char(string="Your Email", required=True)
    support_for = fields.Selection([('training', 'Training'),
                              ('solve_problem', 'Solve Problem'),
                              ('create_report', 'Create Report')], string="Support for" )

    date_t = fields.Date(string="Date")
    description_t = fields.Char(string="Description")
    note_t = fields.Char(string="Note")

    problem_type = fields.Char(string="Problem Type")
    file = fields.Binary('Attachment', attachment=True)
    description_p = fields.Char(string="Description")
    note_p = fields.Char(string="Note")


    report_type = fields.Char(string="Report Type")
    vehicle_id = fields.Many2many('tracking.vehicle', required=True)
    fields_in_report =  fields.Many2many('ir.model.fields',
        domain=[('model', '=', 'tracking.vehicle')])
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

