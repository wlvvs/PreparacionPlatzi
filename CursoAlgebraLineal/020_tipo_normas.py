import numpy as np
import random
from icecream import ic

v_escalar1 = random.randint(-10,10)
v_escalar2 = random.randint(-3,3)

def run():
    vector = np.array([v_escalar1, v_escalar2, v_escalar1 + 3, 0, v_escalar2 -1, 0])
    print('\nNorma L0: Devuelve el número de elementos distintos de 0:')
    ic(vector)
    ic(np.linalg.norm(vector, ord = 0))
    
    print('\nNorma L1: Devuelve la sumatoria de los valores absolutos del vector:')
    ic(vector)
    ic(np.linalg.norm(vector, ord = 1))

    print('\nNorma L2: Devuelve la distancia euclidiana del vector (default):')
    vector = np.array([v_escalar2, v_escalar1])
    ic(vector)
    ic(np.linalg.norm(vector, ord = 2))

    print('\nNorma L2**2: Devuelve el valor del producto interno del vector multiplicado por su traspuesta:')
    print('Representa computacionalmente mejor que el cálculo con manejo de raices cuadradas')
    vector = np.array([v_escalar1, v_escalar2, v_escalar1 + 3, 0, v_escalar2 -1, 0])
    ic(vector)
    ic(np.linalg.norm(vector, ord = 2) ** 2)
    ic(vector.T.dot(vector))

    print('\nNorma L(infinito): Devuelve el valor absoluto mas grande en el vector:')
    vector = np.array([v_escalar1, v_escalar2, v_escalar1 + 3, 0, v_escalar2 -1, 0])
    ic(vector)
    ic(np.linalg.norm(vector, ord = np.inf))


if __name__ == '__main__':
    run()