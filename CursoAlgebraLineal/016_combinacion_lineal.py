# Muestra de combinacion lineal de vectores con escalares consecutivos generados por un loop
import numpy as np
import random
from icecream import ic
import matplotlib.pyplot as plt

v_escalar1 = int(random.choice((1, 2, 3)))
v_escalar2 = int(random.choice((2, 4)))

def run():

    vector1 = np.array([v_escalar1, v_escalar1 + v_escalar2])
    vector2 = np.array([v_escalar2 + v_escalar1, v_escalar2])
    ic(vector1)
    ic(vector2)
    
    for a in range (-11, 11):
        for b in range (-11, 11):
            plt.scatter(vector1[0] * b + vector2[0] * a, vector1[1] * b + vector2[1] * a,
            marker = '.',
            color = 'green')
    
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)
    plt.axvline(x = 0, color = "grey", zorder = 0)
    plt.axhline(y = 0, color = "grey", zorder = 0)
    plt.grid(color = 'black', linestyle = '-', linewidth = 0.5)
    plt.show()


if __name__ == '__main__':
    run()