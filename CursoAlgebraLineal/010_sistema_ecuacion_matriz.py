# Se comprueban la propiedad de trasposicion de productos de matrices
import numpy as np
import matplotlib.pyplot as plt
from icecream import ic

def run():

    # Definir intervalos en lso cuales se evaluan nuestras ecuaciones
    # Inicio, fin e intervalo
    x = np.arange(-5, 5, 0.5)
    y_1 = 3 * x + 5
    y_2 = 2 * x + 3

    # Se indica que se debe graficar algo
    plt.figure()
    
    # Se indica que esto se debe graficar, que son justamente los puntos de las funciones
    # y_1 y y_2 evaluadas con los puntos del vector x
    plt.plot(x, y_1)
    plt.plot(x, y_2)

    # Se indica que el eje x debe contemplar en gráfica los valores de nuestro vector, para acotarlo
    plt.xlim(-5, 5)
    plt.ylim(-5 , 5)

    # Se definen los ejes x y y
    plt.axvline(x = 0, color = 'grey')
    plt.axhline(y = 0, color = 'grey')
    plt.show()


if __name__ == '__main__':
    run()