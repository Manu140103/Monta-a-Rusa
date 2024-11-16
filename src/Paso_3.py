import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Legendre

# Polinomios Ortogonales

def polinomio_ortogonal():
    x_legendre = np.linspace(-1, 1, 100)
    P3 = Legendre([0, 0, 0, 1])  # Polinomio de Legendre de grado 3
    y_legendre = P3(x_legendre)

    plt.figure(figsize=(10, 6))
    plt.plot(x_legendre, y_legendre, label="Polinomio de Legendre P3")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Polinomio Ortogonal de Legendre para Optimización de Tramos")
    plt.legend()
    plt.grid()
    plt.show()
