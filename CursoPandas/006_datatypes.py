import pandas as pd
from icecream import ic

dir_pandas = './files/{}'
"""
Es posible ajustar el formato con el cual los datos seran presentados en la 
pantalla. En este caso, se hacen ajustes para que los valores decimales del
dataframe aparezcan con un solo valor decimal y con la coma como caracter de
división para identificar valores en rango de miles

"""
pd.options.display.float_format = '{:,.1f}'.format

def run():
    df_meteoritos = pd.read_csv(dir_pandas.format('Meteorite_Landings.csv'))
    
    # Se presentan los 10 primeros valores del csv
    ic(df_meteoritos.head(10))

    # Se presentan los 10 ultimos valores del csv
    ic(df_meteoritos.tail(10))

    # Se presentan 10 valores aleatorios del csv
    ic(df_meteoritos.sample(10))

    # Se presenta la composición matricial del csv, que en este caso es de 45716 filas con 10 columnas
    ic(df_meteoritos.shape)

    # Se presenta el tamaño del csv, que es de 45716 elementos
    ic(df_meteoritos.size)

    # Se presenta el valor del indexado del csv, que va de 0 a 45715 con avance de 1
    ic(df_meteoritos.index)

    # Se presenta el nombre de las columnas que componen al csv
    ic(df_meteoritos.columns)

    # Se presenta información general del csv, como la composición de columnas, tipos de dato y uso de memoria
    ic(df_meteoritos.info())

    # Se presenta información especial de los campos numéricos, un primer vistazo de la información
    ic(df_meteoritos.describe())

    # Se presenta información especial de los campos numéricos, un primer vistazo de la información, incluyendo los campos alfanumericos
    ic(df_meteoritos.describe(include = 'all'))
    
    # Se muestran los tipos de dato correspondientes a cada columna
    ic(df_meteoritos.dtypes)

    # Se muestran los tipos de dato correspondientes a cada columna con base a un proceso de optimización que realiza pandas
    ic(df_meteoritos.convert_dtypes().dtypes)


if __name__ == '__main__':
    run()