'''
Created on 14/12/2013

@author: luiscarlo
'''
from datetime import date

from django.db import models


#from Persona import Participante
class Inscripcion(models.Model):
    tarifa = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=0)
    pago = models.IntegerField(default=0)
    persona_a_inscribir = models.CharField(max_length = 100)

    def __init__(self, tarifa, fecha, pago):
        if (isinstance(tarifa, long) and 
            isinstance(fecha, date) and 
            isinstance(pago, long)):
              
            self.__tarifa = tarifa
            self.__fecha = fecha
            self.__pago = pago
        else:
            raise ValueError
          
#     def get_tarifa(self):
#         return self.__tarifa
#     
#  
#     def get_fecha(self):
#         return self.__fecha
#  
#  
#     def get_pago(self):
#         return self.__pago
#  
#  
#     def get_persona_a_inscribir(self):
#         return self.__persona_a_inscribir
#  
#  
#     def set_tarifa(self, value):
#         self.__tarifa = value
#  
#  
#     def set_fecha(self, value):
#         self.__fecha = value
#  
#  
#     def set_pago(self, value):
#         self.__pago = value
#  
#  
#     def set_persona_a_inscribir(self, value):
#         self.__persona_a_inscribir = value

        