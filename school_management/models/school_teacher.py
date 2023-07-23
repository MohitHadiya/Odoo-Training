from odoo import fields, models, api


class SchoolTeacher(models.Model):
    _name = 'school.teacher'
    _description = 'School Teacher Data'
    _rec_name = 'full_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    full_name = fields.Char(string="Name")
    date_of_birth = fields.Date(string='Date of Birth')
    age = fields.Integer()
    qualification = fields.Char()
    contact_number = fields.Char(string='Contact Number')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default="male")
    address = fields.Text(string='Address')
    image = fields.Image()
    subjects_ids = fields.Many2many('school.subject', string='Subjects Taught')
