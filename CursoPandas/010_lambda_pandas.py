from icecream import ic
import pandas as pd
import numpy as np

dir_pandas = './files/{}'
pd.options.display.float_format = '{:,.1f}'.format

def fun_2(x, a = 1, b = 0):
    y = x **2 + a * x + b
    return y


def fun_1(x):
    y = (x ** 2) + 1
    return y


def run():
    df = pd.read_csv(dir_pandas.format('london_merged.csv'))
    df_lm = df.copy(deep = True)
    df_lm['timestamp'] = pd.to_datetime(df_lm['timestamp'])
    df_lm['hour'] = df_lm['timestamp'].dt.hour
    df_lm = df_lm.iloc[:,1:]
    ic(df_lm)
    ic(fun_1(np.arange(-10,10)))
    # Para usar una funcion a partir de una columna del dataframe, se usa la funcion apply
    ic(df_lm['hour'].apply(fun_1))
    
    ic(fun_2(np.arange(-10,10)))
    # Es posible pasar argumentos a una función tomando como base una columna de un dataframe
    # definiendo la key args o indicando la variable y valor tal como los pide la funcion, ya
    # que si se le cambia el nombre a las variables en la llamada, esta no ejecuta correctamente
    ic(df_lm['hour'].apply(fun_2, args = (7, 11)))
    ic(df_lm['hour'].apply(fun_2, a = 7, b = 11))
    # Las funciones lambda se usan para ejecutar funciones sin declaracion de la misma
    # Con esto, se puede simplificar la definicion de labores recurrentes sobre los datos de 
    # nuestro dataframe
    ic(df_lm['hour'].apply(lambda x: x **2 + 7 * x + 11))

    ic(df_lm['hour'].apply(lambda x: x + 273))

    ic(df_lm.apply(lambda x: x.mean()))

    ic(df_lm.apply(lambda x: x.mean(), axis = 1))

    ic(df_lm.applymap(lambda x: x * 3))


if __name__ == '__main__':
    run()