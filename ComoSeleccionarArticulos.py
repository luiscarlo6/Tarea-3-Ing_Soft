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
        for art in lista_articulo:
            if not isinstance(art, Articulo.Articulo):
                raise TypeError
        self.__lista_articulos = lista_articulo
        self.__num_articulos_aceptar = num_art_aceptar

    def get_lista_articulos(self):
        return self.__lista_articulos
    
    def get_num_articulos_aceptar(self):
        return self.__num_articulos_aceptar

    def seleccionararticulos(self):
        raise NotImplementedError("Excepcion, ComoSeleccionarArticulos se supone que es una interfaz")

class ArticuloTopico(ComoSeleccionarArticulos):
        
    __lista_topicos = []
        
    def __init__(self, lista_articulo, num_art_aceptar, lista_topicos):
        super(ArticuloTopico,self).__init__(lista_articulo, num_art_aceptar)
        self.__lista_topicos = lista_topicos
    
    def seleccionararticulos(self):
                
        matriz_topicos = []
        for topi in self.__lista_topicos:
            lista_articulos_por_topico = []
            for art in self.get_lista_articulos():
                for nombre_topico in art.getTopicos():
                    if nombre_topico == topi.get_nombre_topico():
                        lista_articulos_por_topico.append(art)
                        break
            matriz_topicos.append((topi,lista_articulos_por_topico))
        
        for i in matriz_topicos:
            print i[0]
            for j in i[1]:
                print j
                       
        lista_seleccionados = []
        for i in matriz_topicos:
            j=0
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
                    
if __name__=="__main__":
    
    cp1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True);
    cp2 = Persona.CP("a", "b", "usb", "venezuela", ["Base"], True);
    cp3 = Persona.CP("a", "b", "usb", "venezuela", ["Computacion"], True);
    
    a1 = Articulo.Articulo("Titulo1", ["pal1", "pal2"], ["Base", "Redes"], [(cp1,3) , (cp2, 4), (cp3, 5)])
    a2 = Articulo.Articulo("Titulo2", ["pal1", "pal2"], ["Base", "Redes"], [(cp1,4) , (cp2, 4), (cp3, 4)])
    a3 = Articulo.Articulo("Titulo3", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [(cp1,3) , (cp2, 3), (cp3, 3)])
    
    topicos = Topico.Topico("Base")
    topi1 = Topico.Topico("Redes")
    topi2 = Topico.Topico("Computacion")

    
    estrategia1 = ArticuloTopico([a1,a2,a3], 2, [topicos,topi1,topi2])
    estrategia1.seleccionararticulos()
    
    
    