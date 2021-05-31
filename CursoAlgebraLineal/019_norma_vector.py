
import numpy as np
import random
import seaborn as sns
import matplotlib.pyplot as plt
from icecream import ic

v_escalar1 = int(random.choice((1, 2, 3)))
v_escalar2 = int(random.choice((2, 4)))

def run():

    vector1 = np.array([v_escalar1, v_escalar1 + v_escalar2])
    vector2 = np.array([v_escalar2 + v_escalar1, v_escalar2])
    ic(vector1)
    ic(vector2)
    ic(np.linalg.norm(vector1))
    ic(np.linalg.norm(vector2))
    ic(np.linalg.norm(vector1) + np.linalg.norm(vector2))
    ic(vector1 + vector2)
    vector = vector1 + vector2
    vector = np.linalg.norm(vector)
    ic(vector)

    # Se realiza el ejemplo gráfico de desigualdad triangular

    v1 = np.array([0, 0, 2, 7])
    v2 = np.array([0, 0, 3, 5])

    # Se extraen los componentes que salen del origen para formar un vector auxiliar
    v1_aux = np.array([v1[2], v1[3], v2[2], v2[3]])
    v1v2 = np.array([0, 0, 5, 12])

    plt.quiver(
        [v1[0], v1_aux[0], v1v2[0]],
        [v1[1], v1_aux[1], v1v2[1]],
        [v1[2], v1_aux[2], v1v2[2]],
        [v1[3], v1_aux[3], v1v2[3]],
        angles = 'xy',
        scale_units = 'xy',
        scale = 1,
        color = sns.color_palette()
    )
    
    plt.xlim(-0.5, 6)
    plt.ylim(-0.5, 15)
    plt.show()


if __name__ == '__main__':
    run()