"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
from homework.funciones_generales import DATASET_LISTO
dataset = DATASET_LISTO

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
    lista = []
    for registro in test:
        #Si el value no existe, lo agrega con un append
        # El resultado será un key, [lista]
        dict_local[registro[0]] = dict_local.get(registro[0], []) + [int(registro[1])]
        
    
    for claves, valores in dict_local.items():
        # Agregando en la forma lista de tuplas
        lista.append((claves, min(valores),max(valores)))
    
    return sorted(lista)

pregunta_06()