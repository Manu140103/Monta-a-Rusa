import numpy as np

def leer_datos_csv(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data_paso1 = []
    data_paso2 = []
    data_paso4 = []

    bloque_actual = None
    for line in lines:
        line = line.strip()

        if line == '':
            bloque_actual = None
            
        elif 'x_data_paso1' in line:
            bloque_actual = 'paso1'
            
        elif 'x_data_paso2' in line:
            bloque_actual = 'paso2'
            
        elif 'A1' in line:
            bloque_actual = 'paso4'
            
        else:
            if bloque_actual == 'paso1':
                data_paso1.append([float(x) for x in line.split(',')])
                
            elif bloque_actual == 'paso2':
                data_paso2.append([float(x) for x in line.split(',')])
                
            elif bloque_actual == 'paso4':
                data_paso4.append([float(x) for x in line.split(',')])

    data_paso1 = np.array(data_paso1)
    data_paso2 = np.array(data_paso2)
    data_paso4 = np.array(data_paso4)

    return data_paso1, data_paso2, data_paso4
