import unittest
import Persona
import Articulo

class PersonaTestCase(unittest.TestCase):
    
    
    def setUp(self):
        self.persona = Persona.Persona("nombre","apellido", "institucion", "pais", ["Base de Datos", "Robotica"])
        
        
    def tearDown(self):
        self.persona = None
        
        
    def testGetNombre(self):
        self.persona.setNombre("luis")
        self.assertEqual(self.persona.getNombre(), "luis"), "getNombre: no funciona"
        
        
    def testSetNombre(self):
        self.persona.setNombre("Franklin")
        self.assertEqual(self.persona.getNombre() , "Franklin"), "setNombre() no establece el valor de nombre apropiadamente"
        
                
    def testSetNombre1(self):
        try:
            self.persona.setNombre(2)
        except TypeError:
            pass
        else:
            self.assertFalse(True,  'setNombre(): Se esperaba un TypeError')
            
    def testSetNombre2(self):
        try:
            self.persona.setNombre("")
        except ValueError:
            pass
        else:
            self.assertFalse(True,  'setNombre(): Se esperaba un ValueError')
            
            
    def testGetApellido(self):
        self.persona.setApellido("luis")
        self.assertEqual(self.persona.getApellido(), "luis"), "getApellido: no funciona"
    
        
              
    def testSetApellido(self):
        self.persona.setApellido("Franklin")
        self.assertTrue(self.persona.getApellido() == "Franklin", 
                "setApellido() no establece el valor de apellido apropiadamente")
        
        
    def testSetApellido1(self):
        try:
            self.persona.setApellido(2)
        except TypeError:
            pass
        else:
            self.assertFalse(True,'setApellido(): Se esperaba un TypeError')
            
    def testSetApellido2(self):
        try:
            self.persona.setApellido("")
        except ValueError:
            pass
        else:
            self.assertFalse(True,'setApellido(): Se esperaba un ValueError')
            
            
    def testGetInstitucion(self):
        self.persona.setInstitucion("UCV")
        self.assertEqual(self.persona.getInstitucion(), "UCV"), "getInstitucion(): no funciona"
        
        
    def testSetInstitucion(self):
        self.persona.setInstitucion("USB")
        self.assertEqual(self.persona.getInstitucion() , "USB"), "setInstitucion() no establece el valor de institucion apropiadamente"      
        
          
    def testSetInstitucion1(self):
        try:
            self.persona.setInstitucion(2)
        except TypeError:
            pass
        else:
            self.assertFalse(True,  'setInstitucion(): Se esperaba un TypeError')
            
    def testSetInstitucion2(self):
        try:
            self.persona.setInstitucion("")
        except ValueError:
            pass
        else:
            self.assertFalse(True,  'setInstitucion(): Se esperaba un ValueError')
            

    def testGetPais(self):
        self.persona.setPais("Venezuela")
        self.assertEqual(self.persona.getPais() , "Venezuela"), "getPais(): no funciona"
        
        
    def testSetPais(self):
        self.persona.setPais("Mexico")
        self.assertTrue(self.persona.getPais() == "Mexico", 
                "setPais() no establece el valor del pais apropiadamente")
        
        
    def testSetPais1(self):
        try:
            self.persona.setPais([2,3])
        except TypeError:
            pass
        else:
            self.assertFalse(True,'setPais(): Se esperaba un TypeError')
            
    def testSetPais2(self):
        try:
            self.persona.setPais("")
        except ValueError:
            pass
        else:
            self.assertFalse(True,'setPais(): Se esperaba un ValueError')
            
