from odoo import fields, models, api
from .school_student import _compute_fullname, set_name


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher Data'
    _rec_name = 'full_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    full_name = fields.Char(string="Name", compute=_compute_fullname, inverse=set_name)
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer()
    qualification = fields.Char()
    contact_number = fields.Char(string='Contact Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default="male")
    address = fields.Text(string='Address')
    image = fields.Image()
    subjects_ids = fields.Many2many('school.subject', string='Subjects Taught')
