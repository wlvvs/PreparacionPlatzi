# Ejercicio para resolver una regreseion logistica con libreria de apoyo
# Tomando en cuenta la forma de la flor de iris, se desarrolla un algoritmo para determinanr las medidas de la misma con respecto a su fisonomia
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from icecream import ic

def run():
    atrib_names = ['sepal length', 'sepal width', 'petal length', 'petal width']
    X, y = load_iris(return_X_y=True)
    clf = LogisticRegression(random_state=10, solver='liblinear').fit(X[:100], y[:100])
    model_coefs = pd.DataFrame(clf.coef_, columns=atrib_names)
    ic(model_coefs)


if __name__ == '__main__':
    run()
