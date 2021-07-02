from itertools import groupby
from icecream import ic
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def run():
    df_iris = sns.load_dataset('iris')
    ic(df_iris.info())
    ic(df_iris.describe())
    ic(df_iris.sample(5))

    # Grafico de dispersion
    sns.scatterplot(data = df_iris, x = 'sepal_length', y = 'petal_length', hue = 'species', palette = 'hls')
    plt.show()

    sns.jointplot(data = df_iris, x = 'sepal_length', y = 'petal_length', hue = 'species', palette = 'hls')
    plt.show()

    sns.jointplot(data = df_iris, x = 'sepal_width', y = 'petal_width', hue = 'species', palette = 'hls')
    plt.show()

    sns.boxplot(y = 'species', x = 'sepal_width', data = df_iris, palette = 'hls')
    plt.show()

    sns.barplot(y = 'species', x = 'sepal_width', data = df_iris, palette = 'hls')
    plt.show()
    
    sns.barplot(y = 'species', x = 'sepal_width', data = df_iris, estimator = np.median, palette = 'hls')
    plt.show()


if __name__ == '__main__':
    run()