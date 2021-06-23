from icecream import ic
import pandas as pd
import numpy as np

pd.options.mode.use_inf_as_na = True

def run():
    """
    Dentro de numpy, nan es el valor nulo.
    Dentro de pandas, NA es el valor nulo. La diferencia entre ambos radica
    en que para el caso de NA, este tambien es util al momento de trabajar
    con cadenas, lo que lo hace versatil para el manejo de informacion en
    nuestros dataframes

    """
    ic(np.nan)
    ic(np.nan + 1)
    ic(np.nan - 1)
    ic(np.nan * 2)
    ic(np.nan / 2)
    ic(np.nan > 0)
    ic(np.nan < 0)
    ic(np.nan == 0)

    ic(pd.NA)
    ic(pd.NA + 1)
    ic(pd.NA - 1)
    ic(pd.NA * 2)
    ic(pd.NA / 2)
    ic(pd.NA > 0)
    ic(pd.NA < 0)
    ic(pd.NA == 0)
    ic(pd.NA + 'Cadena de caracteres')

    """
    Tomando en cuenta un dataframe numerico definido, se observa el comportamiento
    de nan y NA con respecto a la informacion.
    Si se realiza la evaluacion de nulidad, vemos que para aquellos
    campos que tienen nan o NA, son evaluados con la nulidad

    """
    df = pd.DataFrame(np.arange(0, 15).reshape(5, 3), columns = ['a', 'b', 'c'])
    ic(df)
    df['d'] = np.nan
    df['e'] = np.arange(15, 20)
    df.loc[5,:] = pd.NA
    df.loc[4,'a'] = pd.NA
    df.loc[0,'d'] = 1
    df.loc[5,'d'] = 10
    ic(df)
    ic(df.isnull()) # Esta linea otorga la misma respuesta que la de abajo
    ic(df.isna()) # Esta linea otorga la misma respuesta que la de arriba
    ic(df.isnull().sum()) # Genera la suma de nulos por columnas
    ic(df.isnull().sum(axis = 1)) # Genera la suma de nulos por index (fila)
    """
    Para encontrar el valor de nulos en todo el dataframe, lo que se hace es
    calcular el tamaño del dataframe y se le resta el total de nulos. En las
    siguientes lineas se aprecia la verificacion realizando la resta desde la 
    perspectiva de las filas y de las columnas

    """
    ic(df.size)
    ic(df.size - df.isnull().sum().sum())
    ic(df.size - df.isnull().sum(axis = 1).sum())

    ic(df[df['a'].notnull()]) # Filtra los datos, regresando aquellos que no contienen nulos en columna a
    ic(df.dropna()) # Borra del dataframe completo el registro completo en donde se encuentra un nulo
    ic(df['a'].dropna()) # Borra de la columna a, los valores nulos
    ic(df)

    """
    Con respectro al uso de la informacion, es importante señalar el manejo de
    nulos. Aqui casos practicos.
    Es importante recalcar que los valores anteriores a NA siguen siendo NA en
    todos los casos y el sentido en el que se realiza la revision depende del como
    se rellenan los datos, como sigue:
        - valor siguiente en columna: el sentido es de izquierda a derecha con respecto al campo a rellenar
        - valor siguiente en indice (fila): el sentido es de arriba a abajo con respecto al campo a rellenar
        - valor anterior en columna: el sentido es de derecha a izquierda con respecto al campo a rellenar
        - valor anterior en indice (fila): el sentido es de abajo a arriba con respecto al campo a rellenar

    """
    ic(df.fillna(0)) # Se rellena con el valor 0 cuando se encuentra un nulo
    ic(df.fillna(method = 'ffill')) # se rellena con el valor siguiente partiendo de las columnas
    ic(df.fillna(method = 'ffill', axis = 1)) # se rellena con el valor siguiente partiendo de los indices (filas)
    ic(df.fillna(method = 'bfill')) # se rellena con el valor anterior partiendo de las columnas
    ic(df.fillna(method = 'bfill', axis = 1)) # se rellena con el valor anterior partiendo de los indices (filas)
    ic(df)

    """
    Tomando como base una serie, tambien podemos aplicar el rellenado de datos.
    En este caso, lo que hace pandas es rellenar con respecto a los indices
    de la serie y conservar aquellos valores que no son considerados dentro
    de la serie.
    En este set tambien se muestra el rellenado por medio de operaciones
    aritmeticas, ya que a veces es conveniente hacerlo. Para el ejemplo, se 
    toman la mediana de los valores del dataframe.
    Por ultimo, la interpolacion es un proceso en donde pandas trata de
    identificar el valor que pudiera pertenecer a la serie que no se contempla
    dentro de los valores por ser NA. Este proceso lo realiza de diversas 
    formas, sin embargo, toma en cuenta los valores anterior y posterior
    de acuerdo al eje de revisión

    """
    fill = pd.Series([100, 101, 102])
    ic(fill)
    ic(df['d'].fillna(fill))
    df['d'] = df['d'].fillna(fill)
    ic(df)
    ic(df.fillna(df.median()))
    df_d = pd.concat([df[['d']], df[['d']].interpolate()], axis = 1)
    df_d.columns = ['d_antes','d_interpolado']
    ic(df_d)



if __name__ == '__main__':
    run()