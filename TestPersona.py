# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
import unittest

from Persona import Persona


class TestPersona(unittest.TestCase):

    # Test de persona

    # Atributos correctos
    def test_Atributos_correctos(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"

        assert Persona(Nombre, Apellido, Pais, Institucion).get_nombre() \
        == Nombre

        assert Persona(Nombre, Apellido, Pais, Institucion).get_apellido() \
        == Apellido

        assert Persona(Nombre, Apellido, Pais, Institucion).get_pais() \
        == Pais

        assert Persona(Nombre, Apellido, Pais, Institucion).get_institucion() \
        == Institucion

    # Un atributo vacio
    def test_Atributo_Vacio(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Vacio = "    "

        assert Persona(Vacio, Apellido, Pais, Institucion).get_nombre() \
        != Nombre

        assert Persona(Vacio, Apellido, Pais, Institucion).get_nombre() \
        == None

        assert Persona(Nombre, Vacio, Pais, Institucion).get_apellido() \
        != Apellido

        assert Persona(Nombre, Vacio, Pais, Institucion).get_apellido() \
        == None

        assert Persona(Nombre, Apellido, Vacio, Institucion).get_pais() \
        != Pais

        assert Persona(Nombre, Apellido, Vacio, Institucion).get_pais() \
        == None

        assert Persona(Nombre, Apellido, Pais, Vacio).get_institucion() \
        != Institucion

        assert Persona(Nombre, Apellido, Pais, Vacio).get_institucion() \
        == None

    # Atributos con errores de tipo
    def test_Error_Tipos(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Error = 123456789

        assert Persona(Error, Apellido, Pais, Institucion).get_nombre() \
        == None

        assert Persona(Nombre, Error, Pais, Institucion).get_apellido() \
        == None

        assert Persona(Nombre, Apellido, Error, Institucion).get_pais() \
        == None

        assert Persona(Nombre, Apellido, Pais, Error).get_institucion() \
        == None

    # Prueba de los metodos set
    def test_Set(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Error = 123456789

        assert Persona(Nombre, Apellido, Pais, Institucion).set_nombre(Nombre)\
        == True

        assert Persona(Nombre, Apellido, Pais, Institucion).set_nombre(Error)\
        == False

        assert Persona(Nombre, Apellido, Pais, Institucion).\
        set_apellido(Apellido) == True

        assert Persona(Nombre, Apellido, Pais, Institucion).\
        set_apellido(Error) == False

        assert Persona(Nombre, Apellido, Pais, Institucion).set_pais(Pais) \
        == True

        assert Persona(Nombre, Apellido, Pais, Institucion).set_pais(Error) \
        == False

        assert Persona(Nombre, Apellido, Pais, Institucion).\
        set_institucion(Institucion) == True

        assert Persona(Nombre, Apellido, Pais, Institucion).\
        set_institucion(Error) == False

    def test_None(self):
        assert Persona().get_nombre() == None
        assert Persona().get_apellido() == None
        assert Persona().get_pais() == None
        assert Persona().get_institucion() == None

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
