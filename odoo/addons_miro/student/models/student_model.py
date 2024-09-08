from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    student_id = fields.Char(string='Student ID', required=True)
    class_name = fields.Char(string='Class Name')
    enrollment_date = fields.Date(string='Enrollment Date')
