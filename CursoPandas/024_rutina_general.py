from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir_pandas = './files/{}'

def run():
    df_temp = pd.read_csv(dir_pandas.format('GlobalLandTemperaturesByCountry.csv'))
    df_temp = df_temp.interpolate()
    ic(df_temp.info())
        """
    El primer paso es realizar conversion de informacion a datos mas optimos
    y la limpieza del universo de datos en el dataframe

    """
    df_temp['year'] = pd.to_datetime(df_temp['dt'])
    ic(df_temp.info())
    """
    Se genera un filtro de datos para extraer aquella informacion que esta
    dentro del dataframe y la fecha a la que pertenecen es mayor a 1970
    Este tipo de asignacion simplifica la instruccion de filtrado
    dentro del dataframe
    
    """
    ixn = df_temp['year'] >= pd.to_datetime('1970-01-01')
    df_temp = df_temp[ixn]
    ic(df_temp.info())

    """
    La informacion del dataframe se agrupara por dos parametros, uno de ellos
    categorico y el otro, la extraccion que generamos de año por medio de la 
    funcion grouper, teniendo una frecuencia de particion de un año.
    De manera adicional, se genera un diccionario de funciones para agregar
    el promedio y la media de las temperaturas registradas
    
    """
    ic(df_temp.groupby(['Country', pd.Grouper(key = 'year', freq = '1Y')]).agg({'AverageTemperature':[np.mean, np.median]}))
    df_tmp_avg = df_temp.groupby(
        ['Country',
        pd.Grouper(key = 'year', freq = '1Y')]).agg({'AverageTemperature':[np.mean, np.median]})
    ic(df_tmp_avg.xs('Mexico')['AverageTemperature'])
    """
    Para elegir un pais en paricular, se utiliza la funcion xs para realizar
    la extraccion de datos y al colocar la funcion plot, estos datos seran
    graficados
    
    """
    df_tmp_avg.xs('Mexico')['AverageTemperature'].plot()
    plt.show()

    """
    Siguiendo con el trabajo en datos, del dataframe de promedio y mediana,
    se genera uno nuevo donde solo se considera la mediana y se resetean
    los indices, para que en vez de tener al pais, ahora se tenga la numeracion
    por default en la estructura
    Se agrega una columna de año, en donde esta se extrae de la columna
    year por medio de la funcion dt
    Se renombran las columnas para un mejor entendimiento de la informacion
    
    """
    df_temp_median = df_tmp_avg['AverageTemperature'][['median']].reset_index()
    ic(df_temp_median.sample(10))
    df_temp_median['date'] = df_temp_median['year'].dt.year
    df_temp_median.rename(columns = {'median':'temperature'}, inplace = True)
    ic(df_temp_median.sample(10))

    """
    Para obtener una grafica botplox, necesitamos generar una tabla pivot en donde
    los valores representativos sean las temperaturas, el indice las fechas y
    las conlumnas sean los paises.
    Un boxplot muestra la informacion por bloques, en este caso los paises, 
    todos evaluados desde la misma gráfica comparativa

    Se usa un manejo interesante de trasposicion para elegir de manera aleatoria
    paises dentro de nuestro dataframe
    
    """
    df_temp_pivot = df_temp_median.pivot_table(values = 'temperature', index = 'date', columns = 'Country')
    df_temp_pivot.T.sample(7).T.boxplot(rot = 45)
    plt.show()


if __name__ =='__main__':
    run()