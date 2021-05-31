import numpy as np
from icecream import ic

def run():
    # Se define una matriz cuadrada
    v1 = np.array(
        [
        [0 , 1, 0, 0],
        [0 , 0, 1, 0],
        [0 , 1, 1, 0],
        [1 , 0, 0, 1]
        ]
    )

    # Con este proceso se buscan autovalores y autovectores
    lambdas, V = np.linalg.eig(v1.T)
    ic(v1)
    ic(lambdas)
    ic(V)

    # Se imprimen lambdas iguales con 0, es decir, la fila que es dependiente dentro de los demas valores de la matriz
    print(v1[lambdas == 0, :])


if __name__ == '__main__':
    run()