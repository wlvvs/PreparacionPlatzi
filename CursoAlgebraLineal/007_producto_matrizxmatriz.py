# Se revisa el concepto de producto interno entre dos matrices
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((3, 7, 11, 2)))

def run():

    escalar = v_rand
    ic(escalar)
    vector = np.array([escalar, escalar * 2, escalar * 3])
    ic(vector)
    matriz_a = np.array([vector * 4, vector - 2, vector + 3, vector - 1])
    matriz_b = np.array([vector * 4, vector + 3])
    matriz_b = matriz_b.T
    '''
    El producto interno de matrices es tal que el número de filas de la primera matriz debe ser
    igual al número de columnas de la segunda matriz El proceso de multiplicacion se realiza 
    de la forma conocida, que es, la suma de multiplicaciones de la fila 1 de la primera matriz
    multiplicado por la columna 1 de la segunda matriz, teniendo como resultado una matriz
    de dimensiones igual al numero de columnas de la primera matriz por el numero de filas de 
    la segunda matriz
    '''
    ic(matriz_a)
    ic(matriz_a.shape)
    ic(matriz_b)
    ic(matriz_b.shape)
    print('')
    print('')
    ic(matriz_a.dot(matriz_b))


if __name__ == '__main__':
    run()