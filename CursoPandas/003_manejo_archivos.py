from icecream import ic
import pandas as pd
import numpy as np

def run():
    
    dict_data = {
    'edad' : [ 10, 9, 13, 14, 12, 11, 12],
    'cm' : [ 115, 110, 130, 155, 125, 120, 125],
    'pais' : [ 'co', 'mx', 'co', 'mx', 'mx', 'ch', 'ch'],
    'genero' : [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'Q1' : [ 5, 10, 8, np.nan, 7, 8, 3],
    'Q2' : [ 7, 9, 9, 8, 8, 8, 9]
    }
    ic(dict_data)

    df = pd.DataFrame(dict_data)
    ic(df)

    """
    Usando este tipo de interpretacion, generamos una variable que almacenara
    la ruta del archivo que estemos manejando, mismo que nos permitira tener
    acceso de forma rapida y con tan solo copiar y pegar la linea

    """
    dir_pandas_01 = './files/{}'.format('test.csv')

    """
    Con la ruta que construimos anteriormente, vamos a guardar el dataframe en
    formato csv dentro del directorio especificado de archivos.
    Se comentaran las lineas con respecto a las actividades que se realizan
    en cada una de las corridas

    """
    # Se crea CSV
    df.to_csv(dir_pandas_01)
    
    dir_pandas_02 = './files/{}'.format('test2.csv')
    # Se crea CSV sin indice default
    df.to_csv(dir_pandas_02, index = False)

    dir_pandas_03 = './files/{}'.format('test3.csv')
    # Se crea CSV sin indice default y modificando el separador default
    df.to_csv(dir_pandas_03, sep = '|', index = False)

    """
    Para leer la informacion de los csv que generamos, se usa la funcion
    read_csv. Cuando se realizan modificaciones a los separadores
    del csv, estos archivos dejan de ser reconocidos en su opcion
    default, por lo que será necesario que se indique cual es el 
    separador de información para poder mostrarla en pantalla

    """

    ic(pd.read_csv(dir_pandas_01))
    ic(pd.read_csv(dir_pandas_02))
    ic(pd.read_csv(dir_pandas_03))
    ic(pd.read_csv(dir_pandas_03, sep = '|'))


if __name__ == '__main__':
    run()