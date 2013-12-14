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
        
        '''for i in matriz_topicos:
            print i[0]
            for j in i[1]:
                print j'''
                       
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
            
class ArticuloPaisesDesempate(ComoSeleccionarArticulos):
    
    def __init__(self, lista_articulo, num_art_aceptar, lista_paises, p):
        super(ArticuloPaisesDesempate, self).__init__(lista_articulo, num_art_aceptar)
        if not isinstance(p, int):
            raise TypeError
        if p < 0:
            raise ValueError
        if not isinstance(lista_paises, list):
            raise TypeError
        for pais in lista_paises:
            if not isinstance(pais, str):
                raise TypeError
        self.__p = p
        self.__lista_paises = lista_paises
        
    def seleccionar_articulos(self):
        lista_seleccionados = []
        # Seleccionamos los p mejores articulos de cada pais 
        for pais in self.__lista_paises:
            lista_articulo_del_pais = [art for art in self.get_lista_articulos() if art.pertenece_a_pais(pais)]  
            lista_articulo_del_pais = sorted(lista_articulo_del_pais,
                                              key = lambda x: x.calcularPromedio() )
            for i in range(0, self.__p):
                articulo_agregar = lista_articulo_del_pais.pop()
                lista_seleccionados.append(articulo_agregar)
                self.get_lista_articulos().remove(articulo_agregar)
                
        # Eliminamos articulos repetidos
        list(set(lista_seleccionados))
        
        
        if len(lista_seleccionados) >= self.get_num_articulos_aceptar():
            lista_seleccionados = lista_seleccionados[0 : self.get_num_articulos_aceptar()]
        # Si quedan aun articulos por elegir, los elegimos por mejor promedio    
        else:
            num_articulos_por_elegir = self.get_num_articulos_aceptar() - len(lista_seleccionados) 
            
            
            # Si el numero de articulos que quedan es menor al numero de articulos por elegir
            # entonces acetamos a todos los articulos que quedan
            if len(self.get_lista_articulos()) <= num_articulos_por_elegir:
                lista_seleccionados += self.get_lista_articulos()
        
            else:
                self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                                key=lambda x: x.calcularPromedio(),
                                                reverse=True))
        
                primeros_n = self.get_lista_articulos()[0 : num_articulos_por_elegir]
               
                min_promedio = min([ar.calcularPromedio() for ar in primeros_n])
                lista_restantes_aceptados = [ar for ar in primeros_n if ar.calcularPromedio() > min_promedio]
                lista_restantes_empatados = [ar for ar in self.get_lista_articulos() if ar.calcularPromedio() == min_promedio]
                if len(lista_restantes_empatados) > 1:
                    
                    lista_seleccionados += lista_restantes_aceptados
                    num_articulos_por_elegir -= len(lista_restantes_aceptados)

                    for pais in self.__lista_paises:
                        for art in lista_restantes_empatados:
                            if art.pertenece_a_pais(pais):
                                lista_seleccionados.append(art)
                                num_articulos_por_elegir -= 1
                                if num_articulos_por_elegir == 0:
                                    break
                        if num_articulos_por_elegir == 0:
                            break
                    
                else:
                    lista_seleccionados += primeros_n 
        
        print 'Lista Aceptados'
        for art in lista_seleccionados:
            print ".-%s " % (art)
                    
# la lista_articulo que se le pasa es una lista de articulos aceptable (prom >= 3)
# por lo que se suponen que todos los articulos que estan aqui son articulos que forman
    
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

