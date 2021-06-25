from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir_pandas = './files/{}'

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
    df_time = df.groupby('ObservationDate').sum()
    df_diff = df_time.diff()
    df_diff = df_diff.fillna({'Confirmed': 555.0, 'Deaths': 17.0, 'Recovered': 28.0})
    
    """
    Aqui estamos resampleando el dataframe con el filtro de tiempo que teniamos
    previamente, usando como razon de resample un marco de 12 horas
    Los datos del grupo son datos de tiempo pero sin la propiedad de horas, lo
    que hara que en nuestro dataframe aparezcan valores nulos.
    De principio, esto no sucede puesto que al agregar la operacion de suma,
    esta considera esos valores como un cero.

    Una vez que indicamos que necesitamos que sume valores cuyo valor minimo
    sea 1, entonces recuperamos un valor nulo, lo cual es el comportamiento
    esperado y real

    """
    ic(df_diff.resample('12h').sum())
    ic(df_diff.resample('12h').sum(min_count = 1))
    ic(df_time.resample('12h').sum(min_count = 1))

    """
    Existen diversas formas de rellenar los valores nulos, mismas que se listam
    a continuacion, todos ellos partiendo de la posicion del valor nulo:
    bfill: rellena con el valor siguiente de abajo hacia arriba
    ffill: rellena con el valor anterior de abajo hacia arriba
    fillna: rellena con un valor preestablecido
    interpolate: realiza un calculo para integrar el valor medio entre los limites
    inferior y superior

    """
    df_cum = df_time.resample('12h').sum(min_count = 1)
    ic(df_cum.bfill().head(5))
    ic(df_cum.ffill().head(5))
    ic(df_cum.fillna('A').head(5))
    ic(df_cum.interpolate().head(5))
    df_cum = df_cum.interpolate()
    df_cum['survivor_rate'] = (1 - df_cum['Deaths'] / df_cum['Confirmed']) * 100
    ic(df_cum.tail(10))
    """
    Con la funcion reset index, se elimina el agrupamiento previo por
    fecha y obtenemos el dataframe con los cambios que le hemos realizado, pero
    con un indexado default.
    Bajo este esquema, tambien es posible realizar filtros de informacion
    por series de tiempo, haciendo uso de la funcion grouper.
    Dentro de los argumentos que podemos pasar a dicha funcion, esta un campo
    dentro del dataframe que tomara como base y una frecuencia con respecto 
    a tiempo.

    Con dicha serie, podemos trabajar para realizar la graficacion de informacion
    y ver de manera grafica como se comporta la informacion.
    Existe una funcion llamada rolling que permite indicar un rango de presentacion
    para que sea la división de valores en el eje x y los valores en la serie para
    cada una de las ocurrencias, constituya el valor de y
    
    """
    df_cum = df_cum.reset_index()
    ic(df_cum.tail(10))

    ic(df_cum.groupby(pd.Grouper(key = 'ObservationDate', freq = 'M'))[['survivor_rate']].mean())
    sr = df_cum.groupby(pd.Grouper(key = 'ObservationDate', freq = '1D'))['survivor_rate'].mean()

    plt.plot(sr, label = 'Original')
    plt.plot(sr.rolling(window = 7).mean(), label = '7 días')
    plt.plot(sr.rolling(window = 30).mean(), label = '30 días')
    plt.xticks(rotation = '90')
    plt.legend()
    plt.title('Promedio de Tasa de Supervivencia COVID19')

    plt.show()
    plt.plot(sr.rolling(window = 30).apply(lambda x: np.std(x)))
    plt.xticks(rotation = '90')
    plt.legend()
    plt.title('Variacion de tasa de Supervivencia COVID19')
    plt.show()


if __name__ =='__main__':
    run()