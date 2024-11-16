import unittest
import numpy as np
from numpy.polynomial import Legendre



class TestPolinomiosOrtogonales(unittest.TestCase):
    def test_legendre(self):
        # prueba de polinomio de Legendre en grado 2
        grado = 2
        x_val = 0.5
        pol_legendre = Legendre(grado)  # scipy para el polinomio de Legendre
        valor_calculado = pol_legendre(x_val)
        
        # función para el cálculo del polinomio de Legendre en el paso 3
        valor_funcion = calcular_pol_ortogonal(grado, x_val, tipo="legendre")
        
        self.assertAlmostEqual(valor_funcion, valor_calculado, places=5)
        x_legendre = np.linspace(-1, 1, 100)
        P3 = Legendre([0, 0, 0, 1])  # Polinomio de Legendre de grado 3
        y_legendre = P3(x_legendre)
        
if __name__ == '__main__':
    unittest.main()
