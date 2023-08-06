from odoo import fields, models, api


class SchoolExam(models.Model):
    _name = 'school.exam'
    _description = 'This is a exam table of school management'
    _rec_name = 'name'

    name = fields.Char(string='Exam Name', required=True)
    date = fields.Date(string='Exam Date')
    subject_id = fields.Many2one('school.subject', string='Subject')
    class_id = fields.Many2one('school.class', string='Class')
    result_ids = fields.One2many('school.exam.result', 'exam_id', string='Results')
