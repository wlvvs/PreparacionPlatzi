# Ejercicio para definir una regreseion logistica
from mpl_toolkits.mplot3d import Axes3D # Libreria para graficos tridimensionales
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns

def likelihood(y, yp):
    return yp * y + (1 - yp) * (1 - y)


def run():
    # Se define un objeto tipo figura
    fig = plt.figure()
    # Se define una variable de eje en donde se extrae el parametro gca de una proyeccion 3d
    #ax = fig.gca(projection = '3d') Esta instruccion aparece como deprecada, se usa la sugerencia de python
    ax = plt.axes(projection = '3d')

    # Se declaran valores de Y y YP que van entre 0 y 1 con intervalos de 0.01
    Y = np.arange(0, 1, 0.01)
    YP = np.arange(0, 1, 0.01)

    # Se genera una malla con los valores de los rangos de Y y YP
    Y, YP = np.meshgrid(Y, YP)
    # Se calculan los elementos para cada valor de la malla
    Z = likelihood(Y, YP)

    # Se grafica la superficie, incluyendo los ejes x, y y z
    surf = ax.plot_surface(Y, YP, Z, cmap = cm.coolwarm)
    fig.colorbar(surf, shrink = 0.5, aspect = 5)
    plt.show()


if __name__ == '__main__':
    run()