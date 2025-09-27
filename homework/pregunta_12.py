"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    dict_values = dict()

    for linea in dataset:
        # Los splits y el index [1] es para obtener una lista de números
        # input: fff:3,hhh:1,ddd:2 - output: [3,1,2]
        col_1, col_2 = linea[0], linea[4].split(",")
        
        col_2 = [int(row.split(":")[1]) for row in col_2]

        dict_values[col_1] = dict_values.get(col_1, 0) + sum(col_2) 
        
    return dict(sorted(dict_values.items()))

pregunta_12()

