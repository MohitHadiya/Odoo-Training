# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _rec_name = 'full_name'
    _description = 'School Student Data'

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    full_name = fields.Char(string="Name")
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer()
    contact_number = fields.Char(string='Contact Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default="male")
    address = fields.Text(string='Address')
    image = fields.Image()
    class_id = fields.Many2one('school.class', string='Class')
    subjects_ids = fields.Many2many('school.subject')
