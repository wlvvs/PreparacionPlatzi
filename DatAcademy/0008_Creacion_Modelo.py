'''
Aquí se crea el modelo de regresión lineal
'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    
    '''
    Se carga el csv usando pandas
    '''
    df = pd.read_csv('./files/StudentsPerformance.csv')
    
    '''
    Se extraen los valores dentro del csv para las columnas de
    reading score y writing score, ya que para el ejemplo práctico,
    se genera la hipotesis dwe que si se obtiene un buen puntaje en el test
    de lectura, tambien se debera obtener en el test de escritura
    '''
    X = df['reading score'].values
    Y = df['writing score'].values

    print('')
    print('Valores sin formato para regresion lineal (Se muestra el formato de 5)')
    for i in range (1,6):
        print(X[i])

    '''
    Los valores recibidos por parte de la regresión lineal deberan formatearse
    para su manejo
    '''
    X = X.reshape(-1, 1)

    print('')
    print('Valores sin formato para regresion lineal (Se muestra el formato de 5)')
    for i in range (1,6):
        print(X[i])

    '''
    Una vez instalado el paquete scikit-learn, podemos usarlo para importar la funcion
    de entrenamiento.
    Train test split divide el universo de datos (x, y) con base a una razón porcentual
    En este ejemplo, estamos diciendo que del valor total de la muestra, tomará como
    valores de prueba el 20% y el 80% restante sera el valor de entrenamiento
    Al invocar el proceso, este divide la información en 4 grupos, los valores de
    entrenamiento tanto para X como Y y los valores de prueba tanto para X como para Y
    '''
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

    '''
    Aca se genera la implementación de la regresion lineal
    Esto se vió de manera practica y manual previamente, aqui se usan funciones diseñadas
    con ese fin
    '''
    from sklearn.linear_model import LinearRegression
    reg = LinearRegression() # Se asigna la función a una variable de trabajo
    
    reg.fit(X_train, Y_train) # Se realiza el proceso de entrenamiento
    
    # Valores que regresa la funcion de regresion lineal
    print('La pendiente es: ',reg.coef_)
    print('El bias es: ', reg.intercept_)


if __name__ == '__main__':
    run()