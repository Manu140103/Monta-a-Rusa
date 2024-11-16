import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from Lector import leer_datos_csv

# Método de Trazador Cúbico Sujeto

def trazador_cubico(file_path):
    data_paso1, _, _ = leer_datos_csv(file_path)
    x_data = data_paso1[:, 0]
    y_data = data_paso1[:, 1]

    bc_type = ((1, 0.0), (1, 0.0))
    cubic_spline = CubicSpline(x_data, y_data, bc_type=bc_type)

    x_vals = np.linspace(x_data[0], x_data[-1], 100)
    y_vals = cubic_spline(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, 'o', label="Puntos de control")
    plt.plot(x_vals, y_vals, label="Trazador cúbico")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Método de Trazador Cúbico Sujeto")
    plt.legend()
    plt.grid()
    plt.show()
