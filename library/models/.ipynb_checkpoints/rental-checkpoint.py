# -*- coding: utf-8 -*-
from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'
    
    book_id = fields.Many2one('library.book', string='Book')

    rental_date = fields.Date()
    return_date = fields.Date()
