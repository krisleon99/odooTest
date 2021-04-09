from odoo import models, fields, api

class Course(models.Model):
    _name = 'test_bug.course'
    _description = "OpenAcademy Courses"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()