# -*- coding: utf-8 -*-

from odoo import models, fields, api


def _compute_fullname(self):
    for student in self:
        student.full_name = student.first_name + " " + student.last_name


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'full_name'
    _description = 'School Student Data'

    first_name = fields.Char(required=True, tracking=True)
    last_name = fields.Char()
    full_name = fields.Char(string="Name", compute=_compute_fullname)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer()
    contact_number = fields.Char(string='Contact Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default="male")
    address = fields.Text(string='Address')
    image = fields.Image()
    class_id = fields.Many2one('school.class', string='Class')
    class_teacher_id = fields.Many2one('school.teacher')
    subjects_ids = fields.Many2many('school.subject')

    @api.onchange("class_id")
    def onchange_class(self):
        self.subjects_ids = self.class_id.subjects_ids
        self.class_teacher_id = self.class_id.teacher_id
