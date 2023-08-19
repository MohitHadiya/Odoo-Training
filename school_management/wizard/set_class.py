from odoo import fields, models, api


class SetClass(models.TransientModel):
    _name = 'set.class'
    _description = 'Description'

    class_id = fields.Many2one("school.class")

    def set_class(self):
        student_id = self._context.get("active_id")
        student = self.env['school.student'].browse(student_id)
        student.class_id = self.class_id.id
        student.onchange_class()
