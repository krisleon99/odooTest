# -*- coding: utf-8 -*-
from odoo import fields, models


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title')
    edition_date = fields.Date()

