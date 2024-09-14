# -*- coding: utf-8 -*-
#
from xml.dom import ValidationErr
from xxlimited_35 import error

from odoo import models, fields, api, exceptions, _
from datetime import timedelta
import requests
from prompt_toolkit.validation import ValidationError


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Session")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         'The title of the course should not be the description'),

        ('name_unique',
         'UNIQUE(name)',
         'The course title must be unique'),
    ]

    def get_courses(self):
        payload = dict()
        try:
            response = requests.get('http://localhost:8017/v1/courses', data=payload)
            if response.status_code == 200:
                print("Successful")
            else:
                print("Fail")
        except Exception as erorr:
            raise ValidationError(str(erorr))


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Open Academy Session'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2))
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    active = fields.Boolean(default=True)
    end_date = fields.Date(string="End date", store=True, compute='_get_end_date', inverse="_set_end_date")
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {'title': "Incorrect seats value",
                            'message': "The number of available seats may not be negative",
                            },
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {'title': "Too many attendees",
                            'message': "Increase seats or remove excess attendee",
                            },
            }

    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = r.start_date + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            r.duration = (r.end_date - r.start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A session's instructor can't be an attendee")
