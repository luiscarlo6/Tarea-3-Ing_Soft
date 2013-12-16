'''
Created on 14/12/2013

@author: ubuntu
'''
from inscripcion.TipoDeInscripcion import TipoDeInscripcion


class TipoDeDescuento(object):
    '''
    classdocs
    '''
    def monto_de_descuento(self):
        raise NotImplementedError("Excepcion, TipoDeDescuento")

    def porcentaje_de_descuento(self):
        raise NotImplementedError("Excepcion, TipoDeDescuento")

    def __str__(self):
        raise NotImplementedError("Excepcion, TipoDeDescuento")


class Ninguno(TipoDeDescuento):
    __NOMBRE_DESCUENTO = "Ninguno"
    __valor_paquete = None
    __valor_descuento = None

    def __init__(self, tipoDeInscripcion, porcentajeDescuento):
        if isinstance(tipoDeInscripcion, TipoDeInscripcion) and \
            isinstance(porcentajeDescuento, float):
            self.__valor_paquete = tipoDeInscripcion.get_precio()
            self.__valor_descuento = porcentajeDescuento
        else:
            raise NotImplementedError("Excepcion, TipoDeDescuento")

    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

    def __str__(self):
        Cadena = self.__NOMBRE_DESCUENTO + "\n"
        Cadena += "Descuento " + str(self.__valor_descuento) + "\n"
        Cadena += "Porcentaje de Descuento " + str(self.__valor_paquete) + "\n"
        return Cadena


class Academico(TipoDeDescuento):
    __NOMBRE_DESCUENTO = "Academico"
    __valor_paquete = None
    __valor_descuento = None

    def __init__(self, tipoDeInscripcion, porcentajeDescuento):
        if isinstance(tipoDeInscripcion, TipoDeInscripcion) and \
         isinstance(porcentajeDescuento, float):
            self.__valor_paquete = tipoDeInscripcion.get_precio()
            self.__valor_descuento = porcentajeDescuento
        else:
            raise NotImplementedError("Excepcion, TipoDeDescuento")

    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

    def __str__(self):
        Cadena = self.__NOMBRE_DESCUENTO + "\n"
        Cadena += "Descuento " + str(self.__valor_descuento) + "\n"
        Cadena += "Porcentaje de Descuento " + str(self.__valor_paquete) + "\n"
        return Cadena


class CompraTemprana(TipoDeDescuento):
    __NOMBRE_DESCUENTO = "Compra Temprana"
    __valor_paquete = None
    __valor_descuento = None

    def __init__(self, tipoDeInscripcion, porcentajeDescuento):
        if isinstance(tipoDeInscripcion, TipoDeInscripcion) and \
        isinstance(porcentajeDescuento, float):
            self.__valor_paquete = tipoDeInscripcion.get_precio()
            self.__valor_descuento = porcentajeDescuento
        else:
            raise NotImplementedError("Excepcion, TipoDeDescuento")

    def monto_de_descuento(self):
        Valor = self.__valor_paquete * self.__valor_descuento
        Valor *= 1 / 100
        return Valor

    def porcentaje_de_descuento(self):
        return self.__valor_descuento

    def __str__(self):
        Cadena = self.__NOMBRE_DESCUENTO + "\n"
        Cadena += "Descuento " + str(self.__valor_descuento) + "\n"
        Cadena += "Porcentaje de Descuento " + str(self.__valor_paquete) + "\n"
        return Cadena
