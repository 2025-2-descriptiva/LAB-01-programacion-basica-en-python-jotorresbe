# Creando una función que abre el dataset


RUTA = 'files/input/data.csv'
# Definimos los separadores de nuestro dataset 
PATRON = '[\t]|;|:|,|[\r]'

'''def abridor():
    lista = list()
    with open(RUTA, newline='') as dataset:
        for linea in dataset:
            # Agregamos cada arreglo a una posición de la lista
            lista.append(re.split('[\t]|;|:|,|[\r]', linea))
        return lista'''

def abridor():
    lista = list()
    with open(RUTA, newline='') as dataset:
        for linea in dataset:
            lista.append(linea.strip().split('\t'))
        return lista


DATASET_LISTO = abridor()

