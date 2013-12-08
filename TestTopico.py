# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
import unittest

from Topico import Topico


class TestTopico(unittest.TestCase):

    # Prueba para que el nombre del Topico
    # sea no vacia
    def test_Vacio(self):
        Caso = ""
        assert Topico().Agregar_Topico(Caso) == False

    # Prueba para que nombre este compuesta
    def test_Vacio_1(self):
        Caso = "      "
        assert Topico().Agregar_Topico(Caso) == False

    def test_Error_tipo(self):
        Caso = 123456789
        assert Topico().Agregar_Topico(Caso) == False

    # Nombre correcto
    def test_Correcto(self):
        Caso = "Computacion"
        assert Topico().Agregar_Topico(Caso) == True

    # Nombre con espacios
    def test_Espacio_Nombre(self):
        Caso = "Computacion 1"
        assert Topico().Agregar_Topico(Caso) == True

    # Nombre iguales pero uno de ellos tiene espacio al inicio o al final
    def test_Nombre_Iguales(self):
        Caso = "  Computacion  "
        assert Topico().Agregar_Topico(Caso) == True

    # Prueba de eliminar
    def test_Agregar_Eliminar(self):
        Caso = "C1"
        Caso1 = "C11"
        Caso2 = 123456789
        Aux = Topico()
        assert Aux.Agregar_Topico(Caso) == True
        assert Aux.Eliminar_Topico(Caso1) == False
        assert Aux.Eliminar_Topico(Caso2) == False
        assert Aux.Eliminar_Topico(Caso) == True

    # Prueba de eliminar
    def test_Listar(self):
        Caso = "C1"
        Caso1 = "C2"
        Aux = Topico()
        Aux1 = []
        Aux1.append(Caso)
        Aux1.append(Caso1)
        Aux1 = sorted(Aux1)

        Aux.Agregar_Topico(Caso)
        Aux.Agregar_Topico(Caso1)
        assert Aux.Listar_Topico() == Aux1

    # cantidad de elementos
    def test_Cantidad(self):
        topico = Topico()
        for i in range(10):
            A = "C"
            A += str(i)
            topico.Agregar_Topico(A)
        assert topico.Cantidad_Topico() == 10


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
