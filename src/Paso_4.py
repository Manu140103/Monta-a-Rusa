import numpy as np
from scipy.linalg import solve
from Lector import leer_datos_csv

# Resolución de Ecuaciones

def resolver_ecuaciones(file_path):
    _, _, data_paso4 = leer_datos_csv(file_path)
    A = data_paso4[:, :3]
    b = data_paso4[:, 3]

    x_solution = solve(A, b)
    print("Solución del sistema Ax = b:")
    print(x_solution)
