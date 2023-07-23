from odoo import fields, models, api


class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'School Subject Data'
    _rec_name = 'name'

    name = fields.Char(string='Subject Name', required=True)
    code = fields.Char(string='Subject Code')
    teacher_ids = fields.Many2many('school.teacher', string='Teachers')
    class_ids = fields.Many2many('school.class', string='Classes')
