"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO
def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    # Diccionario para almacenar los valores únicos (llaves) y conteos (valores) 
    diccionario_conteos = {}
    # Lista de comprensión para obtener la primera columna (porque estoy usando un lista de listas)
    primera_columna = [row[0] for row in dataset]
    # Ordenando alfabéticamente
    primera_columna.sort()

    '''
    Bucle para asignar la clave (letra) y con su respectivo valor. 
    Si no encuentra la clave, el valor será 1 (primera vez)
    Si la encuentra, acumula 1 
    ''' 
    for letra in primera_columna:
        diccionario_conteos[letra] = diccionario_conteos.get(letra,0)+1
    
    # Retorna lista de tuplas
    return list(diccionario_conteos.items())


pregunta_02()


