from icecream import ic
import pandas as pd

dir_pandas = './files/{}'
pd.options.display.float_format = '{:,.1f}'.format

def run():
    df_meteoritos = pd.read_csv(dir_pandas.format('Meteorite_Landings.csv'))
    # Se crea columna para realizar el borrado de la misma
    df_meteoritos['ones'] = 1
    df_meteoritos[['fell','found']] = pd.get_dummies(df_meteoritos['fall'])
    df_meteoritos['year'] = pd.to_datetime(df_meteoritos['year'], errors = 'coerce', format = '%m/%d/%Y %H:%M:%S %p')
    ic(df_meteoritos.head(10))
    ic(df_meteoritos.convert_dtypes().dtypes)
    # Se elimina la columna. El valor axis indica que se trata de un borrado de columna y
    # con inplace, el cambio se realiza en automatico en el dataframe
    df_meteoritos.drop(['ones'], axis = 1, inplace = True)
    ic(df_meteoritos.head(10))
    # Se genera una copia del dataframe para realizar modificaciones
    # Es importante que se coloque la opción deep, de lo contrario, en las 
    # variables habra actividad tipo apuntador, con deep se generan objetos independientes
    df_test = df_meteoritos.copy(deep = True)
    # Se realiza el borrado de las columnas id y recclass junto con los indices 0, 2, 4 y 6 del
    #dataframe
    df_test.drop(columns = ['id', 'recclass'], index = [0, 2, 4, 6], inplace = True)
    ic(df_meteoritos.head(10))
    ic(df_test.head(10))


if __name__ == '__main__':
    run()