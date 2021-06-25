from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir_pandas = './files/{}'

"""
Dentro de las opciones del dataframe, se pueden utilizar funciones de graficacion
que existen dentro de las utilerias de matplotlib.
Esto resulta muy util debido a que la muestra de informacion por medio
de graficos es mas entendible y se puede apreciar en detalle mas
facilmente

"""
def run():
    df = pd.read_csv(dir_pandas.format('covid_19_data.csv'))
    df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
    df = df[
        ['ObservationDate',
        'Country/Region',
        'Confirmed',
        'Deaths',
        'Recovered']
        ]
    ic(df.groupby('Country/Region')['Confirmed'].max().sort_values(ascending = False).head(10))
    df_time = df.groupby(['Country/Region', pd.Grouper(key = 'ObservationDate', freq = '1D')]).sum()
    ic(df_time)
    df_china = df_time.loc['Mainland China',:]
    df_france = df_time.loc['France',:]
    df_india = df_time.loc['India',:]
    df_mexico = df_time.loc['Mexico',:]
    df_chile = df_time.loc['Chile',:]

    df_china.plot(figsize = (10, 7), title = 'COVID19-CHINA', style = ['r-', 'g--', 'b.'])
    df_france.plot(figsize = (10, 7), title = 'COVID19-FRANCIA', style = ['r-', 'g--', 'b.'])
    df_india.plot(figsize = (10, 7), title = 'COVID19-INDIA', style = ['r-', 'g--', 'b.'])
    df_chile.plot(figsize = (10, 7), title = 'COVID19-CHILE', style = ['r-', 'g--', 'b.'])
    df_mexico.plot(figsize = (10, 7), title = 'COVID19-MEXICO', style = ['r-', 'g--', 'b.'])
    plt.xlabel('Date')
    plt.ylabel('People')
    plt.show()

    df_china = df_china.resample('Y').max()
    df_china.plot(figsize = (10, 7), kind = 'bar', title = 'COVID19-CHINA')
    df_france = df_france.resample('Y').max()
    df_france.plot(figsize = (10, 7), kind = 'bar', title = 'COVID19-FRANCIA')
    df_india = df_india.resample('Y').max()
    df_india.plot(figsize = (10, 7), kind = 'bar', title = 'COVID19-INDIA')
    df_chile = df_chile.resample('Y').max()
    df_chile.plot(figsize = (10, 7), kind = 'bar', title = 'COVID19-CHILE')
    df_mexico = df_mexico.resample('Y').max()
    df_mexico.plot(figsize = (10, 7), kind = 'bar', title = 'COVID19-MEXICO')
    plt.show()

    df_china['Traitment'] = df_china['Confirmed'] - df_china['Deaths'] - df_china['Recovered']
    df_france['Traitment'] = df_france['Confirmed'] - df_france['Deaths'] - df_france['Recovered']
    df_india['Traitment'] = df_india['Confirmed'] - df_india['Deaths'] - df_india['Recovered']
    df_chile['Traitment'] = df_chile['Confirmed'] - df_chile['Deaths'] - df_chile['Recovered']
    df_mexico['Traitment'] = df_mexico['Confirmed'] - df_mexico['Deaths'] - df_mexico['Recovered']

    df_china[['Deaths', 'Recovered', 'Traitment']].T.plot(figsize = (10,7), kind = 'pie', subplots = True, title = 'COVID19-CHINA')
    df_france[['Deaths', 'Recovered', 'Traitment']].T.plot(figsize = (10,7), kind = 'pie', subplots = True, title = 'COVID19-FRANCIA')
    df_india[['Deaths', 'Recovered', 'Traitment']].T.plot(figsize = (10,7), kind = 'pie', subplots = True, title = 'COVID19-INDIA')
    df_chile[['Deaths', 'Recovered', 'Traitment']].T.plot(figsize = (10,7), kind = 'pie', subplots = True, title = 'COVID19-CHILE')
    df_mexico[['Deaths', 'Recovered', 'Traitment']].T.plot(figsize = (10,7), kind = 'pie', subplots = True, title = 'COVID19-MEXICO')

    plt.show()


if __name__ =='__main__':
    run()