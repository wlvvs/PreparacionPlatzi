import numpy as np
from icecream import ic

'''
Se generan constantes del código, para identificar la clasificación
de palabras y los caracteres especiales que se quitarán de los tweets
'''
CARACTERES_ESP = '!#$%^&*().,¿?¡'

P_POSITIVAS = ['excelente', 'gran', 'bueno', 'inteligente', 'corazón', 'felicidad', 'bien', 'buenos', 'corazon']

P_NEGATIVAS = ['muerte', 'perdida', 'ignorante', 'despedimos', 'confundida', 'confundido', 'drogas', 'soledad', 'luto', 'falsa']

P_NEUTRAS = ['mexicano', 'señor', 'señora', 'platzi', 'docente', 'novio', 'novia', 'novios', 'quincena', 'mercurio', 'barda', 'casa', 'películas', 'película', 'vida', 'chocolate', 'gallo', 'argentino', 'mexicanos']

P_TOTALES = P_NEGATIVAS + P_POSITIVAS + P_NEUTRAS


def check_twetts():

    '''
    Se analizan los twets desde un archivo que reside en un directorio de media dentro del proyecto
    '''
    with open("./files/tweets.txt","r", encoding = 'utf8') as twet:
        for item in twet:
            '''
            Se inicializan las variables que contendran tanto los conteos de palabras clasificados
            como positivas, negativas y neutras, así como el conteo de apariciones del universo
            de palabras completo dentro del twet
            '''
            vector_w = []
            conteo_positivo = 0
            conteo_negativo = 0
            conteo_neutro = 0

            '''
            Convertimos el twet en un arreglo de palabras, quitando caracteres especiales
            '''
            twet_clean = item.replace(CARACTERES_ESP, "").lower().split(" ")

            for palabra in P_TOTALES:
                '''
                Por cada palabra existente en la suma de vectores de palabras negativas, positivas
                y neutras, se realiza la evaluación de su existencia en los twets para conocer
                el conteo por clasificación
                '''
                vector_w.append(twet_clean.count(palabra))
                
                if (palabra in P_POSITIVAS) and (palabra in twet_clean):
                    conteo_positivo += 1
                elif (palabra in P_NEGATIVAS) and (palabra in twet_clean):
                    conteo_negativo += 1
                elif (palabra in P_NEUTRAS) and (palabra in twet_clean):
                    conteo_neutro += 1
                else:
                    pass
                
            '''
            Generamos un arreglo con el acumulado de puntos de clasificacion.
            Posteriormente, calculamos el promedio total y el promedio parcial para
            tener el dato de calidad del twet y clasificación con respecto a los
            sentimientos que refleja
            '''
            resume_twitt = np.array([conteo_positivo, conteo_negativo, conteo_neutro])
            vector_w = np.array(vector_w)
            promedio = (np.ones(vector_w.size) / vector_w.size).T.dot(vector_w)
            calidad = resume_twitt / (resume_twitt[0] + resume_twitt[1] + resume_twitt[2])

            print('\n-----------------------')
            print(f'El tweet es el siguiente: \n\n{item}')
            print(f'\nCon respecto a su texto, tiene {conteo_positivo} palabras positivas, {conteo_negativo} palabras negativas y {conteo_neutro} palabras neutras')
            print(f'O lo que es lo mismo, {calidad[0]} de positividad, {calidad[1]} de negatividad y {calidad[2]} de neutralidad')
            print(f'La calidad del tweet es de {promedio}\n')


def run():
    '''
    Progama que revisa los sentimientos que refleja un twet por medio de una clasificación
    de palabras predeterminadas
    '''

    print('''\nEste programa evalua una serie de tweets que se leen de un archivo y con base a una
    clasificación de palabras positivas, negativas y neutras, se determina en que rubro queda el contexto
    del tweet\n\n''')
    check_twetts()

if __name__ == '__main__':
    run()