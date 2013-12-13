import Persona

class Articulo(object):
    
    __titulo = None
    __resumen = []
    __topicos = []
    __autores = []
    __status = None
    
    # Puntuaciones es una lista de duplas, donde la primera posicion
    # de cada dupla es un objeto CP(el arbitro que hizo la evaluacion)
    # y la segunda posicion corresponde a la nota que dio dicho arbitro
    __puntuaciones = []
    
    def __init__(self, tit, res, topicos, autores, pun):
        if (isinstance(tit, str) and isinstance(res, list) and 
            isinstance(topicos, list) and isinstance(pun, list)
            and isinstance(autores, list)):
        
            for r in res:
                if not isinstance(r, str):
                    raise TypeError
                
            for t in topicos:
                if not isinstance(t, str):
                    raise TypeError
            
            for a in autores:  
                if not isinstance(a, Persona.Autor):
                    raise TypeError
            
            for p in pun:
                if not isinstance(p[0], Persona.CP):
                    raise TypeError
                if not isinstance(p[1], int):
                    raise TypeError
                
            
            if len(tit) > 0 and len(res) > 0:
                self.__titulo = tit
                self.__resumen = res
                self.__topicos = topicos
                self.__autores = autores
                self.__puntuaciones = pun
            else:
                raise ValueError
        else:
            raise TypeError

    def getTitulo(self):
        return self.__titulo


    def getResumen(self):
        return self.__resumen
    
    
    def get_topicos(self):
        return self.__topicos
    
    def get_autores(self):
        return self.__autores


    def getPuntuaciones(self):
        return self.__puntuaciones
    
    def get_status(self):
        return self.__status


    def setTitulo(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__titulo = value


    def setResumen(self, value):
        if len(value) not in range(1,6):
            raise ValueError
        self.__resumen = value
        
    def set_topicos(self, value):
        self.__topicos = value
        
    def set_autores(self, value):
        self.__autores = value

    def setPuntuaciones(self, value):
        self.__puntuaciones = value
        
    def agregarPuntuacion(self, value):
        if not isinstance(value[0], Persona.CP):
            raise ValueError
        if not isinstance(value[1], int):
            raise ValueError
        if value[1] not in range(1,6):
            raise ValueError
        self.__puntuaciones.append(value)
        
    def set_status(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__titulo = value
        
    def calcularPromedio(self):
        try:
            promedio = float(sum([punto[1] for punto in self.getPuntuaciones()]) / float(len(self.getPuntuaciones())))
        except ZeroDivisionError:
            return 0
        else:
            return promedio
        
    def es_aceptable(self):
        return len(self.getPuntuaciones()) > 1 and self.calcularPromedio() >= 3
    
    def __str__(self):
        return self.__titulo
    
    
        
