# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class factura_model(models.Model):
    _name = 'videojuegos.factura_model'
    _description = 'Modelo de factura'
    _sql_constraints = [("sql_check_name_factura", "UNIQUE(name)","Error en la factura. La referencia ya existe!"), ]


    name= fields.Integer(string="Referencia",help="Referencia de la Factura")
    fecha= fields.Date(string="Fecha", default=lambda self: datetime.today())
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)
    total = fields.Float(string="Total", compute="_calc_iva", store=True)
    #Relacion uno a muchos con socio
    cod_socio = fields.Many2one("videojuegos.socio_model",string="Socio")
    #Relacion uno a muchos con socio
    cod_dfactura = fields.One2many("videojuegos.dfactura_model","cod_factura",string="Factura")

    @api.depends('cod_dfactura')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.cod_dfactura:
            suma += i.cod_juego.precio*i.cantidad
        self.base = suma
    
    @api.depends('iva', 'base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)