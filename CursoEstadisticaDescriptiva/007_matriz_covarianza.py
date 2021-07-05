from icecream import ic
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def run():
    iris = sns.load_dataset('iris')
    ic(iris.info())
    ic(iris.sample(5))

    sns.pairplot(iris)
    plt.show()

    sns.pairplot(iris, hue = 'species')
    plt.show()

    scaler = StandardScaler()
    scaled = scaler.fit_transform(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])
    ic(scaled[0], scaled[1], scaled[2])

    covariance_matrix = np.cov(scaled.T)
    ic(covariance_matrix)

    plt.figure(figsize = (10,10))
    sns.set(font_scale = 1.5)
    hm = sns.heatmap(
        covariance_matrix,
        cbar = True,
        annot = True,
        square = True,
        fmt = '.2f',
        annot_kws = {'size': 12},
        yticklabels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
        xticklabels = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    )
    plt.show()

    sns.heatmap(iris.corr(), annot = True)
    plt.show()


if __name__ == '__main__':
    run()