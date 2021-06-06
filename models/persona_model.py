# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class persona_model(models.Model):
    _name = 'videojuegos.persona_model'
    _description = 'Modelo de persona'
    _sql_constraints = [("sql_check_dni_persona", "UNIQUE(dni)","Error en la persona. El dni ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre de la persona",index=True)
    apellidos = fields.Char(string="Apellidos",required=True,help="Apellidos de la persona",index=True)
    dni = fields.Char(string="DNI",required=True,help="DNI de la persona",index=True)
    telf = fields.Integer(string="Telefono",required=True,help="Telefono de la persona",index=True)
    email = fields.Char(string="Email",required=True,help="Email de la persona",index=True)
    foto = fields.Binary()
    edad = fields.Integer(string="Edad",required=True,help="Edad de la persona",index=True)
    localidad = fields.Char(string="Localidad",required=True,help="Localidad de la persona",index=True)
    #Relacion uno a muchos persona con vendedor
    cod_vendedor = fields.Many2one("videojuegos.vendedor_model")
    #Relacion uno a muchos persona con socio
    cod_socio = fields.Many2one("videojuegos.socio_model")


    def check_DNI(self, dni):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")

    @api.constrains("email")
    def _comprobarEmail(self):
        if len(self.email)>5:
            if "@" not in self.email:
                raise ValidationError("El email tiene que contener una @")
        else:
            raise ValidationError("El email tiene que tener mas de 5 caracteres")