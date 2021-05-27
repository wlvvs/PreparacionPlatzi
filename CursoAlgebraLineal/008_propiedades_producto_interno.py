# Se comprueban las propiedades del producto interno
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((1, 2, 3, 4, 5, 6)))

def run():

    escalar = v_rand
    ic(escalar)
    vector = np.array([escalar, escalar + 1])
    ic(vector)
    matriz_a = np.array([vector, vector + 2, vector + 4])
    matriz_b = np.array([vector * 2, vector * 4])
    matriz_c = np.array([vector * 5, vector * 3])
    matriz_b = matriz_b.T
    matriz_c = matriz_c.T
    ic(matriz_a)
    ic(matriz_b)
    ic(matriz_c)
    
    print('')
    print('Propiedad asociativa')
    print('')
    ic(matriz_a.dot(matriz_b.dot(matriz_c)))
    ic(matriz_a.dot(matriz_b).dot(matriz_c))

    print('')
    print('Propiedad distributiva')
    print('')
    ic(matriz_a.dot(matriz_b + matriz_c))
    ic(matriz_a.dot(matriz_b) + matriz_a.dot(matriz_c))

    print('')
    print('Propiedad conmutativa')
    print('')
    ic(matriz_b.dot(matriz_c))
    ic(matriz_c.dot(matriz_b))


if __name__ == '__main__':
    run()