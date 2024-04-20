import unittest #libería especifica para pruebas unitarias, estas ayudan a probar funciones concretas en python
from suma import sumar #importamos del fichero sumar.py la funcion suma

class TestSumar(unittest.TestCase):#creamos clase llamada TestSumar que recibe como parametro prueba unitaria 

#Dentro de la clases tenemos un método que se llama test_sumar que llama a 3 funciones
    def test_sumar(self):
        #con el metodoo assertEqual, decimos ejecutar 3 + 2 el resultado es 5
        #si falla git hub actions nos debe de avisar
        self.assertEqual(sumar(3,2),5)#recibe como parametro a la función sumar y el 5 es el resultado esperado
        self.assertEqual(sumar(-1,1),0)
        self.assertEqual(sumar(-1,-1),-2)

if __name__ == '__main__':
    unittest.main()



