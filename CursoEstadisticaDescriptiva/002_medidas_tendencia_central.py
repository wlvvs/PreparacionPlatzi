from icecream import ic
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dir_pandas = './files/{}'

def run():
    df = pd.read_csv(dir_pandas.format('cars.csv'))
    ic(df.info())
    ic(df.describe())
    ic(df.sample(5))
    # Se calcula el promedio del precio en dolares de todos los autos
    ic(df['price_usd'].mean())
    # Se calcula la mediana del precio en dolares de todos los autos
    ic(df['price_usd'].median())
    
    # Se genera un histograma de frecuencias a partir de un campo del dataframe
    # La opción bins indica la division por cada elemento del histograma
    # Aqui se observa sesgo importante en datos
    
    df['price_usd'].plot.hist(bins = 20)
    plt.show()
    
    # Seaborn es una libreria con enfoque estadistico que agrega valor tanto
    # funcional como visual. En la instruccion se indica el origen de los datos,
    # que en este caso es el dataframe, la columna a evaluar, que seguira siendo
    # el precio y la distribucion de los histogramas, en este caso, la marca,
    # esto con el fin de que se agrupe toda la informacion de esta manera
    #sns.displot(df, x = 'price_usd', hue = 'manufacturer_name')
    #plt.show()

    sns.displot(df, x = 'price_usd', hue = 'engine_type', multiple = 'stack')
    plt.show()

    ic(df.groupby('engine_type').count())

    # Filtro la informacion para que mi dataframe solo sea considerado con
    # respecto a jeeps
    df_filter = df[(df['manufacturer_name'] == 'Jeep')]
    # Reviso la disponibilidad de modelos
    sns.histplot(df_filter, x = 'price_usd', hue = 'model_name')
    plt.show()
    # Con base al gráfico, solo me interesa conocer algunos modelos, por
    # lo que reduzco mi dataframe
    df_filter = df_filter.query('model_name in ("Cherokee" , "Wrangler" , "Renegade")')
    # Reviso la informacion de precios con respecto a los modelos
    sns.histplot(df_filter, x = 'price_usd', hue = 'model_name')
    plt.show()
    # Reviso la ubicacion de los modelos revisados contra el año del auto, ya que
    # el hecho de que esten en Rusia me hace ya no quererlo jeje
    sns.histplot(df_filter, x = 'year_produced', y = 'price_usd', hue = 'location_region')
    plt.show()

if __name__ == '__main__':
    run()