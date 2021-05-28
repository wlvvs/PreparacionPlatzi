# Se revisan sistemas sin solución, con una solución y con soluciones infinitas
import numpy as np
import random
import matplotlib.pyplot as plt
from icecream import ic

v_rand = int(random.choice((1, 2, 3, 4, 5, 6)))

def run():

    opcion = input('''\nIndica que tipo de sistema quieres ver:
    (1) Sistemas sin solución
    (2) Con una solución
    (3) Soluciones infinitas    :''')
    # Declaramos el vector de rangos de valores
    x = np.arange(-6, 6)

    # Se declaran las funciones que serviran de ejemplo para un sistema sin soluciones
    y1 = 3 * x +5
    y2 = -x + 3
    y3 = 2 * x + 1
    
    plt.figure()
    if int(opcion) ==1:
        plt.plot(x, y1)
        plt.plot(x, y2)
        plt.plot(x, y3)
        print('El sistema es indeterminado porque hay mas soluciones que incógnitas')
    elif int(opcion) ==2:
        plt.plot(x, y1)
        plt.plot(x, y2)
        print('El sistema es compatible determinado, converge en un solo punto')
    else:
        plt.plot(x, y3)
        print('Hay soluciones infinitas, ya que las incógnitas superan a las ecuaciones')

    plt.xlim(-8, 8)
    plt.ylim(-8, 8)

    plt.axvline(x = 0, color = 'grey')
    plt.axhline(y = 0, color = 'grey')
    plt.show()


if __name__ == '__main__':
    run()