# -*- coding: utf-8 -*-
from odoo import fields, models

PARTNER = [
    ('customer', 'Customer'), 
    ('author', 'Author'),
]

class Partner(models.Model):
    _name = 'library.partner'
    _description = 'Partner'

    name = fields.Char()
    email = fields.Char()
    address = fields.Text()
    partner_type = fields.Selection(PARTNER, default="customer")

    rental_ids = fields.One2many('library.rental', 'customer_id', string='Rentals')
