# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import ValidationError, UserError


class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'
    
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    
    name = fields.Char(string='Title')

    author_ids = fields.Many2many("library.partner", string="Authors")
    edition_date = fields.Date()
    isbn = fields.Char(string='ISBN')
    publisher_id = fields.Many2one('library.publisher', string='Publisher')

    rental_ids = fields.One2many('library.rental', 'book_id', string='Rentals')
    
    face = fields.Image(string="Portada")
    
    base_price = fields.Float(string="Precio base", default=0.00)
    aditional_price = fields.Float(string="Precio base", default=0.00)
    total = fields.Float(string="Precio base", readonly=True)

    
    @api.onchange("base_price","aditional_price")
    def _onchange_total(self):
        if self.base_price < 0.00:
            raise UserError("El precio base es negativo")
            
        self.total =  self.base_price + self.aditional_price
        
        
    @api.constrains("aditional_price")
    def _check_aditional_fee(self):
        for records in self:
            if self.aditional_price < 10:
                raise ValidationError("No puede ser la tarifa adicional menor a 10")
        