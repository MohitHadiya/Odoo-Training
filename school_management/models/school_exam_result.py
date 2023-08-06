from odoo import fields, models, api


class SchoolExamResult(models.Model):
    _name = 'school.exam.result'
    _description = 'This is a results of exams.'

    student_id = fields.Many2one('school.student', string='Student')
    exam_id = fields.Many2one('school.exam', string='Exam')
    total_marks = fields.Float(string='Total Marks')
    obtained_marks = fields.Float(string='Obtained Marks')
