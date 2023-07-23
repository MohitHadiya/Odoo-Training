from odoo import fields, models, api


class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Description'

    name = fields.Char(string='Class Name', required=True)
    teacher_id = fields.Many2one('school.teacher', string='Class Teacher')
    students_ids = fields.One2many('school.student', 'class_id', string='Students')
    subjects_ids = fields.Many2many('school.subject', string='Subjects')
