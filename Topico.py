

class Topico(object):
    
    __nombre_topico = None

    
    def __init__(self, nombre_topico):
        if isinstance(nombre_topico, str):
            self.__nombre_topico = nombre_topico
        else:
            raise ValueError


    def get_nombre_topico(self):
        return self.__nombre_topico

    def __str__(self):
        return self.__nombre_topico

    def set_nombre_topico(self, value):
        self.__nombre_topico = value

    def comparar_topico(self, valor):
        if self.__nombre_topico == valor:
            return True
        else:
            return False