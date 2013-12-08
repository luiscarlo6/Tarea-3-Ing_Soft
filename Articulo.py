# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''
from Persona import Persona
from Topico import Topico


class Articulo(object):
    '''
    classdocs
    '''

    # CONSTRUCTOR

    def __init__(self, Titulo, topico, Autor, Resumen, EsAceptado):
        # Atributos diferentes de null
        if (Titulo != None) and (topico != None) and (Autor != None) and \
        (Resumen != None) and (EsAceptado != None):

            if (type(Titulo) == str) and isinstance(topico, Topico) and \
            self.__Validar_Autor(Autor) and self.__Validar_Resumen(Resumen) \
            and (type(EsAceptado) == str) and ((EsAceptado == "S") or \
            (EsAceptado == "N")):

                Titulo = Titulo.strip()

                if (len(Titulo) > 0):
                    self.__Titulo = Titulo
                    self.__topico = topico
                    self.__Autor = Autor
                    self.__Resumen = Resumen
                    if EsAceptado == "S":
                        self.__EsAceptado = True
                    elif EsAceptado == "N":
                        self.__EsAceptado = False

                    self.__Promedio = 0.0
                    self.__Notas = []
                else:
                    self.__Inicializar_None()
            else:
                self.__Inicializar_None()
        else:
            self.__Inicializar_None()

    # Inicializa las variables en none
    def __Inicializar_None(self):
        self.__Titulo = None
        self.__topico = None
        self.__Autor = None
        self.__Resumen = None
        self.__EsAceptado = None
        self.__Promedio = None
        self.__Notas = None

    # Retorna el titulo del articulo
    def get_titulo(self):
        return self.__Titulo

    # Retorna los Topicos que trata el articulo
    def get_topico(self):
        return self.__topico

    # Retorna la lista de Autores del articulo
    def get_autor(self):
        return self.__Autor

    # Retorna el resumen del articulo
    def get_resumen(self):
        return self.__Resumen

    # Retorna si el articulo es aceptado o no
    def get_es_aceptado(self):
        return self.__EsAceptado

    # retorna promedio
    def get_promedio(self):
        return self.__Promedio

    # retorna Nota
    def get_Nota(self):
        return self.__Notas

    # Modifica el titulo
    def set_titulo(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0:
                self.__Titulo = value
                return True
        return False

    # modifica los topicos
    def set_topico(self, value):
        if isinstance(value, Topico):
            if value.Cantidad_Topico() != 0:
                self.__topico = value
                return True
        return False

    # Modifica los autores
    def set_autor(self, value):
        if self.__Validar_Autor(value):
            self.__Autor = value
            return True
        return False

    # Modifica resumen
    def set_resumen(self, value):
        if (self.__Validar_Resumen(value)):
            self.__Resumen = value
            return True
        return False

    # Modifica promedio
    def set_promedio(self, value):
        if type(value) == float:
            self.__Promedio = value
            return True
        return False

    def Agregar_Nota(self, value):
        if type(value) == int:
            if (1 <= value) and (value <= 5):
                self.__Notas.append(value)
                return True
        return False

    # Modifica EsAceptado
    def set_es_aceptado(self, value):
        if type(value) == str:
            value = value.strip()
            if len(value) != 0 and ((value == "S") or (value == "N")):
                if value == "S":
                    self.__EsAceptado = True
                    return True
                elif value == "N":
                    self.__EsAceptado = False
                    return True
        return False

    # Funcion que alida la correctitud del autor
    def __Validar_Autor(self, Autor):
        if type(Autor) == list:
            k = 0
            for i in Autor:
                if isinstance(i, Persona):
                    k += 1
            if k > 0:
                return True
        return False

    # Funcion que verifica que el resumen conste de 5 palabras
    def __Validar_Resumen(self, Resumen):
        if type(Resumen) == list:
            for k in Resumen:
                if type(k) != str:
                    return False
            if 1 <= len(Resumen) and len(Resumen) <= 5:
                return True
        return False


if __name__ == '__main__':
    pass
