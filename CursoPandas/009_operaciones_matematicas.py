from icecream import ic
import pandas as pd
import numpy as np

dir_pandas = './files/{}'
pd.options.display.float_format = '{:,.1f}'.format

def run():
    df = pd.read_csv(dir_pandas.format('london_merged.csv'))
    df_lm = df.copy(deep = True)
    ic(df.head(10))
    ic(df_lm.head(10))
    ic(df_lm.dtypes)
    # Cuando el formato del dato esta apegado al timestamp, es posible
    # ejecutar la transformacion sin parametros
    df_lm['timestamp'] = pd.to_datetime(df_lm['timestamp'])
    ic(df.dtypes)
    ic(df_lm.dtypes)
    # Teniendo el timestamp, se pueden extraer valores especificos del formato
    # en este caso, se usa para generar una nueva columna
    df_lm['hour'] = df_lm['timestamp'].dt.hour
    ic(df_lm.head(10))
    # Esta es otra forma de eliminar columnas, en donde estamos extrayendo
    # por medio de la localizacion de indices, todo menos la primera de las columnas
    df_lm = df_lm.iloc[:,1:]
    ic(df_lm.head(10))

    # Para los campos del dataframe, es posible realizar operaciones matematicas, con
    # la opcion de realizar 'filtros' de informacion al momento de ejecutar las operaciones
    ic(df_lm['wind_speed'] ** 2)
    ic(np.sin(df_lm['season']))
    ic(df_lm['t1'].iloc[::2])
    ic(df_lm['t1'].iloc[::3] - df_lm['t2'])
    # Esta forma de trabajo es tecnicamente una resta que permite 
    # rellenar valores cuando se encuentran nulos en las operaciones
    ic(df_lm['t1'].iloc[::3].sub(df_lm['t2'], fill_value = 1000))


if __name__ == '__main__':
    run()