class ArticuloTestCase(unittest.TestCase):
    
    def setUp(self):
        self.articulo = Articulo.Articulo("Titulo", ["pal1", "pal2"], ["Base de datos", "Redes"], [])
        
        
    def tearDown(self):
        self.articulo = None
        
        
    def testGetTitulo(self):
        self.articulo.setTitulo('Seguridad Informatica en la Deep Web')
        self.assertEqual(self.articulo.getTitulo() , "Seguridad Informatica en la Deep Web"), "getTitulo(): no funciona"
        
        
    def testSetTitulo(self):
        self.articulo.setTitulo("Criptografia")
        self.assertTrue(self.articulo.getTitulo() == "Criptografia", 
                "setTitulo() no establece el valor del pais apropiadamente")
        
    def testSetTitulo1(self):
        try:
            self.articulo.setTitulo([2,3])
        except TypeError:
            pass
        else:
            self.assertFalse(True,'setTitulo(): Se esperaba un TypeError')
            
    def testSetResumen0(self):
        self.articulo.setResumen(["pal", "perro", "hola"])
        self.assertListEqual(self.articulo.getResumen(), ["pal", "perro", "hola"], "setResumen(): no funciona correctamente")
            
            
    def testSetResumen1(self):
        try:
            self.articulo.setResumen(["hola", "como", "estan", "pal", "perro", "hola"])
        except ValueError:
            pass
        else:
            self.assertFalse(True, "setResumen(): Se esperaba ValueError por tener demasiadas palabras resumen")
        
    def testSetResumen2(self):
        try:
            self.articulo.setResumen([])
        except ValueError:
            pass
        else:
            self.assertFalse(True, "setResumen(): Se esperaba ValueError por no tener palabras resumen")
            
    def testGetResumen(self):
        self.assertListEqual(self.articulo.getResumen(), ["pal1", "pal2"], 'getResumen(): no funciona correctamente')
        
    def testGetResumen1(self):
        self.articulo.setResumen(["hola", "como", "estan"])
        self.assertListEqual(self.articulo.getResumen(), ["hola", "como", "estan"], 'getResumen(): no funciona correctamente')
    
        
        
    def testAgregarPuntuacion(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 2))
        self.assertListEqual(self.articulo.getPuntuaciones(), [(a1, 2)], "calcularPromedio(): no funciona correctamente")
        
    
    def testAgregarPuntuacion1(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        a2 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        a3 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 2))
        self.articulo.agregarPuntuacion((a2, 5))
        self.articulo.agregarPuntuacion((a3, 1))
        self.assertListEqual(self.articulo.getPuntuaciones(), [(a1, 2), (a2, 5), (a3, 1)], "calcularPromedio(): no funciona correctamente")
    
    def testAgregarPuntuacion2(self):
        try:
            a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
            a2 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
            a3 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
            self.articulo.agregarPuntuacion((a1, 2))
            self.articulo.agregarPuntuacion((a2, 5))
            self.articulo.agregarPuntuacion((a3, 6))
        except ValueError:
            pass
        else:
            self.AssertFalse(True, "agregarPuntuacion: Se esperaba un ValueError")
        
    
        
    def testCalcularPromedio(self):
        self.assertEqual(self.articulo.calcularPromedio(), 0, "calcularPromedio(): no funciona correctamente")
        
    def testCalcularPromedio1(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 2))
        self.assertEqual(self.articulo.calcularPromedio(), 2, "calcularPromedio(): no funciona correctamente")
        
    def testCalcularPromedio2(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        a2 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 2))
        self.articulo.agregarPuntuacion((a2, 3))
        self.assertEqual(self.articulo.calcularPromedio(), 2.5, "calcularPromedio(): no funciona correctamente")
        
    def testCalcularPromedio3(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        a2 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
        a3 = Persona.CP("bab", "aba", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 5))
        self.articulo.agregarPuntuacion((a2, 5))
        self.articulo.agregarPuntuacion((a3, 5))
        self.assertEqual(self.articulo.calcularPromedio(), 5, "calcularPromedio(): no funciona correctamente")
        
    def testCalcularPromedio4(self):
        a1 = Persona.CP("a", "b", "usb", "venezuela", ["Redes"], True)
        a2 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
        a3 = Persona.CP("bab", "aba", "usb", "venezuela", ["Redes"], True)
        a4 = Persona.CP("a", "b", "usb", "venezuela", ["Redes", "Bases de datos"], True)
        a5 = Persona.CP("ab", "ab", "usb", "venezuela", ["Redes"], True)
        self.articulo.agregarPuntuacion((a1, 1))
        self.articulo.agregarPuntuacion((a2, 2))
        self.articulo.agregarPuntuacion((a3, 3))
        self.articulo.agregarPuntuacion((a4, 4))
        self.articulo.agregarPuntuacion((a5, 5))
        self.assertEqual(self.articulo.calcularPromedio(), 3, "calcularPromedio(): no funciona correctamente")
        
        
    def testCalcularPromedio5(self):
        try:
            self.articulo.agregarPuntuacion(1)
            self.articulo.agregarPuntuacion(2)
            self.articulo.agregarPuntuacion(3)
            self.articulo.agregarPuntuacion(4)
            self.articulo.agregarPuntuacion(0)
        except:
            pass
        else:
            self.AssertFalse(True, "calcularPromedio(): Se esperaba ValueError por ingresar una nota indebida")
            
            
    def testEsAceptable(self):
        a3 = Persona.CP("a", "b", "usb", "venezuela", ["bases"], True)
        a4 = Persona.CP("ab", "ba", "usb", "venezuela", ["bases"], False)
        self.articulo.setPuntuaciones([(a3,3), (a4,3)])
        self.assertTrue(self.articulo.es_aceptable(), "es_aceptable() no funciona correctamente")
            
            
    def testEsAceptable1(self):
        self.articulo.setPuntuaciones([])
        self.assertFalse(self.articulo.es_aceptable(), "es_aceptable() no funciona correctamente")
    
    
    def testEsAceptable2(self):
        a1 = Persona.CP("Erick", "Dos Santos", "usb", "venezuela", ["bases"], True)
        a2 = Persona.CP("JJ", "Pradera", "usb", "venezuela", ["bases"], True)
        a3 = Persona.CP("a", "b", "usb", "venezuela", ["bases"], True)
        a4 = Persona.CP("vuel", "cara", "usb", "venezuela", ["bases"], True)
        self.articulo.setPuntuaciones([(a1, 2), (a2, 3), (a3, 1), (a4, 1)])
        self.assertFalse(self.articulo.es_aceptable(), "es_aceptable() no funciona correctamente")
    
    
    def testEsAceptable3(self):
        a3 = Persona.CP("a", "b", "usb", "venezuela", ["bases"], True)
        self.articulo.setPuntuaciones([(a3, 5)])
        self.assertFalse(self.articulo.es_aceptable(), "es_aceptable() no funciona correctamente")
    
            
class CPTestCase(unittest.TestCase):
    def setUp(self):
        self.CP = Persona.CP("Fran", "Padilla", "Institucion", "Venezuela",["Base de Datos"], False)
        
    def testGetEsPresidente(self):
        self.assertFalse(self.CP.getEsPresidente(), "getEsPresidente(): no funciona correctamente")
        
    def testSetEsPresidente(self):
        self.CP.setEsPresidente(True)
        self.assertTrue(self.CP.getEsPresidente(), "getEsPresidente(): no funciona correctamente")
        
    def testSetEsPresidente1(self):
        try:
            self.CP.setEsPresidente(2)
        except TypeError:
            pass
        else:
            self.assertTrue(False, "getEsPresidente(): Se esperaba un TypeError")
        
        
   
        
    