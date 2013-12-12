class Persona(object):
    __nombre = None
    __apellido = None
    __institucion = None
    __topicos = None
    __pais = None
    
    def __init__(self, nombre, apellido, institucion, pais, topicos):
        
        
        if (isinstance(nombre, str) and isinstance(apellido, str) and 
            isinstance(institucion, str) and isinstance(pais, str) and 
            isinstance(topicos, list)):
        
            if((len(nombre) > 0) and (len(apellido) > 0) and
               (len(institucion) > 0) and (len(pais) > 0) ):
            
                self.__nombre = nombre
                self.__apellido = apellido
                self.__institucion = institucion
                self.__topicos = topicos
                self.__pais = pais
            else:
                raise ValueError
        else:
            raise ValueError

    def getNombre(self):
        return self.__nombre


    def getApellido(self):
        return self.__apellido


    def getInstitucion(self):
        return self.__institucion

    def getTopicos(self):
        return self.__topicos



    def getPais(self):
        return self.__pais


    def setNombre(self, value):
        if not isinstance(value, str):
            raise TypeError("nombre must be set to an string")
        if len(value) == 0:
            raise ValueError("nombre must not be empty")
        self.__nombre = value


    def setApellido(self, value):
        if not isinstance(value, str):
            raise TypeError("apellido must be set to an integer")
        if len(value) == 0:
            raise ValueError("apellido must not be empty")
        self.__apellido = value


    def setInstitucion(self, value):
        if not isinstance(value, str):
            raise TypeError("institucion must be set to an integer")
        if len(value) == 0:
            raise ValueError("institucion must not be empty")
        self.__institucion = value
        
    def setTopicos(self, value):
        if not isinstance(value, list):
            raise TypeError("nombre must be set to an list")
        if len(value) == 0:
            raise ValueError("nombre must not be empty")
        self.__topicos = value


    def setPais(self, value):
        if not isinstance(value, str):
            raise TypeError("pais must be set to an integer")
        if len(value) == 0:
            raise ValueError("pais must not be empty")
        self.__pais = value
        
        
    def __str__(self):
        return "%s %s" % (self.getNombre(), self.getApellido())
    
class CP(Persona):
    __es_presidente = None
    
    def __init__(self, nom, ape, ins, pai, topicos, es_pre):
        super(CP, self).__init__(nom, ape, ins, pai, topicos)
        if not isinstance(es_pre, bool):
            raise TypeError
        else:
            self.es_presidente = es_pre
            
    def getEsPresidente(self):
        return self.es_presidente
    
    def setEsPresidente(self, value):
        if not isinstance(value, bool):
            raise TypeError
        else:
            self.es_presidente = value
            