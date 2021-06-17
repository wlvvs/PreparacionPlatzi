from icecream import ic
import pandas as pd
import numpy as np

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
    df.to_excel(dir_pandas.format('test_excel.xlsx'))
    df.to_excel(dir_pandas.format('test_excel_2.xlsx'), index = False)
    df.to_excel(dir_pandas.format('test_excel_3.xlsx'), index = False, sheet_name = 'Sheet 1')
    df.to_json(dir_pandas.format('test_json.json'))
    df.to_pickle(dir_pandas.format('test_pickle.pkl'))
    df.to_parquet(dir_pandas.format('test_parquet.parquet'))
    #df.to_hdf(dir_pandas.format('test_hadoop.hdf'), key = 'data', format = 'table')
    ic(pd.read_excel(dir_pandas.format('test_excel.xlsx')))
    ic(pd.read_excel(dir_pandas.format('test_excel_2.xlsx')))
    ic(pd.read_json(dir_pandas.format('test_json.json')))
    ic(pd.read_pickle(dir_pandas.format('test_pickle.pkl')))
    ic(pd.read_parquet(dir_pandas.format('test_parquet.parquet')))
    #ic(pd.read_hdf(dir_pandas.format('test_hdf.hdf')))


if __name__ == '__main__':
    run()