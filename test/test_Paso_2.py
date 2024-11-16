import unittest
import numpy as np



class TestMinimosCuadrados(unittest.TestCase):
    def setUp(self):
        self.file_path = 'datos.csv'
    
    def test_ajuste_minimos_cuadrados(self):

        x_data = np.array([0, 1, 2, 3, 4])
        y_data = np.array([1.1, 3.5, 2.8, 4.2, 5.0])

        coef = np.polyfit(x_data, y_data, 2)
        expected_coef = [-0.07857143,  1.16428571,  1.46285714]
        np.testing.assert_array_almost_equal(coef, expected_coef, decimal=1)

if __name__ == '__main__':
    unittest.main()