class ArticuloCortes(ComoSeleccionarArticulos):
    
    # n1 primer numero de corte
    # n2 segundo numero de corte
    __n1 = None
    __n2 = None    
    __lista_paises = []
    
    # Constructor
    def __init__(self,lista_articulo, num_art_aceptar, corte1, corte2, lis_paises):
        super(ArticuloCortes, self).__init__(lista_articulo, num_art_aceptar)     
        if not isinstance(corte1, float) or not isinstance(corte2, float):
            raise TypeError
        cor1 = int(corte1)
        cor2 = int(corte2)
        if cor1 not in range(1,6) or cor2 not in range(1,6):
            raise ValueError
        
        if corte1 <= 3.0 or corte2 < 3.0 or corte2 >= corte1:
        #    print "Los valores no cumplen con la caracteristica indicada"
            raise ValueError
        
        if not isinstance(lis_paises, list):
            raise TypeError
        for pais in lis_paises:
            if not isinstance(pais, str):
                raise TypeError
        self.__n1 = corte1
        self.__n2 = corte2
        self.__lista_paises = lis_paises
            
    def seleccionar_articulos(self):
        #lista_promedios_aceptables = []
        self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                   key=lambda x: x.calcularPromedio(),
                                   reverse=True))            
        lista_promedios_aceptables = [ar for ar in self.get_lista_articulos() if ar.es_aceptable()]
        if len(self.get_lista_articulos()) <= self.get_num_articulos_aceptar():
            pass
        else:
            
            lista_seleccionados = []
            i = 0
            while i < len(lista_promedios_aceptables) and len(lista_seleccionados) < self.get_num_articulos_aceptar():
                if lista_promedios_aceptables[i].calcularPromedio() >= self.__n1:
                    lista_seleccionados.append(lista_promedios_aceptables[i])
                    lista_promedios_aceptables.remove(lista_promedios_aceptables[i])
                else:
                    break
            
            # status = aceptados    
            print "los seleccionados primer corte son: "         
            for i in lista_seleccionados:
                print i, i.calcularPromedio()

            print "los seleccionados aceptables al primero corte son: "         
            for i in lista_promedios_aceptables:
                print i, i.calcularPromedio()
            print
                

            # segundo corte
            tope = 0
            while tope < len(self.__lista_paises) and len(lista_seleccionados) < self.get_num_articulos_aceptar():
                pais = self.__lista_paises[tope]
                articulo = 0
                while articulo < len(lista_promedios_aceptables):
                    aux = lista_promedios_aceptables[articulo]
                    print aux
                    # ya recorri la lista con promedios aceptables para aceptar con el pais "pais"
                    if aux.calcularPromedio() < self.__n2:                        
                        break
                    encontrado = False
                    k = 0
                    for k in aux.get_autores():
                        if k.getPais() == pais:
                            encontrado = True
                            break
                    if encontrado and len(lista_promedios_aceptables)>0:
                        lista_seleccionados.append(aux)
                        lista_promedios_aceptables.remove(aux)
                    else:
                        articulo+=1
                tope += 1
                
            # los nuevos agregados respecto al primer corte serian AceptadoEspecial
            print "seleccionados finales: "
            for i in lista_seleccionados:
                print i, i.calcularPromedio()

            #estos deberian ser rechazadoXfaltaCupo
            print "los seleccionados aceptables sobrantes son: "         
            for i in lista_promedios_aceptables:
                print i, i.calcularPromedio()


