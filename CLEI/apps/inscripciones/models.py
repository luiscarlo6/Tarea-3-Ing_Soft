'''
Created on 14/12/2013

@author: ubuntu
'''
from django.db import models
from CLEI.apps.clei.models import Persona
from datetime import datetime

class Participante(Persona):
    correo = models.EmailField()
    direcionPostal = models.CharField(max_length = 64)
    url = models.CharField(max_length = 64)
    numeroTelefono = models.CharField(max_length = 64)
    
    def __unicode__(self):
        cadena = "%s %s"%(self.nombre, self.apellido)
        cadena += " %s %s"%(self.correo, self.numeroTelefono)
        return cadena
    
class Inscripcion(models.Model):

    persona = models.ForeignKey(Participante)
    fecha_inscripcion = models.DateTimeField(default = datetime.now)
    tipo_de_inscripcion = models.CharField(max_length = 64)
    tipo_de_descuento = models.CharField(max_length = 64)
    monto_cancelado = models.IntegerField(default = 0)
    
    def __unicode__(self):
        insc = "%s %s %s"%(self.Persona.__unicode__(), self.fecha_inscripcion, self.tipo_de_inscripcion)
        return insc