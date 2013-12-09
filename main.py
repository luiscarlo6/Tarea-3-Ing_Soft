#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''

import sys

from Articulo import Articulo
from CP import CP
from Evaluacion import Evaluacion
from Persona import Persona
from Topico import Topico


# variables globales
Lista_Articulos = []
Lista_Persona = []
evaluaciones = None


# Procedimiento que muestra el menu
def __Menu():
    print "\n\n"
    print "1) Crear Articulos"
    print "2) Crear Miembros del comite de programa y su presidente"
    print "3) Cargar Evaluaciones de los Articulos"
    print "4) Mostrar Listas de Aceptados y Empatados"
    print "5) Salir del sitema"


# Funcion que solicita un string por la entrada estandar
def __Solicitar_Parametro(Mensaje):
    Aux = None
    while True:
        Aux = raw_input("Por favor ingrese el" + Mensaje + ": \t")
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if len(Aux) != 0:
            return Aux
        else:
            print "Valor invalido, vuelva a intentarlo\n"


# funcion que solicita un numero por la entrada estandar
def __Solicitar_Numero(Mensaje):
    Aux = None
    while True:
        Aux = raw_input("Por favor ingrese el" + Mensaje + ": \t")
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if len(Aux) != 0 and Aux.isdigit():
            return int(Aux)
        else:
            print "Valor invalido, vuelva a intentarlo\n"


# funcion que retorna 1 si el usuario desea continuar con la opcion
# seleccianada  y 0 en caso contrario
def __Seleccion(Mensaje):
    Aux = None
    while True:
        Aux = raw_input("Selecione 1 para agregar " + Mensaje + \
                        " o 0 para seguir:\t")
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if Aux == "1" or Aux == "0":
            return Aux
        else:
            "seleccion invalida, vuelva a intentarlo"


# funcion que retorna 1 si el usuario desea que una persona sea presidente del
# CP y 0 en caso contrario
def __Seleccion_1():
    Aux = None
    while True:
        Mensaje = "Selecione 1 si esta Persona es el presidente del CP "
        Mensaje += "o 0 para seguir:\t"
        Aux = raw_input(Mensaje)
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if Aux == "1" or Aux == "0":
            return Aux
        else:
            "seleccion invalida, vuelva a intentarlo"


# funcion que solicita los topicos por la entrada estandar
def __Solicitar_Topicos():
    Aux = None
    topico = Topico()
    while True:
        Aux = raw_input("Por favor ingrese el nombre del topico: \t")
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if len(Aux) != 0:
            Temp = topico.Agregar_Topico(Aux)
            if Temp:
                print "Topico agregado"
            else:
                print "Topico no agregado"
        if topico.Cantidad_Topico() != 0:
            Temp = __Seleccion(" Topico")
            if (Temp == "0"):
                break
        else:
            print "Valor invalido, vuelva a intentarlo\n"
    return topico


# funcion que solicita los autores por la entrada estandar
def __Solicitar_Autores():
    Autor = None
    Lista_Autores = []
    while True:
            Nombre = __Solicitar_Parametro(" Nombre del Autor")
            Apellido = __Solicitar_Parametro(" Apellido del Autor")
            Pais = __Solicitar_Parametro(" Pais del Autor")
            Institucion = __Solicitar_Parametro(" Institucion del Autor")
            Autor = Persona(Nombre, Apellido, Pais, Institucion)
            Lista_Autores.append(Autor)
            print "Autor agregado exitosamente"
            if len(Lista_Autores) != 0:
                Temp = __Seleccion(" Autor")
                if (Temp == "0"):
                    break
    return Lista_Autores


# funcion que solicita el resumen por la entrada estandar
def __Solicitar_Resumen():
    Contador = 1
    Resumen = []
    while True and (Contador < 6):
        Aux = raw_input("Ingrese la palabra clave" + str(Contador) + \
                        " del Resumen del Articulo\t")
        Aux = Aux.strip()
        Aux = Aux.capitalize()
        if len(Aux) != 0:
            if Resumen.count(Aux) == 0:
                Resumen.append(Aux)
                Contador += 1
                print "Palabra clave Agregada"
                if (Contador == 6):
                    break
            else:
                print "Palabra ya existente, palabra no valida"

            if (__Seleccion(" Resumen") == "0") and 1 <= len(Resumen) \
            and len(Resumen) <= 5:
                break
        else:
            print "Valor invalido, vuelva a intentarlo\n"
    return Resumen


# Funcion que retorna true si hay una ocurrencia de la clave
def __Existe_Persona_CP(Correo, ListaCP):
    Esta = False
    for i in ListaCP:
        if (Correo == i.get_correo()):
            Esta = True
            break
    return Esta


# Funcion que retorna true si el articulo existe
def __Existe_Articulo(NombreArt, ListaArt):
    Esta = False
    for i in ListaArt:
        if (NombreArt == i.get_titulo()):
            Esta = True
            break
    return Esta


