# -*- coding: utf-8 -*-

from odoo import models, fields, api


class genero_model(models.Model):
    _name = 'videojuegos.genero_model'
    _description = 'Modelo de genero'
    _sql_constraints = [("sql_name_check", "UNIQUE(name)","Error en el genero. El genero ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre de genero")
    descripcion = fields.Html()
    #Relacion uno a muchos con juego
    cod_juego = fields.One2many("videojuegos.juego_model","cod_genero")
