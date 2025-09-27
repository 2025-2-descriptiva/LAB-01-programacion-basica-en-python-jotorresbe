"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    dict_tuplas = {}
    lista_numeros = []
    for fila in dataset:
        letra, valores = fila[0], fila[1]
        # Estoy haciendo un diccionario cuyas claves son letras
        # Los valores están almacenados en una lista
        # Ej: {'Z': [1,5,7,3]}
        dict_tuplas[letra]= dict_tuplas.get(letra,[]) + [int(valores)]
    for key, value in dict_tuplas.items():
        lista_numeros.append((key, max(value), min(value)))
    
    return sorted(lista_numeros)


pregunta_05()

