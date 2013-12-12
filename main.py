import Persona
import Articulo
import Topico
import Lugar
# NO LES DE FLOJERA Y CORRANLO!

# VARIABLES GLOBALES

# Diccionario donde se almacenaran los articulos de la Conferencia 
# que tendra el siguiente formato
# { 1 : articulo1 , 2 : articulo2, 3 : articulo3, ...}
articulos = {}

# Diccionario donde se almacenaran los miembros del CP, incluyendo su presidente,
# que tendra el siguiente formato
# { 1 : CP1 , 2 : CP2, 3 : CP3, ...}
CPs = {}

# Diccionario donde se almacenaran los lugares de la Conferencia 
# que tendra el siguiente formato
# { 1 : lugar1 , 2 : lugar2, 3 : lugar3, ...}
lugares = {}

# Numero de miembros del comite que se han agregado hasta ahora
num_cp = 0

# Numero de articulos que se han agregado hasta ahora
num_articulos = 0

# Numero de lugares que se han agregado hasta ahora
num_lugares = 0

# Variable booleana que indica el cierre del programa
es_fin = False

# Variable booleana que indica si ya el presidente del CP 
# fue elegido
presidente_elegido = False

# Lista de articulos que se aceptaran
lista_aceptados = []

# Lista para los topicos
lista_topicos = []

# Lista de articulos empatados, para ser 
# elegidos como aceptados por el presidente
# del comite(funcionalidad aun no implementada) 
lista_empatados = []

# Numero n de articulos a aceptar 
n = 3

def chequear_topicos_articulos(topicos, topico_entrada):
    for i in topicos:
        if i == topico_entrada:
            return True
    return False    
        
def chequear_topicos(topico_entrada):        
    for j in lista_topicos:
        if j.comparar_topico(topico_entrada):
            return True
    return False

def agregarLugar():
    
    global lugares, num_lugares
    lugar = Lugar.Lugar("nombre","ubicacion", 1)
    
    while(True):
        try:
            print "Ingrese el nombre del lugar: ",
            nombre = raw_input()
            lugar.setNombre(nombre)
            break
        except ValueError:
            print ValueError
            continue
        
    while(True):
        try:
            print "Ingrese la ubicacion del lugar: "
            ubicacion = raw_input()
            lugar.setUbicacion(ubicacion)
            break
        except:
            continue
    
    while(True):
        try:
            print "Ingrese la capacidad del lugar: "
            capacidad = input()
            lugar.setCapacidad(capacidad)
            break
        except:
            print "Valor Erroneo. Intente de nuevo"
            continue
    
    lugares[num_lugares]= lugar 
    num_lugares = num_lugares + 1  
        
def agregarArticulo():
    global presidente_elegido, articulos, num_articulos
    resumen = []
    topicos = []
    
    # Se construye un nuevo articulo y le pasamos unos valores default
    # A medida que el usuario vaya insertando los datos, el articulo
    # se ira conformando.
    articulo = Articulo.Articulo("titulo", ["pal1"], [], []) 
    
    # Se pide por pantalla el titulo
    while(True):
        try:
            print "Ingrese el titulo:",
            titulo = raw_input()
            # Establecemos el titulo al articulo
            articulo.setTitulo(titulo)
            break
        except:
            continue
    
    # Se pide por pantalla el resumen 
    while(True):
        try:
            resumen.append(raw_input("Ingrese una palabra resumen: "))
            
            # Si el usuario ingresa "1" es porque quiere agregar otra palabra resumen
            if raw_input("Desea agregar otra palabra?(Presione 1 si es afirmativo): ") != "1":
                # Agregamos la lista de resumenes armada al articulo
                articulo.setResumen(resumen)
                break
            continue
        except ValueError:
            print "Caracter no valido. Intente de nuevo."
            continue
      
    # Se pide por pantalla los topicos del articulo  
    while(True):
        try:
            topico_recibido = raw_input("Ingrese el topico del articulo: ")
            
            '''encontrado = False
            for i in topicos:
                if i == topico_recibido:
                    encontrado = True
                    break'''
                
            if chequear_topicos_articulos(topicos,topico_recibido):
                print "Este topico ya existe."
                continue
            
            '''encontrado = False
            for j in lista_topicos:
                if j.comparar_topico(topico_recibido):
                    encontrado = True
                    break'''
                
            if not chequear_topicos(topico_recibido):
                print "Me meti a agregar un topico"
                lista_topicos.append(Topico.Topico(topico_recibido))
                
            
            topicos.append(topico_recibido)
            
            
            
            
            # Si el usuario ingresa "1" es porque quiere agregar otra palabra resumen
            if raw_input("Desea agregar otro topico?(Presione 1 si es afirmativo): ") != "1":
                articulo.setTopicos(topicos)
                break
            continue
        except:
            print "Caracter no valido. Intente de nuevo.aaaaaaaaaaaaa"
            continue
   
    # Se agrega el articulo a la lista de articulos y se incrementa el contador     
    articulos[num_articulos]= articulo 
    num_articulos = num_articulos + 1  
    
    raw_input("Articulo agregado!\nPresione cualquier tecla para volver al menu")


