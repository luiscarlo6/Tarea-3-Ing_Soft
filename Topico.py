# -*- coding: utf-8 -*-
'''
Created on 23/11/2013

@author: ubuntu
'''


class Topico(object):
    '''
    Clase que contiene el nombre de los topicos
    '''

    # Costructor
    def __init__(self):
        self.__Topico = []

    # Agrego un nuevo topico
    def Agregar_Topico(self, NombreTopico):

        if  self.__Validar_Topico(NombreTopico):
            # Elimino los espacios en blanco a la derecha
            # e izquierda de la palabra
            NombreTopico = NombreTopico.strip()

            # Caso Vacio
            if len(NombreTopico) == 0:
                return False
            # Caso General
            else:
                if self.__Topico.count(NombreTopico) == 0:
                    self.__Topico.append(NombreTopico)
                    return True
                else:
                    return False
        return False

    # Elimina un Topico
    def Eliminar_Topico(self, NombreTopico):

        if  self.__Validar_Topico(NombreTopico):
            # Elimino los espacios en blanco a la derecha
            # e izquierda de la palabra
            NombreTopico = NombreTopico.strip()

            if self.__Topico.count(NombreTopico) > 0:
                self.__Topico.remove(NombreTopico)
                return True
        return False

    # Listar Topicos
    def Listar_Topico(self):
        return sorted(self.__Topico)

    # Retorna la cantidad total de topicos
    def Cantidad_Topico(self):
        return len(self.__Topico)

    # Valida que el topico sea un Strig y diferente de None
    def __Validar_Topico(self, NombreTopico):

        if  type(NombreTopico) == str and NombreTopico != None:
            return True
        return False

if __name__ == '__main__':
    pass
