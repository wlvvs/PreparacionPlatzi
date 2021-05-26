# Se revisa el concepto de dimension
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
from numpy.core.fromnumeric import size

'''
Shape da la dimensión de la variable. El primer valor es el numero de elementos que contiene, el segundo el numero de filas y el tercero, numero de columnas
Len da la longitud de la variable en su primer columna
size da la cantidad total de elementos en la variable
Aqui se nota claramente el error por el cual squeeze fue necesario, ya que ese espacio me estaba agregando una dimensión a mi variable de tensor.
Pero por que??
'''

ic.configureOutput(includeContext=True)

def run():
    # Por definición, un escalar carece de dimensión, por lo que tanto len como shape me retornan un error
    escalar = 2
    ic(escalar)

    vector = np.array([escalar, escalar + 1])
    ic(vector)
    # Shape dice que vector tiene 3 escalares, sin filas ni columnas
    vector_s = vector.shape
    vector_l = len(vector)
    vector_z = size(vector)
    ic(vector_s)
    ic(vector_l)
    ic(vector_z)

    matriz = np.array([vector * 4, vector * 3, vector + 10, vector])
    ic(matriz)
    # Shape dice que tiene 4 vectores, cada vector con 4 filas y 2 columnas
    matriz_s = matriz.shape
    matriz_l = len(matriz)
    matriz_z = size(matriz)
    ic(matriz_s)
    ic(matriz_l)
    ic(matriz_z)

    tensor = np.array([[matriz * 3], [matriz * 2]])
    ic(tensor)
    tensor_s = tensor.shape
    tensor_l = len(tensor)
    tensor_z = size(tensor)
    ic(tensor_s)
    ic(tensor_l)
    ic(tensor_z)

    tensor_squeeze = tensor.squeeze()
    ic(tensor_squeeze)
    # -Shape dice que tiene 2 matrices, cada matriz de 4 filas y 2 columnas
    tensor_squeeze_s = tensor_squeeze.shape
    tensor_squeeze_l = len(tensor_squeeze)
    tensor_squeeze_z = size(tensor_squeeze)
    ic(tensor_squeeze_s)
    ic(tensor_squeeze_l)
    ic(tensor_squeeze_z)


if __name__ == '__main__':
    run()