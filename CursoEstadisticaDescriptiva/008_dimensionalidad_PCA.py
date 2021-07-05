from icecream import ic
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def run():
    iris = sns.load_dataset('iris')
    ic(iris.info())
    ic(iris.sample(5))
    scaler = StandardScaler()
    scaled = scaler.fit_transform(iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values)
    ic(scaled[0], scaled[1], scaled[2])

    covariance_matrix = np.cov(scaled.T)
    ic(covariance_matrix)
    sns.pairplot(iris)
    plt.show()

    sns.jointplot(x = iris['petal_length'], y = iris['petal_width'])
    sns.jointplot(x = scaled[:, 2], y = scaled[:, 3])
    plt.show()

    eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
    ic(eigen_values)
    ic(eigen_vectors)

    variance_explain = []
    for i in eigen_values:
        variance_explain.append((i / sum(eigen_values)) * 100)
    ic(variance_explain)

    pca = PCA(n_components = 2)
    pca.fit(scaled)
    ic(pca.explained_variance_ratio_)
    reduced_scale = pca.transform(scaled)
    ic(reduced_scale[0], reduced_scale[1], reduced_scale[2])
    iris['pca_1'] = reduced_scale[:,0]
    iris['pca_2'] = reduced_scale[:,1]
    ic(iris.sample(5))

    sns.jointplot(x = iris['pca_1'], y = iris['pca_2'], hue = iris['species'])
    plt.show()


if __name__ == '__main__':
    run()