# Funcion que crea y agrega un miembro del CP a lista de CP 
def agregarCP():
    global presidente_elegido, CPs, num_cp
    topicos = []
    miembroCP = Persona.CP("nombre", "apellido", "inst", "pais", [], False) 
    print "Ingrese el nombre: ",
    while(True):
        try:
            nombre = raw_input()
            miembroCP.setNombre(nombre)
            break
        except:
            continue
    print "Ingrese el apellido: ",
    while(True):
        try:
            apellido = raw_input()
            miembroCP.setApellido(apellido)
            break
        except:
            continue
    print "Ingrese la institucion donde trabaja: ",
    while(True):
        try:
            institucion = raw_input()
            miembroCP.setInstitucion(institucion)
            break
        except:
            continue
        
    print "Ingrese el pais de origen: ",
    while(True):
        try:
            pais = raw_input()
            miembroCP.setPais(pais)
            break
        except:
            continue
        
    # Se pide por pantalla el/los topicos que domina el CP
    while(True):
        try:
            topicos.append(raw_input("Ingrese el topico que domina el CP: "))
            if raw_input("Desea agregar otro topico?(Presione 1 si es afirmativo): ") != "1":
                miembroCP.setTopicos(topicos)
                break
            continue
        except:
            print "Caracter no valido. Intente de nuevo."
            continue
        
    # Si el presidente no ha sido elegido ya, entonces se pregunta
    # si este miembro del CP que se esta creando sera el presidente
    if not presidente_elegido:
        while(True):
            try:
                p = input("Es el presidente(1 si, 0 no)?")
                if p == 1:
                    miembroCP.setEsPresidente(True) 
                    presidente_elegido = True
                    break
                if p == 0:
                    break
                else:
                    continue
            except:
                    continue
                
    # Se agrega el cp a la lista global de CP                  
    CPs[num_cp]= miembroCP 
    # Se incremente el contador de miembros de CP
    num_cp = num_cp + 1  
    
    raw_input("Miembro CP agregado!\nPresione cualquier tecla para volver al menu")
    
    
def agregarPuntuacion():
    global CPs, articulos
    # Si no hay miembros de CP, no tiene sentido una evaluacion
    if len(CPs) == 0 :
        print "No hay CP's"
        return
    
    # Si no hay articulos, no tiene sentido una evaluacion
    if len(articulos) == 0 :
        print "No hay articulos que evaluar"
        return
    
    # De entre todos los CPs creados, se elige al arbitro
    while True:
        # Se muestra por pantalla una lista con todos los cps
        # para que el usuario tenga la oportunidad de elegir
        # al que sera el arbitro
        print "Elija el arbitro: "
        for cp in CPs:
            print "%s.- %s" % (cp, CPs[cp])
        print "Presione %s para salir" % len(CPs)
        
        try:
            choice = input()
            if choice == len(CPs):
                # Si entra aqui quiere decir que el usuario ya no quiere
                # hacer la evaluacion y se devuelve al menu
                return
            # Cuando el usuario elige su opcion, se extrae de la
            # lista el cp que eligio
            CP_elegido = CPs[choice]
            break
        except:
            print "Valor Erroneo. Intente de nuevo"
            continue
        
   
    while True:
        # Esta variable local indica si ya existe una evaluacion
        # entre el arbitro elegido y el articulo que 
        # se elige evaluar
        ya_hay_evaluacion = False
        
        # Se muestra por pantalla una lista con todos los articulos
        # para que el usuario tenga la oportunidad de elegir
        # al que sera el articulo que se desea evaluar
        print "Elija el articulo a evaluar"
        for ar in articulos:
            print "%s.- %s" % (ar, articulos[ar])
        print "Presione %s para salir" % len(articulos)
        try:
            choice = input()
            if choice == len(articulos):
                # Si entra aqui quiere decir que el usuario ya no quiere
                # hacer la evaluacion y se devuelve al menu
                return
            
            # Cuando el usuario elige su opcion, se extrae de la
            # lista el articulo que eligio para ser evaluado
            articulo_elegido = articulos[choice]
        except:
            print "Valor Erroneo. Intente de nuevo"
            continue
        
        # Verificamos que el CP no haya evaluado ya el articulo
        # Para cada evaluacion que se ha hecho sobre este articulo  
        for evaluacion in articulo_elegido.getPuntuaciones():
            # Si el cp que hizo esa evaluacion es el mismo CP
            # que eligio el usuario, entonces se 
            # modifica la variable ya hay evaluacion
            if(evaluacion[0] == CP_elegido):
                ya_hay_evaluacion = True
        
        # Si ya existe una evaluacion del cp elegido hacia el articulo elegido
        # entonces retrocedemos a la eleccion del articulo a evaluar      
        if ya_hay_evaluacion == True:
            print "Ya existe una evaluacion del arbitro hacia este articulo"
            continue 
                                            
        # Si no existe una evaluacion entonces se procede a evaluar
        
        # Aqui se verifica si algun topico que domina el arbitro elegido coincide
        # con algun topico del articulo a evaluar
        if len([x for x in articulo_elegido.getTopicos() if x in CP_elegido.getTopicos()]) != 0:
            while True:
                try:
                    # Se pide la nota y se agrega al articulo
                    articulos[choice].agregarPuntuacion((CP_elegido, input("Elija la nota(1..5): ")))
                    break
                except ValueError:
                    print "Se espera una nota entre 1 y 5"
                    continue
            break
        # No coinciden, se retrocede hasta la eleccion del articulo a evaluars
        else:
            print "El CP no es experto en el topico del articulo. Intente de nuevo"
            continue
            
    raw_input("Puntuacion Agregada!\nPresione cualquier tecla para volver al menu")
    

