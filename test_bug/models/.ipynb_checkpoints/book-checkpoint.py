# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LibraryManagement(models.Model):
    _name = 'test_bug.library_management'
    _description = "Management library"

    name = fields.Char(string="Book", required=True)
    description = fields.Text(string="Descripción")
    author = fields.Char(string="Autor")
    editor = fields.Char(string="Editores")