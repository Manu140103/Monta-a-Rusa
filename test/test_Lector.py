import unittest
import numpy as np
import sys
import os

from src.Lector import leer_datos_csv
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..','src')))


class TestLeerDatosCSV(unittest.TestCase):
    def setUp(self):
        self.file_path = 'datos.csv'
    
    def test_leer_datos_csv(self):
        data_paso1, data_paso2, data_paso4 = leer_datos_csv(self.file_path)
        
        # Verificar dimensiones esperadas para cada bloque de datos
        self.assertEqual(data_paso1.shape, (6, 2))
        self.assertEqual(data_paso2.shape, (5, 2))
        self.assertEqual(data_paso4.shape, (3, 4))
        
        # Verificar algunos valores específicos
        np.testing.assert_array_almost_equal(data_paso1[0], [0, 0.5])
        np.testing.assert_array_almost_equal(data_paso2[0], [0, 1.1])
        np.testing.assert_array_almost_equal(data_paso4[0], [1, 2, 1, 4])

if __name__ == '__main__':
    unittest.main()





