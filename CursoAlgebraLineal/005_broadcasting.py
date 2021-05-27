# Se revisa el concepto de broasdcasting, para suma de vectores y matrices de diferentes dimensiones
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((0, 1, 2, 3)))

def run():

    escalar = v_rand
    ic(escalar)
    vector = np.array([escalar, escalar + 2, escalar * 2, escalar * 3])
    ic(vector)
    
    matriz = np.array([vector * 4, vector - 2, vector + 3])
    matriz = matriz.T
    ic(matriz)
    ic(matriz.T)
    ic(matriz.T + vector)


if __name__ == '__main__':
    run()