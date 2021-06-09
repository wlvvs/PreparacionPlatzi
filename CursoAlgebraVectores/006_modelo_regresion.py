import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from icecream import ic

def pred(x):
    beta = np.array([6.55490348 * np.exp(0.2), -5.75918372 * np.exp(0.2), -2.94216316*np.exp(-0.1)])
    v = 4152.02
    return x@(beta + v)


def run():
    df = pd.read_csv('./files/income_db_gorg.csv')
    X = df[['Lat', 'Lon', 'Zip_Code']].values
    Y_hat = pred(X)
    Y = df['Mean'].values

    fig, ax = plt.subplots(1, 1, figsize = (7, 7), dpi = 120)

    ax.scatter(Y_hat, Y, marker = 'o', color = 'red')
    ax.plot(Y, Y, ls = '--')
    plt.show()


if __name__ == '__main__':
    run()