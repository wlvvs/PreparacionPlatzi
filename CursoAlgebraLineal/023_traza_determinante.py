import numpy as np
from icecream import ic
import matplotlib.pyplot as plt
import importlib.util

def run():
    spec = importlib.util.spec_from_file_location('graficarVectores', './utils/graficarVectores.py')
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)

    matriz = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ])

    ic(matriz)
    ic(np.trace(matriz))

    v1 = np.array([0, 1])
    v2 = np.array([1, 0])
    a = np.array([
         [2, 0],
         [0, 2]
    ])

    ic(v1)
    ic(v2)
    ic(a)
    v1_t = a.dot(v1)
    v2_t = a.dot(v2)
    ic(v1_t)
    ic(v2_t)

    area_t = abs(v1_t[0] - v2_t[0]) * abs(v1_t[1] - v2_t[1])
    ic(area_t)

    a_new = a * [-1, 1]
    ic(a_new)
    
    # Determinantes
    ic(np.linalg.det(a))
    ic(np.linalg.det(a_new))

    # Transformación al multiplicar por el nuevo vector
    v1_t1 = a_new.dot(v1)
    v2_t2 = a_new.dot(v2)
    ic(v1_t1)
    ic(v2_t2)

    foo.graficarVectores([v1, v2, v1_t, v2_t, v1_t1, v2_t2], ['blue', 'red', 'green', 'orange', 'pink', 'black'])
    plt.xlim(-3, 3)
    plt.ylim(-1, 3)
    plt.show()


if __name__ == '__main__':
    run()