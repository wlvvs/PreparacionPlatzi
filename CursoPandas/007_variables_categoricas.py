from icecream import ic
import pandas as pd
from pandas.core.tools.datetimes import to_datetime

dir_pandas = './files/{}'
pd.options.display.float_format = '{:,.1f}'.format

def run():
    df_meteoritos = pd.read_csv(dir_pandas.format('Meteorite_Landings.csv'))
    ic(df_meteoritos.head())
    ic(df_meteoritos.convert_dtypes().dtypes)
    # Muestra el conteo de registros unicos dentro del dataframe
    ic(df_meteoritos.nunique())
    ic(df_meteoritos[['fall','nametype']])
    # Cambia el tipo de dato de los campos marcados a categórico. Esto se usa para generar catalogos de datos
    df_meteoritos[['fall','nametype']] = df_meteoritos[['fall','nametype']].astype('category')
    ic(df_meteoritos.convert_dtypes().dtypes)
    ic(df_meteoritos['fall'].unique)
    # Realiza conteo de datos agrupados por conceptos (en este caso, las categorias que se definieron previamente)
    ic(df_meteoritos['fall'].value_counts())
    ic(df_meteoritos['nametype'].unique)
    ic(df_meteoritos['nametype'].value_counts())
    # Con base a los datos categoricos, recrea dichos valores en columnas con distribucion binaria, siendo la categoria el nombre de columna
    ic(pd.get_dummies(df_meteoritos['fall']))
    df_meteoritos[['fell','found']] = pd.get_dummies(df_meteoritos['fall'])
    ic(df_meteoritos.head())
    ic(df_meteoritos[['year']])
    # Cambio de tipo de dato string con caracteristicas de fecha a tipo de dato fecha
    df_meteoritos['year'] = pd.to_datetime(df_meteoritos['year'], errors = 'coerce', format = '%m/%d/%Y %H:%M:%S %p')
    ic(df_meteoritos[['year']])
    ic(df_meteoritos.convert_dtypes().dtypes)
    df_meteoritos.rename(columns = {'mass (g)':'mass'}, inplace = True)
    ic(df_meteoritos.head())


if __name__ == '__main__':
    run()