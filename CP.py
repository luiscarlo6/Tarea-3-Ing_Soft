# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
from Persona import Persona
from Topico import Topico


class CP(Persona):
    '''
    classdocs
    '''

    # CONSTRUCTOR

    def __init__(self, Nombre, Apellido, Pais, Institucion, \
    Correo, topico, EsPresidente):

        SonNone = type(Correo) != None and type(topico) != None and \
        type(EsPresidente) != None

        if (type(Correo) == str) and (isinstance(topico, Topico)) and \
        (type(EsPresidente) == str) and ((EsPresidente == "S") or \
        (EsPresidente == "N")) and SonNone:

            Persona.__init__(self, Nombre, Apellido, Pais, Institucion)

            if self.get_nombre() == None or topico.Cantidad_Topico() == 0:
                self.__Inicializar_None()
            else:
                Correo = Correo.strip()
                self.__Correo = Correo
                self.__topico = topico
                if EsPresidente == "S":
                    self.__EsPresidente = True
                elif EsPresidente == "N":
                    self.__EsPresidente = False

        else:
            Persona.__init__(self)
            self.__Inicializar_None()

    # Inicializa en none
    def __Inicializar_None(self):
        self.__Correo = None
        self.__topico = None
        self.__EsPresidente = None

    # Retorna correo
    def get_correo(self):
        return self.__Correo

    # Retorna topico
    def get_topico(self):
        return self.__topico

    # Retorna si es presidente
    def get_es_presidente(self):
        return self.__EsPresidente

    # Modifica Correo
    def set_correo(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Correo = value
                return True
        return False

    # Modifica topico
    def set_topico(self, value):
        if isinstance(value, Topico):
            if value.Cantidad_Topico() != 0:
                self.__topico = value
                return True
        return False

    # Modifica es Presidente
    def set_es_presidente(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0 and ((value == "S") or (value == "N")):
                if value == "S":
                    self.__EsPresidente = True
                    return True
                elif value == "N":
                    self.__EsPresidente = False
                    return True
        return False

if __name__ == '__main__':
    pass
