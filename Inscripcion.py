'''
Created on 14/12/2013

@author: luiscarlo
'''
from datetime import date

from Persona import Asistente

class Inscripcion(object):
    __tarifa = None
    __fecha = None
    __pago = None
    __persona_a_inscribir = None

    def __init__(self, tarifa, fecha, pago, persona_a_inscribir):
        if (isinstance(persona_a_inscribir, Asistente) and 
            isinstance(tarifa, long) and 
            isinstance(fecha, date) and 
            isinstance(pago, long)):
            
            self.__tarifa = tarifa
            self.__fecha = fecha
            self.__pago = pago
            self.__persona_a_inscribir = persona_a_inscribir
        else:
            raise ValueError
        
    def get_tarifa(self):
        return self.__tarifa
   

    def get_fecha(self):
        return self.__fecha


    def get_pago(self):
        return self.__pago


    def get_persona_a_inscribir(self):
        return self.__persona_a_inscribir


    def set_tarifa(self, value):
        self.__tarifa = value


    def set_fecha(self, value):
        self.__fecha = value


    def set_pago(self, value):
        self.__pago = value


    def set_persona_a_inscribir(self, value):
        self.__persona_a_inscribir = value

        