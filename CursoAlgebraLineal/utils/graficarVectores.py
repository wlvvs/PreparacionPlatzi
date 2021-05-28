import numpy as np
import matplotlib.pyplot as plt

def graficarVectores(vecs, cols, alpha = 1):
    '''
    Los valores de las variables son:
    vecs = recibe los vectores a graficar
    cols = recibe los colores que usaremos para cada vector

    Al generar el vector, concatenamos al mismo la coordenada (0,0)
    Esto nos sirve para indicar el inicio del vector
    La función de plt quiver permite que el vector se dibuje con una flecha
    '''
    plt.figure()
    plt.axvline(x = 0, color = "grey", zorder = 0)
    plt.axhline(y = 0, color = "grey", zorder = 0)
    plt.grid(color = 'black', linestyle = '-', linewidth = 0.5)
    plt.gca().set_aspect("equal")
    
    for i in range(len(vecs)):
        x = np.concatenate([[0,0], vecs[i]])
        plt.quiver([x[0]],
                  [x[1]],
                  [x[2]],
                  [x[3]],
                  angles = 'xy',
                  scale_units = 'xy',
                  scale = 1, 
                  color = cols[i],
                  alpha = alpha)


if __name__ == '__main__':
    graficarVectores()