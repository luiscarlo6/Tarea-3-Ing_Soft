'''
Created on 14/12/2013

@author: ubuntu
'''


class TipoDeInscripcion(object):
    '''
    classdocs
    '''
    def get_precio(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def set_precio(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def get_beneficios(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def set_beneficios(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def get_eventos_asistir(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def set_eventos_asistir(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")

    def __str__(self):
        raise NotImplementedError("Excepcion, TipoDeInscripcion")


class AsistenciaExclusivaCharlas(TipoDeInscripcion):
    __NOMBRE = "Asistencia Exclusiva a Charlas\n"
    __precio = None
    __beneficios = None
    __eventos_asistir = None

    def __init__(self, precio, beneficios, eventos):
        if isinstance(precio, float) and isinstance(beneficios, list) and \
        isinstance(eventos, list):

            for i in beneficios:
                if not isinstance(i, str):
                    raise TypeError

            for i in eventos:
                if not isinstance(i, str):
                    raise TypeError

            self.__precio = precio
            self.__beneficios = beneficios
            self.__eventos_asistir = eventos
        else:
            raise TypeError

    def get_precio(self):
        return self.__precio

    def get_beneficios(self):
        return self.__beneficios

    def get_eventos_asistir(self):
        return self.__eventos_asistir

    def set_precio(self, value):
        if isinstance(value, float):
            self.__precio = value
        else:
            raise TypeError

    def set_beneficios(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
            self.__beneficios = value
        else:
            raise TypeError

    def set_eventos_asistir(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
                self.__eventos_asistir = value
        else:
            raise TypeError

    def __str__(self):
        Cadena = self.__NOMBRE
        Cadena += str(self.get_precio()) + "\n"
        Cadena += str(self.get_beneficios()) + "\n"
        Cadena += str(self.get_eventos_asistir()) + "\n"
        return Cadena


class AsistenciaExclusivaTalleres(TipoDeInscripcion):
    __NOMBRE = "Asistencia Exclusiva a Talleres\n"
    __precio = None
    __beneficios = None
    __eventos_asistir = None

    def __init__(self, precio, beneficios, eventos):
        if isinstance(precio, float) and isinstance(beneficios, list) and \
        isinstance(eventos, list):

            for i in beneficios:
                if not isinstance(i, str):
                    raise TypeError

            for i in eventos:
                if not isinstance(i, str):
                    raise TypeError

            self.__precio = precio
            self.__beneficios = beneficios
            self.__eventos_asistir = eventos
        else:
            raise TypeError

    def get_precio(self):
        return self.__precio

    def get_beneficios(self):
        return self.__beneficios

    def get_eventos_asistir(self):
        return self.__eventos_asistir

    def set_precio(self, value):
        if isinstance(value, float):
            self.__precio = value
        else:
            raise TypeError

    def set_beneficios(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
            self.__beneficios = value
        else:
            raise TypeError

    def set_eventos_asistir(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
                self.__eventos_asistir = value
        else:
            raise TypeError

    def __str__(self):
        Cadena = self.__NOMBRE
        Cadena += str(self.get_precio()) + "\n"
        Cadena += str(self.get_beneficios()) + "\n"
        Cadena += str(self.get_eventos_asistir()) + "\n"
        return Cadena


class AsistenciaCharlasYTalleres(TipoDeInscripcion):
    __NOMBRE = "Asistencia a Charlar y Talleres\n"
    __precio = None
    __beneficios = None
    __eventos_asistir = None

    def __init__(self, precio, beneficios, eventos):
        if isinstance(precio, float) and isinstance(beneficios, list) and \
        isinstance(eventos, list):

            for i in beneficios:
                if not isinstance(i, str):
                    raise TypeError

            for i in eventos:
                if not isinstance(i, str):
                    raise TypeError

            self.__precio = precio
            self.__beneficios = beneficios
            self.__eventos_asistir = eventos
        else:
            raise TypeError

    def get_precio(self):
        return self.__precio

    def get_beneficios(self):
        return self.__beneficios

    def get_eventos_asistir(self):
        return self.__eventos_asistir

    def set_precio(self, value):
        if isinstance(value, float):
            self.__precio = value
        else:
            raise TypeError

    def set_beneficios(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
            self.__beneficios = value
        else:
            raise TypeError

    def set_eventos_asistir(self, value):
        if isinstance(value, list):
            for i in value:
                if not isinstance(i, str):
                    raise TypeError
                self.__eventos_asistir = value
        else:
            raise TypeError

    def __str__(self):
        Cadena = self.__NOMBRE
        Cadena += str(self.get_precio()) + "\n"
        Cadena += str(self.get_beneficios()) + "\n"
        Cadena += str(self.get_eventos_asistir()) + "\n"
        return Cadena


if __name__ == "__main__":

    A = AsistenciaCharlasYTalleres(150, ["Lujo"], ["Talleres"])
    print A, isinstance(A, TipoDeInscripcion)
