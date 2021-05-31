import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from icecream import ic

def run():
    vuelos = sns.load_dataset("flights")
    vuelos = vuelos.pivot("month", "year", "passengers")
    ax = sns.heatmap(vuelos)
    plt.show()


if __name__ == '__main__':
    run()