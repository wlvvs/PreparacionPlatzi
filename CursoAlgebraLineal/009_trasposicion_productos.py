# Se comprueban la propiedad de trasposicion de productos de matrices
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
    matriz_b = matriz_b.T
    ic(matriz_a)
    ic(matriz_b)
    
    '''
    Aqui se comprueba que (A.dot(B)).T = (B.T).dot((A).T)
    '''
    print('')
    ic((matriz_a.dot(matriz_b)).T)
    ic(matriz_b.T.dot(matriz_a.T))


if __name__ == '__main__':
    run()