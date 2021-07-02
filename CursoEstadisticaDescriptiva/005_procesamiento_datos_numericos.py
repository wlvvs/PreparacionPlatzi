from icecream import ic
from matplotlib import scale
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import timeit
from sklearn import datasets, linear_model

dir_pandas = './files/{}'

def run():

    def train_raw():
        linear_model.LinearRegression().fit(raw, y)
    
    def train_scaled():
        linear_model.LinearRegression().fit(scaled, y)
    
    def train_z():
        linear_model.LinearRegression().fit(nz, y)
    
    """
    En este paso, preparamos el dataset que vamos a usar para probar la parte
    de preprocesamiento
    
    """
    X, y = datasets.load_diabetes(return_X_y = True)
    raw = X[:, None, 2]
    ic(X.shape)
    ic(y.shape)
    ic(raw.shape)
    ic(raw[0])
    ic(raw[441])
    ic(raw[220])

    """
    Se usara el método de máximos mínimos para realizar el proceso de
    normalizacion - escalamiento y tambien z-score
    
    """
    max_raw = max(raw)
    min_raw = min(raw)
    meanz = raw.mean()
    stdevz = raw.std()
    scaled = (2 * raw - max_raw - min_raw) / (max_raw - min_raw)
    nz = (raw - meanz) / stdevz
    ic(max_raw, min_raw)
    ic(meanz, stdevz)
    ic(scaled.shape)
    ic(scaled[0])
    ic(scaled[441])
    ic(scaled[220])
    ic(nz.shape)
    ic(nz[0])
    ic(nz[441])
    ic(nz[220])

    """
    Al graficar los histogramas, se aprecia como la normalizacion afecta
    la forma de la distribucion de valores
    
    """
    fig, axs = plt.subplots(3, 1, sharex = True)
    axs[0].hist(raw)
    axs[1].hist(scaled)
    axs[2].hist(nz)
    plt.show()

    raw_time = timeit.timeit(train_raw, number = 300)
    ic(raw_time)
    scaled_time = timeit.timeit(train_scaled, number = 300)
    ic(scaled_time)
    z_time = timeit.timeit(train_z, number = 300)
    ic(z_time)


    """
    Analizando un origen de datos con transformación no lineal
    
    """
    df = pd.read_csv(dir_pandas.format('cars.csv'))
    ic(df.info())
    ic(df.sample(5))

    df.price_usd.hist()
    plt.show()
    df.price_usd.apply(lambda x: np.tanh(x)).hist()
    plt.show()
    df.price_usd.apply(lambda x: np.tanh(x / 10000)).hist()
    plt.show()


if __name__ == '__main__':
    run()