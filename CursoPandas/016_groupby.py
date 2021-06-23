from icecream import ic
from numpy.ma import count
import pandas as pd
import numpy as np
import seaborn as sns

def mean_kilos(x):
    return np.mean(x) / 1000


def f_filter(x):
    return mean_kilos(x['price']) > 4


def run():
    """
    La funcion de agrupacion dentro de pandas permite generar un conjuto de
    datos acotado con respecto a uno o mas columnas del dataframe con el fin
    de operar y filtrar bajo ese subconjunto

    """
    df = sns.load_dataset('diamonds')
    dict_agg = {
        'carat': [min, max, count],
        'price': [np.mean, mean_kilos]}

    ic(df)
    ic(df.groupby('cut').mean()) # Agrupando por cut, se genera el promedio de los campos restantes
    ic(df.groupby('cut').median())
    ic(df.groupby('cut')['price'].mean()) # Agrupando por cut, se genera el promedio del campo price

    """
    El ciclo for que se definio nos muestra que se puede realizar un analisis
    iterativo del agrupamiento de datos, sin embargo, expone los mismos
    valores que la instrucción anterior

    """
    for key_group, group in df.groupby('cut'):
        grouped_price = group['price'].mean()
        print('Cut: {} - Price: {}'.format(key_group, grouped_price))

    """
    Cuando definimos grupos con mas de un campo, nos encontramos con una estructura
    que previamente revisamos, que son los indices multiples, por lo que las
    operaciones que en su momento revisamos, son perfectamente aplicables
    bajo esta perspectiva del agrupamiento de datos

    """
    ic(df.groupby(['cut', 'color'])['price'].mean())
    ic(df.groupby(['cut', 'color'])['price'].mean().to_frame)

    """
    Aunado al uso de funciones propias de las librerias de python, podemos hacer
    diseño de funciones a medida y aplicar un conjunto de ellas al subconjunto
    de datos en nuestro grupo, con el fin de obtener información calculada y al
    tiempo agrupada

    Es posible definir funciones en un diccionario para agrupar tambien las operaciones
    y que estas sean aplicadas con respecto a los campos del dataframe evaluado

    """
    ic(df.groupby(['cut', 'color'])['price'].aggregate([min, count, max, np.mean, mean_kilos])) # Se agregan funciones explicitamente
    ic(df.groupby(['cut', 'color']).aggregate(dict_agg)) # Se agregan funciones implicitamente, declaradas a partir de un diccionario
    """
    Los filtros pueden ser definidos de igual forma por medio de funciones, dando
    asi mayor versatilidad al momento de traer la información en nuestro dataframe

    """
    ic(df.groupby(['cut']).filter(f_filter))
    ic(df.groupby(['cut']).filter(f_filter)['color'].unique())
    ic(df.groupby(['cut']).filter(f_filter)['cut'].unique())


if __name__ == '__main__':
    run()