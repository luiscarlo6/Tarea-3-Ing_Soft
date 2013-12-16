'''
Created on 14/12/2013

@author: ubuntu
'''

from Persona import Participante

import datetime

# Importo el paquete de inscripcion
from inscripcion.TipoDeInscripcion import TipoDeInscripcion, AsistenciaCharlasYTalleres, AsistenciaExclusivaCharlas, AsistenciaExclusivaTalleres
from inscripcion.TipoDeDescuento import TipoDeDescuento, Ninguno, CompraTemprana, Academico


class Inscripcion(object):

    __persona = None
    __fecha_inscripcion = None
    __tipo_de_inscripcion = None
    __tipo_de_descuento = None
    __monto_cancelado = None

    def __init__(self, persona, fechaInscripcion, tipoInscripcion, \
                  tipoDescuento):
        if isinstance(persona, Participante) and \
            isinstance(fechaInscripcion, datetime.datetime) and \
            isinstance(tipoInscripcion, TipoDeInscripcion) and \
            isinstance(tipoDescuento, TipoDeDescuento):

            self.__persona = persona
            self.__fecha_inscripcion = fechaInscripcion
            self.__tipo_de_inscripcion = tipoInscripcion
            self.__tipo_de_descuento = tipoDescuento
            self.__monto_cancelado = tipoInscripcion.get_precio() - \
                                        tipoDescuento.monto_de_descuento()

        else:
            raise TypeError

    def get_persona(self):
        return self.__persona

    def get_fecha_inscripcion(self):
        return self.__fecha_inscripcion

    def get_tipo_de_inscripcion(self):
        return self.__tipo_de_inscripcion

    def get_tipo_de_descuento(self):
        return self.__tipo_de_descuento

    def get_monto_cancelado(self):
        return self.__monto_cancelado

    def set_persona(self, value):
        if isinstance(value, Participante):
            self.__persona = value
        else:
            raise TypeError

    def set_fecha_inscripcion(self, value):
        if isinstance(value, datetime):
            self.__fecha_inscripcion = value
        else:
            raise TypeError

    def set_tipo_de_inscripcion(self, value):
        if isinstance(value, TipoDeInscripcion):
            self.__tipo_de_inscripcion = value
        else:
            raise TypeError

    def set_tipo_de_descuento(self, value):
        if isinstance(value, TipoDeDescuento):
            self.__tipo_de_descuento = value
        else:
            raise TypeError

    def set_monto_cancelado(self, value):
        if isinstance(value, float):
            self.__monto_cancelado = value
        else:
            raise TypeError

    def __str__(self):
        Cadena = str(self.get_persona()) + "\n"
        Cadena += str(self.get_fecha_inscripcion()) + "\n"
        Cadena += str(self.get_tipo_de_inscripcion()) + "\n"
        Cadena += str(self.get_tipo_de_descuento()) + "\n"
        Cadena += str(self.get_monto_cancelado()) + "\n"
        return Cadena

if __name__ == '__main__':

    # la Persona a inscribirse
    Par = Participante("Jose", "Prado", "USB", "VEN", ["Bases"],
                       "josejulianprado@gmail.com", "1220", "www.usb.ve",
                       "+584162068514")
    #print Par

    # fecha
    Hoy = datetime.datetime.now()
    #Hoy = Hoy.strftime("%d/%m/%Y")
    #print Hoy

    # tipo de inscripcion
    tipoInscripcion = AsistenciaExclusivaTalleres(150.0, ["VIP"], ["Ponencia"])
    #print tipoInscripcion

    #descuento
    descuento = Ninguno(tipoInscripcion, 0.0)
    #print descuento

    ins = Inscripcion(Par,Hoy,tipoInscripcion, descuento)
    print ins
