# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class dfactura_model(models.Model):
    _name = 'videojuegos.dfactura_model'
    _description = 'Modelo de detalle factura'

    #Relacion uno a muchos con factura
    cod_factura = fields.Many2one("videojuegos.factura_model",string="Factura")
    #Relacion uno a muchos con juego
    cod_juego = fields.Many2one("videojuegos.juego_model",string="Juego")
    cantidad = fields.Integer(string="Cantidad",default=1,required=True)

    @api.constrains('cantidad')
    def _comprobarCant(self):
        for i in self:
            if i.cantidad < 0:
                   raise ValidationError("La minima catidad de un producto tiene que ser 1")