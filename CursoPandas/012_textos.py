from icecream import ic
import pandas as pd

def run():
    data = {'names':['Sara Moreno 34',
    'jUAn GOMez 23',
    'CArlos mArtinez 89',
    'Alfredo VelaZques 3',
    'luis Mora 56',
    '@freddier #platzi 10',pd.NA]}
    ic(data)

    df = pd.DataFrame(data)
    ic(df)
    # Se cambian las cadenas con respecto a la forma del texto
    ic(df['names'].str.lower())
    ic(df['names'].str.upper())
    ic(df['names'].str.capitalize())

    # Se mide el tamaño de cadena almacenada en el dataframe
    ic(df['names'].str.len())

    # Se dividen las cadenas por la ocurrencia de espacios
    # Es posible definir el caracter de division de diversas maneras, no solo espacios
    ic(df['names'].str.split(' '))

    # Por medio del principio de slices, es posible extraer caracteres de las cadenas
    # Notese la ubicacion de los dos puntos y el signo de valores
    # que representan el sentido de la extraccion
    ic(df['names'].str[:10]) # Los primeros 10
    ic(df['names'].str[-8:]) # Los ultimos 8

    # De esta forma se realiza el remplazo de caracteres
    ic(df['names'].str.replace('a', 'AAA'))

    # Se encuentran cadenas especificas dentro de las cadenas del dataframe
    ic(df['names'].str.findall('Mo')) # Explicitamente
    ic(df['names'].str.contains('Mo')) # Implicitamente

    # Forma para realizar conteo de ocurrencias
    ic(df['names'].str.lower().str.count('o'))

    # Forma para extraer texto por medio de expresiones regulares
    ic(df['names'].str.extract('([0-9]+)', expand = True)) # Extraccion de numeros
    ic(df['names'].str.extract('([0-9]+)', expand = False)) # Extraccion de numeros
    ic(df['names'].str.replace('@[^\s]+','')) # Reemplazo de una cadena antecedida por @


if __name__ == '__main__':
    run()