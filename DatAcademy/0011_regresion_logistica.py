import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# De aca se carga un dataset de imagenes, que viene recortado con respecto a la libreria
from sklearn.datasets import load_digits
# De aca se obtienen todas las utilerias que usaremos para definir los sets de entrenamiento y pruebas
from sklearn.model_selection import train_test_split
# De aca se toma lo necesario para generar la regresion lineal
from sklearn.linear_model import LogisticRegression
# De aca se toma lo necesario para generar un pipeline
from sklearn.pipeline import make_pipeline
# De aca se toma lo necesario para el proceso de escalacion de datos del modelo
from sklearn.preprocessing import StandardScaler
# De aca se obtienen lo necesario para generar la matriz de confusión
from sklearn import metrics
from icecream import ic

def run():
    
    digits = load_digits()
    """
    Se revisa la dimensión de mi dataset. Dice que tiene 1979 iagenes con 64 pixeles
    Esto dado que el dataset contiene piezas de 8 x 8, como se aprecia en la ejecución
    de ic(digits)
    Contiene claves: data, imagenes, target y target_names

    """

    ic(digits.data.shape)

    """
    Se genera un sample de la primera imagen del dataset.
    Los números del arreglo representan a los pixeles. Marcan la 
    intensidad, que va de 0 a 255. Así es como se leen las imágenes
    dentro de una computadora

    """
    digit_sample = digits.data[0]
    ic(digit_sample)

    """
    Al ser un problema de aprendizaje supervisado contamos con datos
    ya etiquetados a los que queremos llegar como resultado.
    Se revisa la dimensión de target y además, se extrae el primer
    valor del mismo.
    El resultado que obtenemos significa que el primer resultado que
    se pretende representar es un 0. Dicho de otra forma, el valor del sample
    que obtuvimos lineas arriba está etiquetado como 0
    
    Para graficarlo, se usará la función de plt con la función imshow() y ademas
    de eso, tenemos que realizar un reshape de nuestro sample.
    Como se ve al imprimir el valor del sample, este es un vector y, para realizar
    la 'conversión' a modo imagen, es necesario que se presente como
    una matriz de 8 x 8
    Para esto, usamos la función reshape() de numpy y le indicamos que queremos
    ver una matriz de 8 x 8

    """
    ic(digits.target.shape)
    ic(digits.target[0])
    digit_reshaped = digit_sample.reshape(8,8)
    ic(digit_reshaped)
    plt.imshow(digit_reshaped)
    plt.show()

    """
    Para verificar de manera gráfica mas imagenes dentro del dataset original,
    se realiza el siguiente proceso. Como vimos anteriormente, requerimos
    de un sample con formato de matriz y su target para saber de que valor
    se trata, por lo que, con dicho antecedente, se generará una lista de
    esta combinación de valores, ayudandonos del método zip(), que justamente
    genera una tupla de valores, justo los que necesitamos. Vamos a tomar
    un rango del 31 al 41 para contemplar 10 valores que, como ya comentamos,
    tendrán dos elementos, que son mi vector de sample y la etiqueta

    """
    number_sample = list(zip(digits.data[31:41], digits.target[31:41]))
    ic(number_sample)
    ic(np.array(number_sample).shape)

    """
    Para realizar la graficación de las imagenes, se usará un ciclo for,
    usando enumerate. Esto permite que en las iteraciones, podamos manejar
    el índice del elemento en el sample de 10 números.
    De igual forma como se realizó en el ejemplo anterior, es necesario
    generar el reshape del vector para convertirlo en una matriz y pueda
    ser interpretado en gráfica.
    Para visualizar cada una de las gráficas como una sola, se utiliza
    subplots. Los valores que recibe esta función, de izquierda a derecha,
    son: el número de figuras, el número de subplots y el índice de recorrido
    del ciclo for.
    La línea plt.figure() se usó para cambiar el tamaño de cada uno de los
    subplots. Ejecuta con y sin esa línea para que notes la diferencia.
    Los valores que recibe son dimensiones en pulgadas

    """
    plt.figure(figsize = (11, 11))
    for index, (image, label) in enumerate(number_sample):
        ic(index + 1, label)
        digit_reshaped = image.reshape(8,8)
        plt.subplot(1, len(number_sample), index + 1)
        plt.imshow(digit_reshaped)
        plt.title(f'L: {label}')
    plt.show()

    """
    Para el caso concreto del proceso de regresion logística que se
    trabaja, el objetivo es generar un clasificador de imágenes. En
    ejercicios previos en donde usamos una regresión lineal para obtener
    predicciones dependiendo de la recta.
    En este caso, lo que buscamos es predecir una serie de valores
    que pueden denominarse clases. Por la naturaleza de información
    que tenemos dentro del set de datos, las clases son los valores del
    0 al 9 (10 clases)
    Con claridad en el contexto, usaremos la funcion traint_test_split
    para generar el set de entrenamiento y el set de pruebas con respecto
    al set general que importamos con nuestras imágenes
    Los valores que ingresaremos seran las imagenes (digits.data),
    las etiquetas (digits.target), el tamaño del entrenamiento (test_size)
    y un elemento llamado semilla (seed), que nos dará un valor aleatorio
    para realizar la división de la información

    """
    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size = 0.2, random_state = 21)
    ic(len(x_test))
    ic(len(x_train))

    """
    A continuación, se crea un pipeplane, que es la forma en que se tratan
    los datos para ser entrenados. En este punto, vamos a escalar/estandarizar
    los datos para tener un modelo mas eficiente y rápido de entrenar.
    La instrucción de construcción del pipeline make_pipeline() recibe
    como entrada dos valores, primero el método de escalamiento, mismo 
    que inicializamos con sklearn y el segundo, el contenido de
    la regresión logística. Lo que se va a realizar en este punto es que 
    todos los pasos que entraran a la regresión logistica a entrenamiento,
    primero deben pasar por el escalador

    """
    pipe = make_pipeline(StandardScaler(), LogisticRegression())
    pipe.fit(x_train, y_train)
    ic(pipe.fit(x_train, y_train))

    """
    La regresión logística con Scikit-Learn usa por defecto la presición
    como métrica de evaluación del modelo. La presición se define como:
    precisión = (# de predicciones correctas) / (# total de predicciones)
    Para obtenerlo, se usa pipe.score() y regresa un valor decimal que
    representa el porcentaje de efectividad de predicciones

    """
    score = pipe.score(x_test, y_test)
    ic(pipe.score(x_test, y_test))

    """
    El siguiente paso, es practicar haciendo predicciones con nuestro
    modelo. En una variable cualquiera, vamos a asignar el valor de
    entrenamiento correspondiente a alguno de los índices de valores,
    en este caso, un valor del 0 al 359 (recuerda que calculamos el
    numero de valores que se estaban considerando dentro de nuestro test
    y este dio 360. Esto va a diferir con respecto al valor porcentual que
    indiquemos al momento de definir cuanto sera test y cuanto sera
    entrenamiento).
    Una vez hecho esto, vamos a formatear la variable que asignemos
    en modo tensor, esto para poder pasar despues la asignación de la
    variable al proceso de predicción. Esto me regresa un valor que
    representa lo que tendrá la imagen. Para corroborar los
    resultados, lo graficamos

    """
    guinea_pig = x_test[29]
    ic(guinea_pig)
    guinea_pig = guinea_pig.reshape(1, -1)
    ic(guinea_pig)
    ic(pipe.predict(guinea_pig))
    guinea_pig = guinea_pig.reshape(8, 8)
    ic(guinea_pig.reshape(8, 8))
    plt.imshow(guinea_pig)
    plt.show()

    """
    Ahora, teniendo ese contexto, se generan todas las predicciones
    globales del modelo.

    """
    predictions = pipe.predict(x_test)
    ic(predictions)
    ic(len(predictions))

    """
    Una matriz de confusión es una forma de visualizar el desempéño
    de nuestro algoritmo comparando el valor actual de la
    etiqueta vs el de la predicción realizada por el modelo.
    Esto lo hacemos con metrics.confusion_matrix() que requiere
    en primer lugar, los valores de las etiquetas y despues, las
    predicciones calculadas.
    Para visualizar los resultados de la matriz de confusión, usamos
    seaborn, en donde, con respecto a la intersección de los ejes, veremos
    cuanles son los 'hits' en donde los valores se predicen correctamente
    y en donde existe un error en la predicción

    Para la grafica de calor, annot permite anotaciones, se da un valor de 
    0.5 en las lineas y la rejilla de valores se formatea como cuadrado

    """
    cm = metrics.confusion_matrix(y_test, predictions)
    ic(cm)
    plt.figure(figsize = (9, 9))
    plt.title(f'Puntaje de precisión: {score}', fontsize = 15)
    plt.xlabel("Valor de predicción")
    plt.ylabel("Valor de actual")
    sns.heatmap(cm, annot = True, linewidths = 0.5, square = True, cmap = "Blues_r")
    plt.show()


if __name__ == '__main__':
    run()