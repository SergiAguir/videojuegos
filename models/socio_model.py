# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class socio_model(models.Model):
    _name = 'videojuegos.socio_model'
    _description = 'Modelo de socio'
    _sql_constraints = [("sql_check_id_socio", "UNIQUE(name)","Error en el socio. El id ya existe!"), ]

    name = fields.Integer(string="Id",required=True,help="Id de socio")
    fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
    #Releacion uno a muchos con persona
    cod_persona = fields.One2many("videojuegos.persona_model","cod_socio")
    #Relacion uno a muchos con prestamo
    cod_prestamo = fields.One2many("videojuegos.prestamo_model","cod_socio")
    #Relacion uno a muchos con factura
    cod_factura = fields.One2many("videojuegos.factura_model","cod_socio")