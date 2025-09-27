"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    # Diccionario para almacenar los valores únicos (llaves) y conteos (valores) 
    diccionario_conteos = {}

    for fila in dataset:
        letra = fila[0]
        numero = int(fila[1])
        if letra in diccionario_conteos:
            diccionario_conteos[letra] += numero
        else:
            diccionario_conteos[letra] = numero
    
    # Organizar lista de tuplas por key
    return sorted(diccionario_conteos.items())


pregunta_03()