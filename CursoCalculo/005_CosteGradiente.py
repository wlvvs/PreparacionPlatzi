from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt

res = 100 # Resolución de gráfica
h = 0.01 # Incremento del punto
lr = 0.01 # Learning rate

def f(x, y):
  return np.tanh(x) + 2 * np.cos(y)** 3

# Se define una funcion para ejecutar la derivada
def derivate(_p, p):
  return (f(_p[0], _p[1]) - f(p[0], p[1])) / h


# Se define una funcion para encontrar el gradiente, recibiendo el punto anteriormente calculado
def gradiente(p):
  # Vector lleno de ceros para calcular el recorrido del punto
  grad = np.zeros(2)
  # Se requiere iterar esos componentes con respecto al punto
  for idx, val in enumerate(p):
    _p = np.copy(p)
    # Se agrega el incremento h en mi copia de punto. Si vale 0, se agrega a x, si vale 1, a Y
    _p[idx] = _p[idx] + h;

    # Se calcula la derivada parcial del punto.
    # Recibe como entrada el punto de la copia y el punto original
    dp = derivate(_p, p)
    # Se guardan los resultados de la derivada parcial en el vector de ceros con el índice correspondiente del for ACTUAL
    # Una vez terminada la iteración, se regresa dicho valor
    grad[idx] = dp
  return grad


def run():
    # Se definen los vectores a graficar
    x = np.linspace(-4, 4, num = res)
    y = np.linspace(-4, 4, num = res)

    x, y = np.meshgrid(x, y) # Genera los pares ordenados con respecto a los vectores declarados
    z = f(x, y)

    fig, ax = plt.subplots(subplot_kw={"projection" : "3d"}) # Se define el modo de graficación, en este caso, proyección en 3D

    surf = ax.plot_surface(x, y, z, cmap = cm.hsv) # Se imprime la superficie. El ultimo parametro da código de color
    fig.colorbar(surf) # Imprime una barra de color para representar las zonas con respecto a valores

    fig2, ax2 = plt.subplots()
    level_map = np.linspace(np.min(z), np.max(z), num = res) # Genera un vector con los valores minimos y maximos de la combinacion
    cp = ax2.contour(x, y, z, levels = level_map, cmap = cm.hsv) # 
    #cp2 = ax2.contourf(x, y, z, levels = level_map, cmap = cm.hsv) # 

    fig2.colorbar(cp) # Imprime las curvas de nivel con los huecos que pudieran formarse gracias a la resolucion
    #fig2.colorbar(cp2) # Imrpime las curvas de nivel con el mapa lleno en totalidad

    # Considerando los rangos máximos y mínimos de 0 y 1, con esa operación aseguramos que salga el -4 y 4, que son los valores que definimos dentro de los vectores
    p = np.random.rand(2) * 8 - 4
    plt.plot(p[0], p[1], 'o', c= 'r')

    # Se define el proceso iterativo del gradiente
    for i in range(1000):
    # Se asigna el valor de p como p menos el learning rate multiplicado por el gradiente que calculamos con el proceso de derivadas parciales
        p = p - lr * gradiente(p)
    # Con esto, pintamos el punto cada 10 iteraciones
        if (i % 10 == 0):
            plt.plot(p[0], p[1], 'o', c= 'b')

    plt.plot(p[0], p[1], 'o', c= 'w')
    print('El punto mínimo esta en: ',p)

    plt.show()


if __name__ == '__main__':
    run()