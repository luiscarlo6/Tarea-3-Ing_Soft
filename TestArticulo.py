# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
import sys
import unittest

from Articulo import Articulo
from Persona import Persona
from Topico import Topico


class TestArticulo(unittest.TestCase):

    # Todos los atributos corrrectos
    def test_Atributos_correctos(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = "MyArticulo"
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        Autor = Persona(Nombre, Apellido, Pais, Institucion)

        Lista_Persona = []
        Lista_Persona.append(Autor)

        topico = Topico()
        topico.Agregar_Topico(Caso)

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_titulo() == Titulo

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_topico() == topico

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_topico() == topico

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_autor() == Lista_Persona

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_resumen() == Resumen

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        get_es_aceptado() == True

    # Un atributo incorrecto
    def test_Atributos_Incorrectos(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = "MyArticulo"
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        ERROR = 123456789

        Autor = Persona(Nombre, Apellido, Pais, Institucion)

        Lista_Persona = []
        Lista_Persona.append(Autor)

        topico = Topico()
        topico.Agregar_Topico(Caso)

        assert  Articulo(ERROR, topico, Lista_Persona, Resumen, EsAceptado).\
        get_titulo() == None

        assert  Articulo(Titulo, ERROR, Lista_Persona, Resumen, EsAceptado).\
        get_topico() == None

        assert  Articulo(Titulo, topico, ERROR, Resumen, EsAceptado).\
        get_autor() == None

        assert  Articulo(Titulo, topico, Lista_Persona, ERROR, EsAceptado).\
        get_resumen() == None

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, ERROR).\
        get_es_aceptado() == None

    # Pruebas de set
    def test_Set(self):
        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = "MyArticulo"
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        Autor = Persona(Nombre, Apellido, Pais, Institucion)

        Lista_Persona = []
        Lista_Persona.append(Autor)

        topico = Topico()
        topico.Agregar_Topico(Caso)

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_titulo("Nuevo") == True

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_titulo("") == False

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_topico(Topico()) == False

        Aux = Topico()
        Aux.Agregar_Topico("NombreTopico")
        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_topico(Aux) == True

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_autor(Persona()) == False

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_autor([]) == False

        Aux = []
        assert Autor.set_pais("VEN")
        Aux.append(Autor)

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_autor(Aux) == True

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_resumen([]) == False

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_resumen(["D", "E", "F", "G"]) == True

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_resumen(["D", "E", "F", "G", "H"]) == True

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_es_aceptado("value") == False

        assert  Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado).\
        set_es_aceptado("N") == True

    # Test de nota
    def test_Notas(self):

        Nombre = "Jose"
        Apellido = "Prado"
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = "MyArticulo"
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        Autor = Persona(Nombre, Apellido, Pais, Institucion)

        Lista_Persona = []
        Lista_Persona.append(Autor)

        topico = Topico()
        topico.Agregar_Topico(Caso)

        articulo = Articulo(Titulo, topico, Lista_Persona, Resumen, EsAceptado)

        assert articulo.get_promedio() == 0.0

        assert articulo.get_Nota() == []

        for i in range(10):
            articulo.Agregar_Nota(i)

        assert articulo.get_Nota() == [i + 1 for i in range(5)]

        assert articulo.Agregar_Nota(sys.maxint + sys.maxint) == False

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
