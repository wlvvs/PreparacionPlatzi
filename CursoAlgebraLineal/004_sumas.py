# Se revisa el concepto de suma de vectores y escalares
import numpy as np
from icecream import ic

def run():

    escalar = 3
    ic(escalar)
    vector1 = np.array([escalar, escalar + 1, escalar * 4, escalar - 3])
    vector2 = np.array([escalar, escalar + 2, escalar * 2, escalar - 2])
    vector = vector1 + vector2
    ic(vector1)
    ic(vector2)
    ic(vector)
    
    matriz1 = np.array([vector1 * 4, vector2 * 3, vector1 + 10])
    matriz2 = np.array([vector2 * 4, vector1 * 3, vector2 + 10])
    matriz = matriz1 + matriz2
    ic(matriz1)
    ic(matriz2)
    ic(matriz)

    tensor1 = np.array([[matriz1 * 3], [matriz2 * 2]])
    tensor1 = tensor1.squeeze()
    tensor2 = np.array([[matriz2 * 2], [matriz1 - 1]])
    tensor2 = tensor2.squeeze()
    tensor = tensor1 + tensor2
    ic(tensor1)
    ic(tensor2)
    ic(tensor)


if __name__ == '__main__':
    run()