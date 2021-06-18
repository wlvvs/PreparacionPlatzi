from icecream import ic
import pandas as pd
import numpy as np

"""
La definición de la ruta de esta manera nos permite utilizarla en diversas
ocasiones a lo largo del codigo, sobre todo de este en donde estaremos
creando diferentes tipos de archivo

"""
dir_pandas = './files/{}'

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
    # Instruccion para crear un archivo en formato excel a partir del dataframe
    df.to_excel(dir_pandas.format('test_excel.xlsx'))
    # Instruccion para crear un archivo en formato excel a partir del dataframe, quitando el indexado del dataframe
    df.to_excel(dir_pandas.format('test_excel_2.xlsx'), index = False)
    # Instruccion para crear un archivo en formato excel a partir del dataframe, quitando el indexado del dataframe y colocando un nombre a la hoja
    df.to_excel(dir_pandas.format('test_excel_3.xlsx'), index = False, sheet_name = 'Sheet 1')
    # Instruccion para crear un archivo en formato json a partir del dataframe
    df.to_json(dir_pandas.format('test_json.json'))
    # Instruccion para crear un archivo en formato pickle a partir del dataframe
    df.to_pickle(dir_pandas.format('test_pickle.pkl'))
    # Instruccion para crear un archivo en formato pickle a partir del dataframe
    df.to_parquet(dir_pandas.format('test_parquet.parquet'))
    # Instruccion para crear un archivo en formato hdf a partir del dataframe
    # Dentro de la plataforma de linux, el archivo se genera correctamente
    df.to_hdf(dir_pandas.format('test_hdf.h5'), key = 'data', format = 'table')

    """
    La lectura de los archivos atiende al tipo y es similar en todos
    los casos. No existe un archivo correcto o incorrecto, esto depende
    totalmente del uso y las condiciones con las cuales estaremos
    trabajando, ya que hay archivos que destacan por el entorno, por la
    usabilidad, el peso e incluso por la herramienta que los usará como
    insumo. En esencia, todos brindan la misma información del dataframe,
    eso es lo verdaderamente importante

    """
    ic(pd.read_excel(dir_pandas.format('test_excel.xlsx')))
    ic(pd.read_excel(dir_pandas.format('test_excel_2.xlsx')))
    ic(pd.read_json(dir_pandas.format('test_json.json')))
    ic(pd.read_pickle(dir_pandas.format('test_pickle.pkl')))
    ic(pd.read_parquet(dir_pandas.format('test_parquet.parquet')))
    ic(pd.read_hdf(dir_pandas.format('test_hdf.h5')))


if __name__ == '__main__':
    run()
