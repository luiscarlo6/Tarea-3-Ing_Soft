'''
Created on 08/12/2013

@author: admin
'''
import unittest
import Lugar

class Test(unittest.TestCase):


    def setUp(self):
        self.lugar = Lugar.Lugar("nombre","ubicacion", 100);


    def tearDown(self):
        self.lugar = None;


    def testGetNombre(self):
        self.lugar.setNombre("maria");
        self.assertEqual(self.lugar.getNombre(), "maria"), "no funciona get nombre"
        
    def testSetNombre(self):
        self.lugar.setNombre("pedro");
        self.assertEqual(self.lugar.getNombre(), "pedro"), "no funciona set nombre"
        
    def testGetUbicacion(self):
        self.lugar.setUbicacion("salon1");
        self.assertEqual(self.lugar.getUbicacion(), "salon1"), "no funciona get ubicacion"
        
    def testSetUbicacion(self):
        self.lugar.setUbicacion("sala10");
        self.assertEqual(self.lugar.getUbicacion(), "sala10"), "no funciona set ubicacion"
        
    def testGetCapacidad(self):
        self.lugar.setCapacidad(300);
        self.assertEqual(self.lugar.getCapacidad(), 300), "no funciona get capacidad"
        
    def testSetCapacidad(self):
        self.lugar.setCapacidad(320);
        self.assertEqual(self.lugar.getCapacidad(), 320), "no funciona set capacidad"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testNombre']
    unittest.main()