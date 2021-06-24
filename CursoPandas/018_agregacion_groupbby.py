from icecream import ic
import numpy as np
import pandas as pd
import seaborn as sns

pd.options.display.float_format = '{:,.3f}'.format

def mean_eur2usd(x):
    return np.mean(x) * 1.12


def f_filter(x):
    return mean_eur2usd(x['total_bill'].mean()) > 20


def run():

    dict_agg = {
    'tip' : [min, max],
    'total_bill' : [np.mean, mean_eur2usd]
    }

    df = sns.load_dataset('tips')
    ic(df.describe(include = 'all'))
    ic(df['day'].value_counts())
    ic((df['day'].value_counts() / df['day'].value_counts().sum()) * 100)
    ic(df.groupby('sex').mean())
    df['prct_tip'] = (df['tip'] / df['total_bill']) * 100
    ic(df.sample(10))
    ic(df.groupby('sex').mean())
    ic(df.groupby('sex').median())
    ic(df.groupby('sex')[['prct_tip']].describe())
    ic(df.groupby('sex')[['total_bill', 'prct_tip']].describe())
    ic(df.groupby('sex')[['total_bill', 'prct_tip']].apply(mean_eur2usd))
    ic(df.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].apply(mean_eur2usd))
    ic(df.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].apply(lambda x: np.mean(x) * 1.12))
    ic(df.groupby(['sex', 'time'])[['total_bill', 'prct_tip']].aggregate([np.mean, np.max]))
    ic(dict_agg)
    ic(df.groupby(['sex', 'time'])[['total_bill', 'tip']].aggregate(dict_agg))
    ic(df.groupby(['sex', 'time']).filter(f_filter))


if __name__ == '__main__':
    run()