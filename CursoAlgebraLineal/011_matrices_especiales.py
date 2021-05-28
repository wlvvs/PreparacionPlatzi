# Se revisan temas de matrices especiales
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((1, 2, 3, 4, 5, 6)))

def run():

    # Esta función regresa una matriz de la dimensión especificada con ceros y unos
    # El 1 recorre del principio al fin de manera diagonal y todos los valores se
    # generan como flotantes. Esto es la matriz identidad
    identidad = np.eye(3)
    ic(identidad)

    escalar = v_rand
    ic(escalar)
    vector = np.array([escalar, escalar * 2, escalar * 3])
    ic(vector)
    matriz_a = np.array([[1,0,1],[0,0,1],[1,1,1]])
    
    ic(identidad.dot(vector))
    ic(matriz_a)
    inversa_matriz_a = np.linalg.inv(matriz_a)
    ic(inversa_matriz_a)
    

if __name__ == '__main__':
    run()