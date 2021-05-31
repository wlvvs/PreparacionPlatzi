import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

def run():
    np.set_printoptions(suppress=True)

    matriz = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    ic(matriz)
    # Se realiza el proceso del vector de la primer columna por el producto interno con la segunda 
    # Todo esto para analisis de filas
    # v1 ortogonal v2
    ic(matriz[:,0].dot(matriz[:,1]))
    # v1 ortogonal v3
    ic(matriz[:,0].dot(matriz[:,2]))
    # v2 ortogonal v3
    ic(matriz[:,1].dot(matriz[:,2]))

    # Resta validar la norma vector a vector (1, 2, 3)
    ic(np.linalg.norm(matriz[:,0]))
    ic(np.linalg.norm(matriz[:,1]))
    ic(np.linalg.norm(matriz[:,2]))

    # Todo esto para analisis de columnas
    # v1 ortogonal v2
    ic(matriz[0,:].dot(matriz[1,:]))
    # v1 ortogonal v3
    ic(matriz[0,:].dot(matriz[2,:]))
    # v2 ortogonal v3
    ic(matriz[1,:].dot(matriz[2,:]))
    # Resta validar la norma vector a vector (1, 2, 3)
    ic(np.linalg.norm(matriz[0,:]))
    ic(np.linalg.norm(matriz[1,:]))
    ic(np.linalg.norm(matriz[2,:]))

    # Generar matrices ortogonales
    a = np.array([
        [np.cos(100), - np.sin(100)],
        [np.sin(100), np.cos(100)]])
    
    ic(a)
    # Derivado de la presición de calculo, esto deberia dar 1, sin embargo, da un valor muy proximo a 1
    ic(np.linalg.norm(a[0,:]))
    ic(np.linalg.norm(a[1,:]))
    ic(np.linalg.norm(a[:,0]))
    ic(np.linalg.norm(a[:,1]))
    # Con esto, corroboramos que en verdad es ortogonal la matriz
    ic(a[0,:].dot(a[1,:]))
    ic(a[:,0].dot(a[:,1]))
    ic(a.T)
    ic(a.T.dot(a))
    ic(a.dot(a.T))
    ic(np.linalg.inv(a))
    ic(1/a.T.dot(a))

if __name__ == '__main__':
    run()