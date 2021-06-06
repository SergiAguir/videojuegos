# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class prestamo_model(models.Model):
    _name = 'videojuegos.prestamo_model'
    _description = 'Modelo de prestamo'

    name = fields.Date(string="Fecha", default=lambda self: datetime.today())
    #Relacion uno a muchos con socio
    cod_socio = fields.Many2one("videojuegos.socio_model")
    #Relacion muchos a muchos con juego
    cod_juego = fields.Many2many("videojuegos.juego_model",string="Lista juegos")
    #Relacion uno a muchos con vendedor
    cod_vendedor = fields.Many2one("videojuegos.vendedor_model")