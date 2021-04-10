from odoo import models, fields, api
    
FUEL = [
    ('coal', 'Coal'),
    ('oil', 'Oil'),
    ('gas', 'Gas'),
]

TYPE_SHIP = [
    ('explorer','Explorer'),
    ('battle','Battle'),
]

class Spaceship(models.Model):
    _name = 'test_bug.spaceship'
    _description = "Space Crew"

    name = fields.Char(string="Ship", required=True)
    description = fields.Text(string="Descripción")
    width = fields.Float("Ancho")
    high = fields.Float("Alto")
    fuel = fields.Selection(FUEL, default=FUEL[0][0],string="Combustible") 
    type_ship = fields.Selection(TYPE_SHIP, default=TYPE_SHIP[0][0], string="Tipo de barco")
    passengers = fields.Integer(string="Número de pasajeros")
    active = fields.Boolean(string="Activa")   