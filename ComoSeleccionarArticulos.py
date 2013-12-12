import Articulo
import Topico
import Persona

class ComoSeleccionarArticulos(object):
    
    __lista_articulos = []
    __num_articulos_aceptar = None
    
    def __init__(self, lista_articulo, num_art_aceptar):
        if not isinstance(lista_articulo, list):
            raise TypeError
        if not isinstance(num_art_aceptar, int):
            raise TypeError
        if num_art_aceptar <= 0:
            raise ValueError
        for art in lista_articulo:
            if not isinstance(art, Articulo.Articulo):
                raise TypeError
        self.__lista_articulos = lista_articulo
        self.__num_articulos_aceptar = num_art_aceptar

    def get_lista_articulos(self):
        return self.__lista_articulos
    
    def set_lista_articulos(self, value):
        self.__lista_articulos = value
    
    
    def get_num_articulos_aceptar(self):
        return self.__num_articulos_aceptar

    def seleccionar_articulos(self):
        raise NotImplementedError("Excepcion, ComoSeleccionarArticulos se supone que es una interfaz")

class ArticuloTopico(ComoSeleccionarArticulos):
        
    __lista_topicos = []
        
    def __init__(self, lista_articulo, num_art_aceptar, lista_topicos):
        super(ArticuloTopico, self).__init__(lista_articulo, num_art_aceptar)
        self.__lista_topicos = lista_topicos
    
    def seleccionar_articulos(self):
                
        matriz_topicos = []
        for topi in self.__lista_topicos:
            lista_articulos_por_topico = []
            for art in self.get_lista_articulos():
                for nombre_topico in art.getTopicos():
                    if nombre_topico == topi.get_nombre_topico():
                        lista_articulos_por_topico.append(art)
                        break
            matriz_topicos.append((topi, lista_articulos_por_topico))
        
        for i in matriz_topicos:
            print i[0]
            for j in i[1]:
                print j
                       
        lista_seleccionados = []
        for i in matriz_topicos:
            j = 0
            while j < len(i[1]): 
                aux = i[1][j]
                if aux in lista_seleccionados:
                    i[1].remove(aux)
                else:   
                    lista_seleccionados.append(aux)
                    if len(lista_seleccionados) == self.get_num_articulos_aceptar():
                        break
                    
                    i[1].remove(aux)
                    break
            if len(lista_seleccionados) == self.get_num_articulos_aceptar():
                break
                
                
        print "Ya pase"
        for i in lista_seleccionados:
            print i
                    
    
class ArticuloDesempate(ComoSeleccionarArticulos):
        
    def __init__(self, lista_articulo, num_art_aceptar):
        super(ArticuloDesempate, self).__init__(lista_articulo, num_art_aceptar)
    
    def seleccionar_articulos(self):
        lista_aceptados = []
        lista_empatados = []
        if len(self.get_lista_articulos()) <= self.get_num_articulos_aceptar():
            lista_aceptados = self.get_lista_articulos()
        
        else:
            self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                   key=lambda x: x.calcularPromedio(),
                                   reverse=True))
        
            primeros_n = self.get_lista_articulos()[0 : self.get_num_articulos_aceptar()]
        
            min_promedio = min([ar.calcularPromedio() for ar in primeros_n])
            empatados = [ar for ar in self.get_lista_articulos() if ar.calcularPromedio() == min_promedio]
            if len(empatados) > 1:
                lista_empatados = empatados
                lista_aceptados = [ar for ar in primeros_n if ar.calcularPromedio() > min_promedio]
                while True:
                    i = 0
                    for art in lista_empatados:
                        print "%s.- %s " % (i, art)
                        i += 1
                    try:
                        print "Articulos Restantes: ", (self.get_num_articulos_aceptar()-len(lista_aceptados))
                        opcion = input("Elija el articulo que desee aceptar: ")
                        articulo_elegido = lista_empatados[opcion]
                        lista_aceptados.append(articulo_elegido)
                        lista_empatados.remove(articulo_elegido)
                        if len(lista_aceptados) == self.get_num_articulos_aceptar():
                            break
                    except:
                        print "Opcion no valida"
                        continue
                
            
            else:
                lista_aceptados = primeros_n
                lista_empatados = []
                
        print 'Lista Aceptados'
        for art in lista_aceptados:
            print ".-%s " % (art)

            
if __name__ == "__main__":
    
    cp1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True);
    cp2 = Persona.CP("a", "b", "usb", "venezuela", ["Base"], True);
    cp3 = Persona.CP("a", "b", "usb", "venezuela", ["Computacion"], True);
    
    a1 = Articulo.Articulo("Titulo1", ["pal1", "pal2"], ["Base", "Redes"], [(cp1, 5) , (cp2, 3), (cp3, 5)])
    a2 = Articulo.Articulo("Titulo2", ["pal1", "pal2"], ["Base", "Redes"], [(cp1, 4) , (cp2, 4), (cp3, 4)])
    a3 = Articulo.Articulo("Titulo3", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [(cp1, 3) , (cp2, 3), (cp3, 5)])
    a4 = Articulo.Articulo("Titulo4", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [(cp1, 3) , (cp2, 3), (cp3, 5)])
    a5 = Articulo.Articulo("Titulo5", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [(cp1, 3) , (cp2, 3), (cp3, 5)])
    
    topicos = Topico.Topico("Base")
    topi1 = Topico.Topico("Redes")
    topi2 = Topico.Topico("Computacion")

    
    estrategia1 = ArticuloDesempate([a1, a2, a3,a4,a5], 4)
    estrategia1.seleccionar_articulos()
