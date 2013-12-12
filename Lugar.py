'''
Created on 08/12/2013

@author: admin
'''

class Lugar(object):
    _nombre = None;
    _ubicacion = None;
    _capacidad = 0;


    def __init__(self, nombre, ubicacion, capacidad):
        
        if(isinstance( nombre, str) and isinstance( ubicacion, str) and
           isinstance( capacidad, int)):
        
            if(len(nombre) > 0 and len(ubicacion) > 0 and
               capacidad > 0):
                
                self._nombre = nombre;
                self._ubicacion = ubicacion;
                self._capacidad = capacidad;
                
            else:
                raise ValueError
        else:
            raise ValueError
        
    def getNombre(self):
        return self._nombre;
    
    def getUbicacion(self):
        return self._ubicacion;
    
    def getCapacidad(self):
        return self._capacidad;
    
    def setNombre(self, value):
        if not isinstance(value, str):
            raise TypeError("Nombre debe ser un string")
        if len(value) == 0:
            raise ValueError("Nombre no puede ser vacio")
        self._nombre = value
        
    def setUbicacion(self, value):
        if not isinstance(value, str):
            raise TypeError("Ubicacion debe ser un string")
        if len(value) == 0:
            raise ValueError("Ubicacion no puede ser vacio")
        self._ubicacion = value
        
    def setCapacidad(self, value):
        if not isinstance(value, int):
            raise TypeError("Capacidad debe ser un entero")
        if 0 >= value:
            raise ValueError("Capacidad no puede ser menor o igual a cero")
        self._capacidad = value