# Se revisa el concepto de producto interno entre uaa matriz y un vector
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((0, 1, 2, 3)))

def run():

    '''
    El producto interno se obtiene de numpy con la funcion .dot() puesto que tambien es conocido matematicamente como
    producto punto.
    Esta operación consiste en sumar las multiplicaciones de nuestro vector
    [[a b],
    [c d],
    [e f]]
    dot
    [z w]
    =
    [az + bw, cz + dw, ez + fw]
    '''
    escalar = v_rand
    ic(escalar)
    vector = np.array([escalar, escalar + 2, escalar * 2, escalar * 3])
    ic(vector)
    matriz = np.array([vector * 4, vector - 2, vector + 3])
    ic(matriz)
    ic(matriz * vector)
    ic(vector * matriz)
    ic(matriz.dot(vector))
    

if __name__ == '__main__':
    run()