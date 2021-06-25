from icecream import ic
import pandas as pd

dir_pandas = './files/{}'

def run():
    df = pd.read_csv(dir_pandas.format('covid_19_data.csv'))
    ic(df.info())
    ic(df.sample(5))
    """
    Se convierte el campo de fecha que esta expresado como cadena a formato datetime

    """
    df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
    ic(df.info())
    ic(df.sample(5))
    """
    Se limpia el dataframe para tener solo las columnas que nos son utiles para
    el proceso de analisis de informacion

    """
    df = df[
        ['ObservationDate',
        'Country/Region',
        'Confirmed',
        'Deaths',
        'Recovered']
        ]
    ic(df.info())
    ic(df.sample(5))
    """
    Se genera un grupo por fecha y aplicamos la sumatoria de valores
    para identificar los casos con respecto al tiempo y como se van
    incrementando las variables

    """
    df_time = df.groupby('ObservationDate').sum()
    ic(df_time.sample(5))
    df1 = df_time['Confirmed'].iloc[10:15]
    df2 = df_time['Deaths'].iloc[12:17]
    ic(df1)
    ic(df2)
    ic(df1 - df2)
    ic(df_time)
    """
    Aplicar la funcion diff resta del elemento actual, el anterior, esta
    es la razon por la que el primer valor aparece como nulo, ya que es
    justo la operación de restar un numero con un nulo dentro de la 
    logica de python
    
    """
    ic(df_time.diff())
    ic(df_time.diff().mean())
    df_diff = df_time.diff()
    df_diff = df_diff.fillna({'Confirmed': 555.0, 'Deaths': 17.0, 'Recovered': 28.0})
    ic(df_time.diff())
    ic(df_diff)
    ic(df_diff.cumsum())
    """
    Con la funcion resample, es posible reordenar y reagrupar la informacion
    de nuestro dataframe, lo que nos da la versatilidad de tener mas opciones
    al momento de analizar la informacion
    
    """
    ic(df_diff.resample('7D').sum())
    ic(df_diff.resample('W-Sun').sum())
    ic(df_diff.resample('M').sum())
    ic(df_diff.resample('M').count())


if __name__ =='__main__':
    run()