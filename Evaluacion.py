# -*- coding: utf-8 -*-
'''
Created on 24/11/2013

@author: ubuntu
'''

import sys

from Articulo import Articulo
from CP import CP


class Evaluacion(object):
    '''
    classdocs
    '''

    # Constructor
    # articulosTodos: Lista de Articulos
    # miembrosCPTodos: Lista de Articulos
    def __init__(self, articulosTodos, miembrosCPTodos):
        if (articulosTodos != None) and (miembrosCPTodos != None):
            if(self.__Validar_Articulos(articulosTodos) and \
            self.__Validar_CP(miembrosCPTodos)):

                self.__articulos = articulosTodos
                self.__cp = miembrosCPTodos
                self.__evaluaciones = []
                self.__Aceptados = []
                self.__Empatados = []
        else:
            self.__articulos = None
            self.__cp = None
            self.__evaluaciones = None
            self.__Aceptados = None
            self.__Empatados = None

    # Retorna Articulos
    def get_articulos(self):
        return self.__articulos

    # Retorna CP
    def get_cp(self):
        return self.__cp

    # Devuelve la lista de articulos Aceptados
    def get_aceptados(self):
        return self.__Aceptados

    # Devuelve la lista de articulos Empatados
    def get_empatados(self):
        return self.__Empatados

    # devuelve la lista de evaluaciones
    def get_evaluaciones(self):
        return self.__evaluaciones

    # cambie el valor de evaluaciones con value
    def set_evaluaciones(self, value):
        self.__evaluaciones = value

    # Reinicia las listas de Empatados y Aceptados
    def Reiniciar_Listas(self):
        self.__Empatados = []
        self.__Aceptados = []

    # Agregar Nota
    def Agregar_Evaluacion(self, NombreArticulo, CorreoCP, Nota):
        # cheque que los atributos no sean nulos
        if (NombreArticulo != None) and (CorreoCP != None) and (Nota != None) \
        and (self.__articulos != None) and (self.__cp != None) and \
        (self.__evaluaciones != None):

            # chequeo que los tipos de datos sean correctos
            if (type(NombreArticulo) == str) and (type(CorreoCP) == str) and \
            (type(Nota) == int) and (1 <= Nota) and (Nota <= 5):

                # Elimino espacios antes del primer caracter
                # Elimino espacion despues del ultimo caracter
                NombreArticulo = NombreArticulo.strip()
                CorreoCP = CorreoCP.strip()
                # chequeo que exista el articulo
                # y si existe lo conservo en Art
                Esta1 = False
                Art = None
                for i in self.__articulos:
                    if NombreArticulo == i.get_titulo():
                        Esta1 = True
                        Art = i
                        break

                # cheque que la persona pertenesca al cp
                Esta2 = False
                for i in self.__cp:
                    # Si el articulo no esta
                    if not Esta1:
                        break

                    if CorreoCP == i.get_correo():
                        Esta2 = True
                        break

                # chqueo que no exista elementos en evaluacion
                if (len(self.__evaluaciones) == 0) and Esta1 and Esta2:
                    # aggrego a evaluaciones
                    self.__evaluaciones.append((NombreArticulo, CorreoCP, \
                    Nota))
                    # agrego la nota en articulo
                    Art.Agregar_Nota(Nota)
                    return True

                elif (len(self.__evaluaciones) > 0) and Esta1 and Esta2:
                    Esta3 = False
                    # busco si existe una evaluacion previa que involucre
                    # el mismo articulo y evaluador para ignorarlo
                    for i in self.__evaluaciones:
                        if (i[0] == NombreArticulo) and (i[1] == CorreoCP):
                            Esta3 = True
                            break

                    if not Esta3:
                        self.__evaluaciones.append((NombreArticulo, CorreoCP, \
                        Nota))
                        Art.Agregar_Nota(Nota)
                        return True
        return False

    # Generar Promedios
    def Generar_Promedios_Evaluacion(self):
        try:
            if (self.__articulos != None) and (self.__cp != None) and \
            (self.__evaluaciones != None):

                # Obtengo los articulos
                Aux = self.__articulos

                for i in Aux:
                    Contador = 0
                    Temp = i.get_Nota()

                    for j in Temp:
                        Contador += j

                    if len(Temp) > 0:
                        Valor = "%.2f" % (float(Contador) / float(len(Temp)))
                        i.set_promedio(float(Valor))
                    else:
                        i.set_promedio(float(-1))

        except(ZeroDivisionError):
            print "Se dividio entre cero"
            sys.exit()

        except(OverflowError):
            print "resultado demasiado grande para ser representado"
            sys.exit()

        except(FloatingPointError):
            print "Error en operecion punto flotante"
            sys.exit()

    # Genera la lista de aceptados y empatados
    def Generar_Listas_Evaluacion(self, numeroArticulo):
        try:
            if (self.__articulos != None) and (self.__cp != None) and \
            (self.__evaluaciones != None) and (numeroArticulo != None):

                if type(numeroArticulo) == int:

                    if numeroArticulo > 0 and numeroArticulo <= sys.maxint:
                        # Reinicio las variables
                        self.__Aceptados = []
                        self.__Empatados = []
                        # genero una lista con los promedios de los articulos
                        # >=3.00 y que tenga 2 o mas evaluaciones
                        ListaPromedioArticulo = [p.get_promedio() for p in \
                                                self.get_articulos() if \
                                                p.get_promedio() >= 3.00 \
                                                and len(p.get_Nota()) >= 2]
                        # lista auxiliar para aplicar el count
                        ListaAuxPromedios = ListaPromedioArticulo

                        # Variables donde guardo los indices
                        IndicesAceptados = []
                        IndicesEmpatados = 0.0

                        # variables auxiliares
                        UltimoIndiceVisto = 0.0
                        ElementosAgregadosEnAceptados = 0
                        # ordeno la lista de mayor a menor
                        for i in sorted(ListaPromedioArticulo, reverse=True):
                            if i != UltimoIndiceVisto:
                                Cantidad = ListaAuxPromedios.count(i)
                                if (Cantidad + ElementosAgregadosEnAceptados \
                                    <= numeroArticulo):
                                    if IndicesAceptados.count(i) == 0:
                                        IndicesAceptados.append(i)
                                        UltimoIndiceVisto = i
                                        ElementosAgregadosEnAceptados += \
                                        Cantidad
                                else:
                                    if (i > IndicesEmpatados):
                                        IndicesEmpatados = i

                        # genero la lista de aceptados
                        for i in sorted(IndicesAceptados, reverse=True):
                            self.__Aceptados.extend([p for p in self.\
                            get_articulos() if p.get_promedio() == i and \
                            len(p.get_Nota()) >= 2])

                        # genero lista de empatados
                        self.__Empatados.extend([p for p in self.\
                        get_articulos() if p.get_promedio() == \
                        IndicesEmpatados and len(p.get_Nota()) >= 2])

                        return True
                return False
            else:
                return False

        except(OverflowError):
            print "resultado demasiado grande para ser representado"
            sys.exit()

    # Imprime la Listas
    def Imprimir_Listas_Evaluacion(self):
        print "\n\n\t\tArticulos Aceptados"
        if (len(self.__Aceptados) > 0):
            for i in sorted(self.__Aceptados, key=lambda Articulo:\
                            Articulo.get_promedio(), reverse=True):
                print i.get_titulo(), "  ", i.get_promedio()
        else:
            print "Lista vacia\n"

        print "\n\n\t\tArticulos Empatados"
        if (len(self.__Empatados) > 0):

            for i in sorted(self.__Empatados, key=lambda Articulo:\
                            Articulo.get_promedio(), reverse=True):
                print i.get_titulo(), "  ", i.get_promedio()
            print "\n\n\n"
        else:
            print "Lista vacia\n"

    # Valido que los articulos vengan en una lista
    # y que todo el contenido de dicha lista sea un Articulo
    def __Validar_Articulos(self, articulo):
        if type(articulo) == list:
            for i in articulo:
                if isinstance(i, Articulo) != True:
                    return False
            return True
        return False

    # Valido que los CP vengan en una lista
    # y que todo el contenido de dicha lista sea un CP
    def __Validar_CP(self, cp):
        if type(cp) == list:
            for i in cp:
                if not isinstance(i, CP):
                    return False
            return True
        return False


if __name__ == '__main__':
    pass
