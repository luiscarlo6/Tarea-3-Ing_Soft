# -*- coding: utf-8 -*-
'''
Created on 24/11/2013

@author: ubuntu
'''

import sys
import unittest

from Articulo import Articulo
from CP import CP
from Evaluacion import Evaluacion
from Persona import Persona
from Topico import Topico


class TestEvaluacion(unittest.TestCase):

    # Test Correctitud
    def test_parametros_Correctos(self):

        Nombre = ["Jose", "Jose1", "Jose2"]
        Apellido = ["Prado", "Prado1", "Prado2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = ["09-11006@usb.ve", "josejulianprado@gmail.com", "API"]
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = ["S", "N", "N"]

        # Lista de CP
        Lista_CP = []
        for i in range(3):
            Aux = CP(Nombre[i], Apellido[i], Pais, Institucion, \
            Correo[i], topico, EsPresidente[i])
            Lista_CP.append(Aux)

        # Lista de Articulos
        Lista_Art = []

        Nombre = ["Luis", "Luis1", "Luis2"]
        Apellido = ["Rivera", "Rivera1", "Rivera2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = ["MyArticulo", "MyArticulo1", "MyArticulo2"]
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        for i in range(3):
            Autor = Persona(Nombre[i], Apellido[i], Pais, Institucion)

            Lista_Persona = []
            Lista_Persona.append(Autor)

            topico = Topico()
            topico.Agregar_Topico(Caso)

            Aux = Articulo(Titulo[i], topico, Lista_Persona, Resumen, \
            EsAceptado)

            Lista_Art.append(Aux)

            Aux = Evaluacion(Lista_Art, Lista_CP)

        assert Aux.get_articulos() == Lista_Art

        assert Aux.get_cp() == Lista_CP

    # Prueba de correctitup para evaluar
    def test_Parametros_Errores(self):
        Nombre = ["Jose", "Jose1", "Jose2"]
        Apellido = ["Prado", "Prado1", "Prado2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = ["09-11006@usb.ve", "josejulianprado@gmail.com", "API"]
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = ["S", "N", "N"]

        # Lista de CP
        Lista_CP = []
        for i in range(3):
            Aux = CP(Nombre[i], Apellido[i], Pais, Institucion, \
            Correo[i], topico, EsPresidente[i])
            Lista_CP.append(Aux)

        # Lista de Articulos
        Lista_Art = []

        Nombre = ["Luis", "Luis1", "Luis2"]
        Apellido = ["Rivera", "Rivera1", "Rivera2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = ["MyArticulo", "MyArticulo1", "MyArticulo2"]
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        for i in range(3):
            Autor = Persona(Nombre[i], Apellido[i], Pais, Institucion)

            Lista_Persona = []
            Lista_Persona.append(Autor)

            topico = Topico()
            topico.Agregar_Topico(Caso)

            Aux = Articulo(Titulo[i], topico, Lista_Persona, Resumen, \
            EsAceptado)

            Lista_Art.append(Aux)

            Aux = Evaluacion(None, None)

        assert Aux.get_articulos() == None

        assert Aux.get_cp() == None

        assert Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", 1)\
        == False

        assert Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", 5)\
        == False

        assert Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", \
        sys.maxint) == False

        assert Aux.Agregar_Evaluacion("MyArticulo", \
        "josejulianprado@gmail.com", 1) == False

        assert Aux.Agregar_Evaluacion("MyArticulo", "API", 1) == False

    # Prueba de correctitup para evaluar
    def test_Calculo_de_promedio(self):
        Nombre = ["Jose", "Jose1", "Jose2"]
        Apellido = ["Prado", "Prado1", "Prado2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = ["09-11006@usb.ve", "josejulianprado@gmail.com", "API"]
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = ["S", "N", "N"]

        # Lista de CP
        Lista_CP = []
        for i in range(3):
            Aux = CP(Nombre[i], Apellido[i], Pais, Institucion, \
            Correo[i], topico, EsPresidente[i])
            Lista_CP.append(Aux)

        # Lista de Articulos
        Lista_Art = []

        Nombre = ["Luis", "Luis1", "Luis2"]
        Apellido = ["Rivera", "Rivera1", "Rivera2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = ["MyArticulo", "MyArticulo1", "MyArticulo2"]
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        for i in range(3):
            Autor = Persona(Nombre[i], Apellido[i], Pais, Institucion)

            Lista_Persona = []
            Lista_Persona.append(Autor)

            topico = Topico()
            topico.Agregar_Topico(Caso)

            Aux = Articulo(Titulo[i], topico, Lista_Persona, Resumen, \
            EsAceptado)

            Lista_Art.append(Aux)

            Aux = Evaluacion(Lista_Art, Lista_CP)

        assert Aux.get_articulos() != None

        assert Aux.get_cp() != None

        Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", 5)

        Aux.Agregar_Evaluacion("MyArticulo", "josejulianprado@gmail.com", 3)
        Aux.Agregar_Evaluacion("MyArticulo", "API", 3)

        Aux.Generar_Promedios_Evaluacion()

        Ali = 0
        for i in Aux.get_articulos():
            if Ali == 0:
                assert i.get_promedio() == 3.67
            elif Ali == 1:
                assert i.get_promedio() == -1.0
            elif Ali == 2:
                assert i.get_promedio() == -1.0
            Ali += 1

    # pruebas de listas
    def test_Lista(self):
        Nombre = ["Jose", "Jose1", "Jose2"]
        Apellido = ["Prado", "Prado1", "Prado2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = ["09-11006@usb.ve", "josejulianprado@gmail.com", "API"]
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = ["S", "N", "N"]

        # Lista de CP
        Lista_CP = []
        for i in range(3):
            Aux = CP(Nombre[i], Apellido[i], Pais, Institucion, \
            Correo[i], topico, EsPresidente[i])
            Lista_CP.append(Aux)

        # Lista de Articulos
        Lista_Art = []

        Nombre = ["Luis", "Luis1", "Luis2", "Luis3"]
        Apellido = ["Rivera", "Rivera1", "Rivera2", "Rivera3"]
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = ["MyArticulo", "MyArticulo1", "MyArticulo2", "MyArticulo3"]
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        for i in range(4):
            Autor = Persona(Nombre[i], Apellido[i], Pais, Institucion)

            Lista_Persona = []
            Lista_Persona.append(Autor)

            topico = Topico()
            topico.Agregar_Topico(Caso)

            Aux = Articulo(Titulo[i], topico, Lista_Persona, Resumen, \
            EsAceptado)

            Lista_Art.append(Aux)

            Aux = Evaluacion(Lista_Art, Lista_CP)

        assert Aux.get_articulos() != None

        assert Aux.get_cp() != None

        Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", 5)

        Aux.Agregar_Evaluacion("MyArticulo", "josejulianprado@gmail.com", 3)
        Aux.Agregar_Evaluacion("MyArticulo", "API", 3)

        Aux.Generar_Promedios_Evaluacion()

        Ali = 0
        for i in Aux.get_articulos():
            if Ali == 0:
                assert i.get_promedio() == 3.67
            elif Ali == 1:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True

            elif Ali == 2:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True

            elif Ali == 3:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True
            Ali += 1

        Aux.Generar_Listas_Evaluacion(3)

        for i in sorted(Aux.get_aceptados()):
            # print  i.get_titulo(), i.get_promedio()
            assert i.get_titulo() == Titulo[0]
            assert i.get_promedio() == 3.67

        Ali = 1
        for i in sorted(Aux.get_empatados()):
            # print i.get_titulo(), i.get_promedio()
            assert i.get_titulo() == Titulo[Ali]
            assert i.get_promedio() == 3.44
            Ali += 1

        Aux.Generar_Listas_Evaluacion(4)

        Ali = 0
        for i in sorted(Aux.get_aceptados(), key=lambda Articulo:\
                        Articulo.get_promedio(), reverse=True):

            if Ali == 0:
                assert i.get_titulo() == Titulo[Ali]
                assert i.get_promedio() == 3.67
            else:
                assert i.get_titulo() == Titulo[Ali]
                assert i.get_promedio() == 3.44
            Ali += 1

        assert Aux.get_empatados() == []

        Aux.Generar_Listas_Evaluacion(2)

        for i in sorted(Aux.get_aceptados()):

            assert i.get_titulo() == Titulo[0]
            assert i.get_promedio() == 3.67

        Ali = 1
        for i in sorted(Aux.get_empatados()):
            assert i.get_titulo() == Titulo[Ali]
            assert i.get_promedio() == 3.44
            Ali += 1

    # pruebas de listas con errores
    def test_Lista_error(self):
        Nombre = ["Jose", "Jose1", "Jose2"]
        Apellido = ["Prado", "Prado1", "Prado2"]
        Pais = "Venezuela"
        Institucion = "USB"
        Correo = ["09-11006@usb.ve", "josejulianprado@gmail.com", "API"]
        topico = Topico()
        topico.Agregar_Topico("Computacion_1")
        topico.Agregar_Topico("Computacion_2")
        EsPresidente = ["S", "N", "N"]

        # Lista de CP
        Lista_CP = []
        for i in range(3):
            Aux = CP(Nombre[i], Apellido[i], Pais, Institucion, \
            Correo[i], topico, EsPresidente[i])
            Lista_CP.append(Aux)

        # Lista de Articulos
        Lista_Art = []

        Nombre = ["Luis", "Luis1", "Luis2", "Luis3"]
        Apellido = ["Rivera", "Rivera1", "Rivera2", "Rivera3"]
        Pais = "Venezuela"
        Institucion = "USB"
        Caso = "Computacion"

        Titulo = ["MyArticulo", "MyArticulo1", "MyArticulo2", "MyArticulo3"]
        Resumen = ["A", "B", "C", "D", "E"]
        EsAceptado = "S"

        for i in range(4):
            Autor = Persona(Nombre[i], Apellido[i], Pais, Institucion)

            Lista_Persona = []
            Lista_Persona.append(Autor)

            topico = Topico()
            topico.Agregar_Topico(Caso)

            Aux = Articulo(Titulo[i], topico, Lista_Persona, Resumen, \
            EsAceptado)

            Lista_Art.append(Aux)

            Aux = Evaluacion(Lista_Art, Lista_CP)

        assert Aux.get_articulos() != None

        assert Aux.get_cp() != None

        Aux.Agregar_Evaluacion("MyArticulo", "09-11006@usb.ve", 5)

        Aux.Agregar_Evaluacion("MyArticulo", "josejulianprado@gmail.com", 3)
        Aux.Agregar_Evaluacion("MyArticulo", "API", 3)

        Aux.Generar_Promedios_Evaluacion()

        Ali = 0
        for i in Aux.get_articulos():
            if Ali == 0:
                assert i.get_promedio() == 3.67
            elif Ali == 1:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True

            elif Ali == 2:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True

            elif Ali == 3:
                assert i.get_promedio() == -1.0
                assert i.set_promedio(3.44) == True
            Ali += 1

        Aux.Generar_Listas_Evaluacion(sys.maxint)

        assert Aux.get_aceptados() != []
        assert Aux.get_empatados() == []

        Aux.Reiniciar_Listas()
        Aux.Generar_Listas_Evaluacion("")

        assert Aux.get_aceptados() == []
        assert Aux.get_empatados() == []

        Aux.Reiniciar_Listas()
        Aux.Generar_Listas_Evaluacion(4.5)
        assert Aux.get_aceptados() == []
        assert Aux.get_empatados() == []


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
