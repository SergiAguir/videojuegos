# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time
from odoo.exceptions import ValidationError

class juego_model(models.Model):
    _name = 'videojuegos.juego_model'
    _description = 'Modelo de juego'
    _sql_constraints = [("sql_check_name_juego", "UNIQUE(name)","Error en el juego. El juego ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre del juego",index=True)
    id = fields.Integer(string="Id",required=True,help="Id del juego")
    foto = fields.Binary()
    fecha = fields.Date(string="Fecha de lanzamiento", default=lambda self: datetime.today())
    calificacion = fields.Selection(selection=[('1', '1'),('2','2'),('3','3'),('4','4'),('5','5')])
    prestado = fields.Boolean(string="Esta prestado?", default=False)
    precio = fields.Float(string="Precio",required=True,help="Precio del juego")
    #Relacion uno a muchos con genero
    cod_genero = fields.Many2one("videojuegos.genero_model")
    #Relacion uno a muchos con prestamo
    cod_prestamo = fields.Many2many("videojuegos.prestamo_model")
    #Relacion uno a muchos con dfacturas
    cod_dfactura = fields.One2many("videojuegos.dfactura_model","cod_juego")

    def cambiaEstado(self):
          self.ensure_one()
          self.prestado = not self.prestado
          return True

    @api.constrains("precio")
    def checkPrecio(self):
          self.ensure_one()
          if self.precio <= 0:
               raise ValidationError("El precio tiene que ser mayor que 0!")