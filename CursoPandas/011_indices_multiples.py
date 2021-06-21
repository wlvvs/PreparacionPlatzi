from icecream import ic
import pandas as pd
import numpy as np

dir_pandas = './files/{}'
pd.options.display.float_format = '{:,.1f}'.format


def run():
    df_pob = pd.read_csv(dir_pandas.format('poblacion.csv'))
    ic(df_pob.info())
    ic(df_pob.sample(10))

    # Convertimos una columna entera en categorica. Esto lo hacemos para poder usar multiples indices
    df_pob['year'] = pd.Categorical(df_pob['year'].apply(str))
    ic(df_pob.info())

    # Creamos un filtro para definir aquellos registros en donde los paises se encuentran en el listado
    ixn_filtro = df_pob['Country'].isin(['Mexico','Argentina'])
    ic(ixn_filtro)

    # A partir del filtro, se crea un nuevo dataframe de trabajo
    df_sample = df_pob[ixn_filtro]
    ic(df_sample.info())
    ic(df_sample)

    # Se indica que dos de las tres columnas del dataframe seran indices
    df_sample = df_sample.set_index(['Country', 'year'])
    ic(df_sample)
    ic(df_sample.sort_index())

    # Se juega con diversas formas de extraer información basado en los indices creados
    ic(df_sample.loc['Mexico',:])
    ic(df_sample.loc['Mexico',:].loc['2018',:])
    ic(df_sample.xs(['Argentina']))
    ic(df_sample.xs(['Argentina', '2018']))
    ic(df_sample.xs('Argentina', level = 'Country'))
    ic(df_sample.xs('2017', level = 'year'))

    # Se crea un dataframe global de paises, siguiendo la misma logica del trabajo previo, pero sin filtros
    df_countries = df_pob.set_index(['Country', 'year'])
    ic(df_countries)
    ic(df_countries.sort_index(ascending = [False, True]))
    ic(df_countries.sort_index(ascending = [True, True]))

    # Se asigna una funcion a una variable para un mejor manejo en codigo
    ids = pd.IndexSlice
    # Con base a la funcion de rebanadas, se toman segmentos de información apoyados en el filtro que
    # proporcionan las rebanadas
    ic(df_countries.sort_index(ascending = [True, True]).loc[ids['Moldova':'Morocco','2015':'2017'],:].sort_index())

    # Estas instrucciones nos muestran cuales son los indices dentro de nuestro dataframe, lo
    # anterior basado en niveles
    ic(df_countries.index.get_level_values(0))
    ic(df_countries.index.get_level_values(1))

    # Se extrae informacion puntual haciendo uso de los indices
    ic(df_countries['pop']['Mexico']['2017'])

    # Se realizan operaciones matematicas con respecto a los indices
    ic(df_countries.sum(level = 'year'))

    # Una de las ventajas de tener indices, es justamente la posibilidad de variar la vista del dataframe
    # y de la extraccion de informacion
    ic(df_sample)
    ic(df_sample.unstack('year'))
    ic(df_sample.unstack('Country'))


if __name__ == '__main__':
    run()