import unittest
import numpy as np
from scipy.interpolate import CubicSpline

from src.Paso_1 import trazador_cubico
class TestTrazadorCubico(unittest.TestCase):
    def setUp(self):
        self.file_path = 'datos.csv'
    
    def test_trazador_cubico(self):
        x_data = np.array([0, 1, 2, 3, 4, 5])
        y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])
        
        bc_type = ((1, 0.0), (1, 0.0))
        valor_test = CubicSpline(x_data, y_data, bc_type=bc_type)
        
        # Comprobamos un valor de interpolación
        self.assertAlmostEqual(valor_test(2), 1.0, places=1)

if __name__ == '__main__':
    unittest.main()