class ArticuloPorcentaje(ComoSeleccionarArticulos):
    
    def __init__(self, lista_articulo, num_art_aceptar, lista_paises):
        super(ArticuloPorcentaje, self).__init__(lista_articulo, num_art_aceptar)
        if not isinstance(lista_paises, list):
            raise TypeError
        for pais in lista_paises:
            if not isinstance(pais, str):
                raise TypeError
        self.__lista_paises = lista_paises
    
    
    def seleccionar_articulos(self):
        num_articulos = len(self.get_lista_articulos())
        ochenta_por_ciento = self.get_num_articulos_aceptar() * 80 / 100
        veinte_por_ciento = self.get_num_articulos_aceptar() - ochenta_por_ciento
        self.set_lista_articulos(sorted(self.get_lista_articulos(),
                                key=lambda x: x.calcularPromedio()))   
        
        
        matriz_paises = [] # matriz que, por cada pais, guarda los articulos enviados
        for pais in self.__lista_paises:
            lista_articulos_por_pais = []
            for art in self.get_lista_articulos():
                for autor in art.get_autores():
                    if pais == autor.getPais():
                        lista_articulos_por_pais.append(art)
                        break
            matriz_paises.append((pais, lista_articulos_por_pais))
           
        # Ahora calculamos el 80 por ciento de los articulos    
        lista_seleccionados = []
        for i in matriz_paises:
            j = 0
            while j < len(i[1]): 
                aux = i[1][j]
                if aux in lista_seleccionados:
                    i[1].remove(aux)
                else:   
                    lista_seleccionados.append(aux)
                    self.get_lista_articulos().remove(aux)
                    tam_lista_seleccionados = len(lista_seleccionados)
                    # Chequeo si ya seleccione el 80 por ciento o se me acabaron los articulos
                    if (tam_lista_seleccionados == ochenta_por_ciento or 
                        tam_lista_seleccionados == num_articulos):
                        break
                    
                    i[1].remove(aux)
                    
            if (tam_lista_seleccionados == ochenta_por_ciento or 
                tam_lista_seleccionados == num_articulos):
                break
        
        print "80p:%s 20p:%s numeroselecc:%s num_art:%s" % (ochenta_por_ciento, veinte_por_ciento, tam_lista_seleccionados, num_articulos)
        if tam_lista_seleccionados < num_articulos:
        # Ahora seleccionamos el 20 por ciento restante 
        # con respecto al mejor promedio
            j = tam_lista_seleccionados
            for i in range(0, veinte_por_ciento):
                if j == num_articulos:
                    break
                lista_seleccionados.append(self.get_lista_articulos().pop())
                j += 1
        
                
        print "seleccionados finales: "
        for i in lista_seleccionados:
            print i, i.calcularPromedio()

            
        
        
            
        
if __name__ == "__main__":
# prueba de desempate    
    cp1 = Persona.CP("a", "b", "usb", "Venezuela", ["Redes"], True);
    cp2 = Persona.CP("a", "b", "usb", "Venezuela", ["Base"], True);
    cp3 = Persona.CP("a", "b", "usb", "Venezuela", ["Computacion"], True);
    
    autor1 = Persona.Autor("a1", "b", "usb", "Venezuela");
    autor2 = Persona.Autor("a2", "b", "usb", "Venezuela");
    autor3 = Persona.Autor("a3", "b", "usb", "Camerun");

    
    
    a1 = Articulo.Articulo("Titulo1", ["pal1", "pal2"], ["Base", "Redes"], [autor1,autor2],[(cp1, 3) , (cp2, 3), (cp3, 3)])
    a2 = Articulo.Articulo("Titulo2", ["pal1", "pal2"], ["Base", "Redes"], [autor1],[(cp1, 4) , (cp2, 4), (cp3, 4)])
    a3 = Articulo.Articulo("Titulo3", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [autor1,autor3], [(cp1, 4) , (cp2, 3), (cp3, 3)])
    a4 = Articulo.Articulo("Titulo4", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [autor1,autor2],[(cp1, 4) , (cp2, 4), (cp3, 5)])
    a5 = Articulo.Articulo("Titulo5", ["pal1", "pal2"], ["Base", "Redes", "Computacion"], [autor3,autor2],[(cp1, 3) , (cp2, 3), (cp3, 3)])
    
    topicos = Topico.Topico("Base")
    topi1 = Topico.Topico("Redes")
    topi2 = Topico.Topico("Computacion")

    estrategia3 = ArticuloPaisesDesempate([a1, a2, a3,a4,a5], 4,  ["Camerun","Venezuela"], 1);
    print "Estrategia #EmpatadosPaises"
    estrategia3.seleccionar_articulos()