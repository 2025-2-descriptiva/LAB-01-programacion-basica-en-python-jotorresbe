"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """

    dict_local = {}
    lista = list()
    for fila in dataset:
        # Se agrega en una misma lista la lista de futuros key-value
        # Ej: ['jjj':'2'] 
        lista.extend(fila[4].split(","))
    
    # Lista de elementos futuro key-values separados:
    # Ej: ['jjj','2']
    test = [row.split(":") for row in lista]
    for registro in test:
        #Si el value no existe lo inicializa en 0
        #Si existe suma +1
        dict_local[registro[0]] = dict_local.get(registro[0], 0) + 1
    
    return dict(sorted(dict_local.items())) #sorted(dict_local.items())
        

print(pregunta_09())


