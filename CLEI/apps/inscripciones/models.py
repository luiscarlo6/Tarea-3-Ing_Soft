'''
Created on 14/12/2013

@author: ubuntu
'''
from CLEI.apps.clei.models import Persona
from datetime import datetime
from django.db import models


class Participante(Persona):
    correo = models.EmailField()
    direcionPostal = models.CharField(max_length=64)
    url = models.CharField(max_length=64)
    numeroTelefono = models.CharField(max_length=64)
    
    def __unicode__(self):
        cadena = "%s %s" % (self.nombre, self.apellido)
        cadena += " %s %s" % (self.correo, self.numeroTelefono)
        return cadena
    
    
class TipoDeInscripcion(models.Model):
    
    
    def __init__(self, *args, **kwargs):
        models.Model.__init__(self, *args, **kwargs)
    
    def __unicode__(self):
        return ""
    
class AsistenciaExclusivaCharlas(TipoDeInscripcion):
    NOMBRE = "Asistencia Exclusiva a Charlas\n"
    precio = models.IntegerField(default=0)
    beneficios = models.CharField(max_length=128)
    charlas = models.CharField(max_length=128)  # aqui van llas charlas

class AsistenciaExclusivaTalleres(TipoDeInscripcion):
    NOMBRE = "Asistencia Exclusiva a Talleres\n"
    precio = models.IntegerField(default=0)
    beneficios = models.CharField(max_length=128)
    talleres = models.CharField(max_length=128)
    
class AsistenciaCharlasYTalleres(TipoDeInscripcion):
    NOMBRE = "Asistencia a Charlar y Talleres\n"
    precio = models.IntegerField(default=0)
    beneficios = models.CharField(max_length=128)
    eventos = models.CharField(max_length=128)
    
class AsistenciaGeneral(TipoDeInscripcion):

    def __init__(self):
        TipoDeInscripcion.__init__(self)
        self.precio = 250
        self.beneficios = 'beneficios'
        self.eventos = 'eventos'    

    NOMBRE = "Asistencia General\n"
    precio = models.IntegerField(default=0)
    beneficios = models.CharField(max_length=128)
    eventos = models.CharField(max_length=128)    
    
    
        
class TipoDeDescuento(models.Model):
    '''
    classdocs
    '''
    def monto_de_descuento(self):
        raise NotImplementedError("Excepcion, TipoDeDescuento")

    def porcentaje_de_descuento(self):
        raise NotImplementedError("Excepcion, TipoDeDescuento")

class Ninguno(TipoDeDescuento):
    NOMBRE_DESCUENTO = "Ninguno"
    valor_paquete = models.IntegerField(default=0)
    valor_descuento = models.CharField(max_length=128)

    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

class Academico(TipoDeDescuento):
    NOMBRE_DESCUENTO = "Academico"
    valor_paquete = models.IntegerField(default=0)
    valor_descuento = models.CharField(max_length=128)
    
    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

class CompraTemprana(TipoDeDescuento):
    NOMBRE_DESCUENTO = "Compra Temprana"
    valor_paquete = models.IntegerField(default=0)
    valor_descuento = models.CharField(max_length=128)
    
    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

class Inscripcion(models.Model):

    persona = models.ForeignKey(Participante)
    fecha_inscripcion = models.DateTimeField(default=datetime.now)
    tipo_de_inscripcion = models.ForeignKey(TipoDeInscripcion)
    tipo_de_descuento = models.ForeignKey(TipoDeDescuento)
    monto_cancelado = models.IntegerField(default=0)
    
    def __unicode__(self):
        insc = "%s %s %s" % (self.persona.__unicode__(), self.fecha_inscripcion, self.tipo_de_inscripcion)
        return insc
