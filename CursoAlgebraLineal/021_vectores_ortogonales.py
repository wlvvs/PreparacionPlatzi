import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from icecream import ic

def run():
    x = np.array([0, 0, 2, 2])
    y = np.array([0 , 0, 2, -2])

    ic(x)
    ic(y)

    plt.quiver(
        [x[0], y[0]],
        [x[1], y[1]],
        [x[2], y[2]],
        [x[3], y[3]],
        angles = 'xy',
        scale_units = 'xy',
        scale = 1,
        color = sns.color_palette()
    )
    plt.xlim(-2 , 4)
    plt.ylim(-3, 3)

    x = np.array([[2, 2]])
    y = np.array([[2, -2]])
    ic(x)
    ic(y)
    ic(x.dot(y.T))
    ic(np.linalg.norm(x))
    ic(np.linalg.norm(y))

    x = np.array([[1, 0]])
    y = np.array([[0, -1]])
    ic(x)
    ic(y)
    ic(x.dot(y.T))
    ic(np.linalg.norm(x))
    ic(np.linalg.norm(y))
    plt.show()

    
if __name__ == '__main__':
    run()