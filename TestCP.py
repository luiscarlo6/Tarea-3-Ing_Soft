# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
import unittest

from CP import CP
from Topico import Topico


class TestCP(unittest.TestCase):

    # prueba que se pasan todos los paramentros de forma correcta
    def test_parametros_correctos(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = "09-11006@usb.ve"
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = "S"

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_nombre() == Nombre

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_apellido() == Apellido

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_pais() == Pais

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_institucion() == Institucion

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_correo() == Correo

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_topico().Listar_Topico() == \
                  topico.Listar_Topico()

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                  EsPresidente).get_es_presidente() == True

    # Se pasa un parametro de forma incorrecta
    def test_parametros_Incorrecto(self):
            Nombre = "Jose"
            Apellido = "Prado"
            Pais = "Venezuela"
            Institucion = "USB"
            Correo = "09-11006@usb.ve"
            topico = Topico()
            topico.Agregar_Topico("Computacion_1")
            topico.Agregar_Topico("Computacion_2")
            EsPresidente = "S"
            Error = 1234567890

            assert CP(Error, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).get_nombre() == None

            assert CP(Nombre, Error, Pais, Institucion, Correo, topico, \
                      EsPresidente).get_apellido() == None

            assert CP(Nombre, Apellido, Error, Institucion, Correo, topico, \
                      EsPresidente).get_pais() == None

            assert CP(Nombre, Apellido, Pais, Error, Correo, topico, \
                      EsPresidente).get_institucion() == None

            assert CP(Nombre, Apellido, Pais, Institucion, Error, topico, \
                      EsPresidente).get_correo() == None

            assert CP(Nombre, Apellido, Pais, Institucion, Correo, Error, \
                      EsPresidente).get_topico() == None

            assert CP(Nombre, Apellido, Pais, Institucion, Correo, Topico(), \
                      EsPresidente).get_topico() == None

            assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      Error).get_es_presidente() == None

            assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      "A").get_es_presidente() == None

    # pruebas de set
    def test_set(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = "09-11006@usb.ve"
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = "S"
        Error = 1234567890

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_correo(Error) == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_topico(Error) == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_es_presidente(Error) == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_correo("josejulian@") == True

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_topico(Topico()) == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_topico(Topico()) == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_es_presidente("MM") == False

        assert CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                      EsPresidente).set_es_presidente("N") == True


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
