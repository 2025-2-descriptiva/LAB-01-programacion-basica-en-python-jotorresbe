"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    dict_values = dict()
    for linea in dataset:
        numero, comb = linea[1], linea[3].split(",")
        # Iteramos sobre cada caracter de la columna 4
        # Para acumular sobre él el valor de la fila
        for caracter in comb:
            # Sumamos a cada caracter el valor de la columna 2
            dict_values[caracter] = dict_values.get(caracter, 0) + int(numero)
    return dict(sorted(list(dict_values.items())))


print(pregunta_11())
