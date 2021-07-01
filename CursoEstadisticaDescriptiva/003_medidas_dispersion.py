from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dir_pandas = './files/{}'

def run():
    df = pd.read_csv(dir_pandas.format('cars.csv'))
    ic(df.info())
    ic(df.describe())
    ic(df.sample(5))

    # Calculo de la desviacion estandar
    desv_std = df['price_usd'].std()
    ic(desv_std)

    # Calculo del rango
    rango = df['price_usd'].max() - df['price_usd'].min()
    ic(rango)

    # Calculo de cuartiles
    # Q2 = mediana
    Q2= df['price_usd'].median()
    ic(Q2)
    # Q1
    Q1= df['price_usd'].quantile(q = 0.25)
    ic(Q1)
    # Q3
    Q3= df['price_usd'].quantile(q = 0.75)
    ic(Q3)
    # Valor mínimo (brazo izquierdo)
    vmin = df['price_usd'].quantile(q = 0)
    ic(vmin)
    # Valor maximo (brazo derecho)
    vmax = df['price_usd'].quantile(q = 1)
    ic(vmax)
    # Rango intercuartil IQR = Q3 - Q1
    IQR = Q3 - Q1
    ic(IQR)
    # Deteccion de outliers (no tenemos datos simetricos, pero asi se calcularian)
    minlimit = Q1 - 1.5 * IQR
    maxlimit = Q1 + 1.5 * IQR
    ic(minlimit)
    ic(maxlimit)

    sns.histplot(df['price_usd'])
    plt.show()
    sns.boxplot(df['price_usd'])
    plt.show()
    sns.boxplot(x = 'engine_fuel', y = 'price_usd', data = df)
    plt.show()


if __name__ == '__main__':
    run()