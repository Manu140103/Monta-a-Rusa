import numpy as np
import matplotlib.pyplot as plt
from Lector import leer_datos_csv

# Polinomio de Mínimos Cuadrados

def ajuste_minimos_cuadrados(file_path):
    _, data_paso2, _ = leer_datos_csv(file_path)
    x_data = data_paso2[:, 0]
    y_data = data_paso2[:, 1]

    coef = np.polyfit(x_data, y_data, 2)
    poly_fit = np.poly1d(coef)

    x_vals = np.linspace(x_data[0], x_data[-1], 100)
    y_vals = poly_fit(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_data, y_data, 'o', label="Datos experimentales")
    plt.plot(x_vals, y_vals, label="Ajuste de mínimos cuadrados (grado 2)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Ajuste de Polinomio de Mínimos Cuadrados")
    plt.legend()
    plt.grid()
    plt.show()

