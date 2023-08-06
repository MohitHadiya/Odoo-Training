# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import UserError


def set_name(self):
    if self.full_name:
        name_list = self.full_name.split(" ")
        if len(name_list) > 1:
            self.last_name = name_list[-1]
        self.first_name = name_list[0]


def _compute_fullname(self):
    for rec in self:
        rec.full_name = (rec.first_name or '') + " " + (rec.last_name or '')


class SchoolStudent(models.Model):
    _name = 'school.student'
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _rec_name = 'full_name'
    _description = 'School Student Data'

    first_name = fields.Char(required=True, tracking=True)
    last_name = fields.Char()
    full_name = fields.Char(string="Name", compute=_compute_fullname, inverse=set_name)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer()
    contact_number = fields.Char(string='Contact Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default="male")
    state = fields.Selection([('new', 'New'), ('enrolled', 'Enrolled'), ('pass_out', 'Pass Out'), ('cancel', 'Cancel')],
                             default="new")
    address = fields.Text(string='Address')
    image = fields.Image()
    class_id = fields.Many2one('school.class', string='Class')
    class_teacher_id = fields.Many2one('school.teacher')
    subjects_ids = fields.Many2many('school.subject')

    @api.constrains("date_of_birth")
    def check_date_of_birth(self):
        if self.date_of_birth and self.date_of_birth > datetime.now().date():
            raise UserError("Date of birth can't be a future date.")

    @api.onchange("class_id")
    def onchange_class(self):
        self.subjects_ids = self.class_id.subjects_ids
        self.class_teacher_id = self.class_id.teacher_id.id

    @api.onchange("date_of_birth")
    def onchange_date_of_birth(self):
        today = datetime.now().date()
        for student in self:
            if student.date_of_birth:
                age_in_days = (today - student.date_of_birth).days
                student.age = age_in_days // 365

    def action_cancel(self):
        self.state = 'cancel'

    @api.model_create_multi
    def create(self, vals):
        rec = super().create(vals)
        return rec

    def write(self, vals):
        rec = super().write(vals)
        return rec

    def copy(self, default_values=None):
        default_values = {"first_name": self.first_name + " - copy"}
        rec = super().copy(default_values)
        return rec

    def unlink(self):
        rec = super().unlink()
        return rec
