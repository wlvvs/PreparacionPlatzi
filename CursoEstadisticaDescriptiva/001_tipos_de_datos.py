from icecream import ic
import pandas as pd

dir_pandas = './files/{}'

def run():
    df = pd.read_csv(dir_pandas.format('cars.csv'))
    ic(df.info())
    ic(df.dtypes)
    ic(df.describe())


if __name__ == '__main__':
    run()