# Opcion 1 del menu
def __Opcion_1(Lista_Aux):
    while True:
        Titulo = __Solicitar_Parametro(" Titulo del Articulo")
        topicos = __Solicitar_Topicos()
        Autores = __Solicitar_Autores()
        Resumen = __Solicitar_Resumen()

        if not __Existe_Articulo(Titulo, Lista_Aux):
            articulo = Articulo(Titulo, topicos, Autores, Resumen, "N")
            Lista_Aux.append(articulo)
            print "El articulo fue agregado de manera exitosa"
        else:
            print "El articulo ya existe"

        if(__Seleccion(" otro articulo a la lista ") == "0"):
            break
    return Lista_Aux


# Opcion 2 del menu
def __Opcion_2(Lista_aux, Control):
    while True:
        Nombre = __Solicitar_Parametro(" Nombre")
        Apellido = __Solicitar_Parametro(" Apellido")
        Pais = __Solicitar_Parametro(" Pais")
        Institucion = __Solicitar_Parametro(" Institucion")
        Correo = __Solicitar_Parametro(" Correo")
        topico = __Solicitar_Topicos()

        if not __Existe_Persona_CP(Correo, Lista_aux):
            if (not Control):
                if (__Seleccion_1() == "1"):
                    EsPresidente = "S"
                    Control = True
                else:
                    EsPresidente = "N"
            else:
                EsPresidente = "N"

            cp = CP(Nombre, Apellido, Pais, Institucion, Correo, topico, \
                    EsPresidente)
            Lista_aux.append(cp)
            print "Persona agregada al CP"
        else:
            print "Miembro del CP ya exists"

        Temp = __Seleccion(" Miembros CP")

        if(Temp == "0")  and Control:
            break

        if (Temp == "0")  and not Control:
            print "No existe presidente del CP."
            print "Debe agregar una persona que sea presidente para",
            print "regresar al menu principal"
    # print "Antes del return", Control
    return Lista_aux, Control


# Opcion 3 del menu
def __Opcion_3(evaluaciones):
    Alicia = None
    if (evaluaciones != None):
        Alicia = evaluaciones.get_evaluaciones()

    Variable_evaluaciones = Evaluacion(Lista_Articulos, Lista_Persona)

    if Alicia != None:
        Variable_evaluaciones.set_evaluaciones(Alicia)
    while True:
        CorreoCP = __Solicitar_Parametro(" Correo del Evaluador")
        NombreArt = __Solicitar_Parametro(" Nombre del Articulo")
        NotaArticulo = __Solicitar_Numero(" Puntuacion dada")
        Aux = Variable_evaluaciones.Agregar_Evaluacion(NombreArt, CorreoCP, \
                                                       NotaArticulo)
        if Aux:
            print "Evaluacion agregada"
        else:
            print "Evaluacion no agregada"

        if(__Seleccion(" otra evaluacion a la lista") == "0"):
            break

    return Variable_evaluaciones


# Opcion 4 del menu
def __Opcion_4():
    numeroArticulo = __Solicitar_Numero(" Articulos a escoger")
    evaluaciones.Generar_Promedios_Evaluacion()
    evaluaciones.Reiniciar_Listas()
    evaluaciones.Generar_Listas_Evaluacion(numeroArticulo)
    evaluaciones.Imprimir_Listas_Evaluacion()


# Programa principal
if __name__ == '__main__':

    # chequeo que el archivo sea llamado de forma correcta
    if len(sys.argv) == 1:
        Control_1 = False
        Control_2 = False
        Control_3 = False
        HayPresidente = False
        print "\t\t\t Bienvenidos a la aplicacion"
        while True:
            __Menu()
            Opcion = raw_input("\nIngrese una opcion\t")
            Opcion = Opcion.strip()
            Opcion = Opcion.capitalize()

            if (Opcion == "1"):
                    Lista_Articulos = __Opcion_1(Lista_Articulos)
                    Control_1 = True

            elif (Opcion == "2"):
                    Lista_Persona, HayPresidente = __Opcion_2(Lista_Persona, \
                                                              HayPresidente)
                    Control_2 = True

            elif (Opcion == "3"):
                if (Control_1 and Control_2):
                    evaluaciones = __Opcion_3(evaluaciones)
                    Control_3 = True
                else:
                    print "No se puede cargar evaluaciones hasta que ",
                    print "hallan cargado los articulos y miembros del CP"

            elif (Opcion == "4"):
                if Control_3:
                    __Opcion_4()
                else:
                    print "No se puede generar las listas hasta que se ",
                    print "hallan cargado los articulos, miembros del CP",
                    print " y las evaluaciones"

            elif (Opcion == "5"):
                break
            else:
                print "\n\nValor invalido vuelva a intentarlo\n\n"
        print "\n\t\tGracias por usar la aplicacion"

    else:
        print "Error: El programa fue mal invocado"
        print "Formato : python Main.py"

    sys.exit()