# Funcion que forma las lista de aceptados y la lista de empatados de
# acuerdo al criterio de mayor promedio       
def generarAceptadosEmpatados():
    global lista_aceptados, lista_empatados, n
    
    # Primero obtenemos la lista de articulos cuyo promedio sea mayor o igual a 3
    # la llamaremos lista de aceptables
    lista_aceptables = [art for art in list(articulos.values()) if art.es_aceptable()]
    
    # Si el numero de articulos aceptables es menor al numero de articulos que
    # se deben aceptar, pues se aceptan todos y listo
    if len(lista_aceptables) <= n:
        lista_aceptados = lista_aceptables
        lista_empatados = []
        
    # Si no, es necesario dejar por fuera algunos :-( 
    else:
        # Ordenamos a los articulos aceptables de acuerdo al promedio
        # de mayor a menor
        lista_aceptables = sorted(lista_aceptables,
                                   key = lambda x: x.calcularPromedio(),
                                   reverse = True)
        
        # Ahora obtenemos de la lista de aceptables, los n articulos que
        # mejor promedio tienen,(recordar que n es el numero maximo de articulos
        # que se pueden aceptar), a esa lista la llamaremos los primeros n,
        # pero espera, puede que estemos dejando
        # por fuera articulos empatados
        # Necesitamos saber si algunos de los que dejamos por fuera
        # tiene igual promedio que los que estamos aceptando
        primeros_n = lista_aceptables[0:n]
        
        # Para ello calculamos el minimo promedio que hay de los primeros n 
        min_promedio = min([ar.calcularPromedio() for ar in primeros_n])
        print "minpromedio: ", min_promedio
        
        # Todos los articulos que tengan ese minimo promedio, seran
        # los articulos que consideraremos como Empatados
        empatados = [ar for ar in lista_aceptables if ar.calcularPromedio() == min_promedio]
        print "cantidad de empatados: ", len(empatados)
        
        # Si hay empatados los agregamos y los aceptados
        # seran aquellos que tengan promedio MAYOR al promedio minimo
        if len(empatados) > 1:
            lista_empatados = empatados
            lista_aceptados = [ar for ar in primeros_n if ar.calcularPromedio() > min_promedio]
            
        # Si no hay empatados, entonces los aceptados seran los primeros n y listo 
        # el presidente del CP no tendra que elegir nada :-)
        else:
            lista_aceptados = primeros_n
            lista_empatados = [] 


# Funcion que muestra por pantalla los articulos aceptados          
def mostrarAceptados():           
    generarAceptadosEmpatados()
    if len(lista_aceptados) == 0:
        print "No hay articulos aceptados que mostrar"
    else:
        print "########  LISTA DE ARTICULOS ACEPTADOS ########"
        for art in lista_aceptados:
            print "%s. Promedio: %s" % (art, art.calcularPromedio())   
            
    raw_input("Presione cualquier tecla para volver al menu")      
   
   
# Funcion que muestra por pantalla los articulos empatados
def mostrarEmpatados():
    generarAceptadosEmpatados()
    if len(lista_empatados) == 0:
        print "No hay articulos empatados que mostrar"
    else:
        print "########  LISTA DE ARTICULOS EMPATADOS ########"
        for art in lista_empatados:
            print "%s. Promedio: %s" % (art, art.calcularPromedio())    
            
    for art in articulos:   
            print articulos[art], articulos[art].getPuntuaciones()         
    raw_input("Presione cualquier tecla para volver al menu")
    
    
# Funcion que termina la ejecucion de la interaccion con el usuario      
def salir():
    global es_fin
    es_fin = True



# MAIN
if __name__ == "__main__":
  
    # MENU
    comandos = {1 : agregarArticulo, 2 : agregarCP, 3 : agregarPuntuacion, 
                4 : mostrarAceptados, 5 : mostrarEmpatados, 6 : agregarLugar, 7 : salir}
    while(not es_fin ):
        print "######  CLEI  ######\n"
        print "1.- Agregar Articulo"
        print "2.- Agregar CP"
        print "3.- Agregar puntuacion"
        print "4.- Chequear lista de ACEPTADOS"
        print "5.- Chequear lista de EMPATADOS"
        print "6.- Agregar Lugares"
        print "7.- Salir"
        print "Ingrese su opcion:"
        try:
            choice = input(">>")
        except :
            continue
        if choice not in range(1,7):
            continue
        # Se ejecuta el comando elegido
        comandos[choice]() 
        
        