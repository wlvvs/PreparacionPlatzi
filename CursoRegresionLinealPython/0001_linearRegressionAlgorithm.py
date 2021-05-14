import numpy as np
import matplotlib.pyplot as ptl


def estimate_b0_b1(x, y):
    n = np.size(x)

    # obtenemos los promedios de x y y
    m_x, m_y = np.mean(x), np.mean(y)

    # calcular sumatoria de XY y sumatoria de XX
    sumatoria_xy = np.sum((x - m_x) * (y - m_y))
    sumatoria_xx = np.sum((x * (x - m_x))

    # coeficientes de regresion
    b_1 = sumatoria_xy / sumatoria_xx
    b_0 = m_y - b_1 * m_x

    return(b_0, b_1)

if __name__ =='__main__':
    estimate_b0_b1()