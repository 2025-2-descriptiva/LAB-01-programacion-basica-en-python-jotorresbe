"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

# Importamos librería Re para utilizar expresiones regulares
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    # Inicializamos variable contador para acumular los valores de la segunda columna
    acumulador = 0
    
    # Abrimos el dataset
    for fila in dataset:
        acumulador+=int(fila[1])
    return acumulador
            
pregunta_01()