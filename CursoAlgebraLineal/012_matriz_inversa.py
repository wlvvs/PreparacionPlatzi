# Solucion de sistema de ecuaciones con matriz inversa
import numpy as np
import random
from icecream import ic

v_rand = int(random.choice((3, 7, 1, 2, 7)))

def run():

    # Permite mostrar resultados muy próximos a cero
    np.set_printoptions(suppress = True)
    print('')

    escalar = v_rand
    ic(escalar)
    print('')
    vector = np.array([escalar, escalar * 2])
    ic(vector)
    print('')
    # Se define una matriz de dimension 2, que representa los coeficientes de nuestras variables
    matriz = np.array([vector, vector + 2])
    ic(matriz)
    print('')

    # Se define un vector con los resultados de nuestro sistema de ecuaciones
    vector2 = np.array([escalar * 3, escalar - 1])
    ic(vector2)
    print('')
    # Generamos la inversa de la matriz que corresponde a los coeficientes de las variables
    inv_matriz = np.linalg.inv(matriz)
    ic(inv_matriz)
    print('')

    # Se realiza el producto interno de la inversa con respecto al vector de resultados
    # Esto regresa el valor de x, que es solución del sistema de ecuaciones
    x = inv_matriz.dot(vector2)
    ic(x)


if __name__ == '__main__':
    run()