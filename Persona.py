# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''


class Persona(object):
    '''
    classdocs
    '''

    # Constructor
    def __init__(self, Nombre=None, Apellido=None, Pais=None, \
    Institucion=None):
        # Chequeo de tipos
        SonNone = type(Nombre) != None and type(Apellido) != None and \
        type(Pais) != None and type(Institucion) != None

        if (type(Nombre) == str) and (type(Apellido) == str) and \
        (type(Pais) == str) and (type(Institucion) == str) and SonNone:

            # Eliminacion de espacios antes y despues de la palabra
            Nombre = Nombre.strip()
            Apellido = Apellido.strip()
            Pais = Pais.strip()
            Institucion = Institucion.strip()

            # chequeo de palabra vacia
            Longitud_vacia = (len(Nombre) == 0) or (len(Apellido) == 0) or \
            (len(Pais) == 0) or (len(Institucion) == 0)

            if Longitud_vacia:
                self.__Inicializar_None()
            else:
                self.__Nombre = Nombre
                self.__Apellido = Apellido
                self.__Pais = Pais
                self.__Institucion = Institucion

        else:
            self.__Inicializar_None()

    # Inicializa en None
    def __Inicializar_None(self):
        self.__Nombre = None
        self.__Apellido = None
        self.__Pais = None
        self.__Institucion = None

    # Retorna el nombre de la persona
    def get_nombre(self):
        return self.__Nombre

    # Retorna el apellido de la persona
    def get_apellido(self):
        return self.__Apellido

    # Retorna el pais de la persona
    def get_pais(self):
        return self.__Pais

    # Retorna la institucion de la persona
    def get_institucion(self):
        return self.__Institucion

    # Cambia el nombre de la persona
    def set_nombre(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Nombre = value
                return True
        return False

    # Cambia el apellido de la persona
    def set_apellido(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Apellido = value
                return True
        return False

    # Cambia el pais de la persona
    def set_pais(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Pais = value
                return True
        return False

    # Cambia el institucion de la persona
    def set_institucion(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Institucion = value
                return True
        return False


if __name__ == '__main__':
    pass
