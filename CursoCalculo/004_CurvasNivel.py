from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
  return np.sin(x) + 2 * np.cos(y)

def run():
    res = 100 # Resolución de gráfica

    # Se definen los vectores a graficar
    x = np.linspace(-4, 4, num = res)
    y = np.linspace(-4, 4, num = res)

    x, y = np.meshgrid(x, y) # Genera los pares ordenados con respecto a los vectores declarados
    z = f(x, y)

    fig, ax = plt.subplots(subplot_kw={"projection" : "3d"}) # Se define el modo de graficación, en este caso, proyección en 3D

    surf = ax.plot_surface(x, y, z, cmap = cm.seismic) # Se imprime la superficie. El ultimo parametro da código de color
    fig.colorbar(surf) # Imprime una barra de color para representar las zonas con respecto a valores

    fig2, ax2 = plt.subplots()
    level_map = np.linspace(np.min(z), np.max(z), num = res) # Genera un vector con los valores minimos y maximos de la combinacion
    cp = ax2.contour(x, y, z, levels = level_map, cmap = cm.seismic) # 
    cp2 = ax2.contourf(x, y, z, levels = level_map, cmap = cm.seismic) # 

    fig2.colorbar(cp) # Imprime las curvas de nivel con los huecos que pudieran formarse gracias a la resolucion
    fig2.colorbar(cp2) # Imrpime las curvas de nivel con el mapa lleno en totalidad

    plt.show()


if __name__ == '__main__':
    run()