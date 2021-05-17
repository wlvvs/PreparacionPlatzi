import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    n = np.size(x)

    # obtenemos los promedios de x y y
    m_x, m_y = np.mean(x), np.mean(y)

    # calcular sumatoria de XY y sumatoria de XX
    sumatoria_xy = np.sum((x - m_x) * (y - m_y))
    sumatoria_xx = np.sum(x * (x - m_x))

    # coeficientes de regresión
    '''
    El concepto de b_1 se comprende como el valor de la ecuación completa
    para calcular los mínimos cuadrados:
    '''
    
    b_1 = sumatoria_xy / sumatoria_xx
    
    '''
    El concepto de b_0 se comprende como el despeje de la ecuación de
    mínimos cuadradoos dentro de la función de la pendiente, que es:
    y = b0 + b1(x)
    b0 = y - b1(x)
    '''
    b_0 = m_y - b_1 * m_x

    return(b_0, b_1)

# Funcion de graficado
def plot_regression(x, y, b):

    plt.scatter(x, y, color = "b", marker = "o", s = 30)

    y_pred = b[0] + b[1] * x
    plt.plot(x, y_pred, color="r")

    #Etiquetado
    plt.xlabel('x - Independiente')
    plt.ylabel('y - Dependiente')

    plt.show()

#Codigo MAIN
def main():
    #DATASET
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 6, 5])

    #Obtenemos b1 y b2
    b = estimate_b0_b1(x, y)
    print("Los valores b0 = {}, b1 ={}".format(b[0], b[1]))

    #Graficamos nuestra linea de regresion
    plot_regression(x, y, b)


if __name__== "__main__":
    main()