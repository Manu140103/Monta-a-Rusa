import unittest
import numpy as np
import sys, os
from src.Paso_4 import trazador_cubico
from src.Lector import leer_datos_csv

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..','src')))


class TestResolverEcuaciones(unittest.TestCase):
    def setUp(self):
        self.file_path = 'datos.csv'
    
    def test_resolver_ecuaciones(self):
        _, _, data_paso4 = leer_datos_csv(self.file_path)
        A = data_paso4[:, :3]
        b = data_paso4[:, 3]
        
        # Calculamos la solución usando numpy
        x_solution = np.linalg.solve(A, b)
        expected_solution = [1.0, 1.0, 1.0]  # Solución esperada
        np.testing.assert_array_almost_equal(x_solution, expected_solution, decimal=1)

if __name__ == '__main__':
    unittest.main()
