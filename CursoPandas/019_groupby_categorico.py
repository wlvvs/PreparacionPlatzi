from icecream import ic
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.display.float_format = '{:,.3f}'.format

def run():
    df = sns.load_dataset('tips')
    df['prct_tip'] = (df['tip'] / df['total_bill']) * 100
    ic(df.describe(include = 'all'))
    ic(df.sample(10))
    """
    Se agrega una columna de 1 que nos servira para realizar agrupaciones por
    medio de campos categoricos.
    Las operaciones en este caso, se efectuan de manera similar a como se ha
    venido trabajando, solo que se usa la columna de 1 para realizar sobre ese
    valor las operaciones

    """
    df['ones'] = 1

    df_g = df.groupby(['sex', 'smoker'])[['ones']].sum() # Traemos la suma de valores divididos por genero y habito de fumar
    ic(df_g)
    ic(df_g.groupby(level = 0).apply(lambda x: (x / x.sum()) * 100)) # Lo mismo que el anterior pero con valores porcentuales

    ic(pd.cut(df['total_bill'], bins = 3).value_counts()) # Usamos una variable no categorica y generamos rangos de particion de datos implicitamente
    ic(pd.cut(df['total_bill'], bins = [3, 18, 35, 60]).value_counts()) # Lo mismo que el anterior pero con una marca de particion explicita
    df['bin_total'] = pd.cut(df['total_bill'], bins = [3, 18, 35, 60]) # Se asigna el valor de particion a una columna categorica dentro del dataframe
    ic(df)

    """
    Los campos no categoricos que se volvieron categoricos tambien pueden usarse
    como parametros de agrupacion

    """
    ic(df.groupby(['time', 'bin_total'])[['ones']].count())
    ic(df.groupby(['time', 'bin_total'])[['ones']].count().groupby(level = 0).apply(lambda x: (x / x.sum()) * 100))


if __name__ == '__main__':
    run()