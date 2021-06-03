'''
Opera de manera similar a enumeración exhaustiva, sin embargo, no
requiere de una respuesta exacta, ya que se basa en aproximaciones.
El valor de comparar la aproximación con la realidad es llamado epsilon
y si es necesario que el valor de epsilon sea mas pequeño, es decir, que
la aproximación sea cada vez mas acertada, es necesario realizar mayor
cantidad de operaciones. Si el valor de aproximación no tiene que ser
tan exacto, entonces epsilon será mas grande pero tomará menos tiempo
realizar las operaciones
'''

from icecream import ic

def run(val):
    
    objetivo = val
    # El valor de epsilon puede ajustarse para nivelar las ejecuciones y que tan cerca queremos estar de la respuesta
    epsilon = 0.01
    # El valor de paso también puede ajustarse y dice que tanto nos vamos acercando en cada iteracion a la respuesta
    paso = epsilon ** 2
    respuesta = 0.0
 
    # Se maneja valor absoluto para el caso de números negativos, junto con la segunda condición. Dice que nos vamos acercando al objetivo
    while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        # ic(objetivo, ' ', respuesta, ' ', paso, ' ', epsilon)
    
    if abs(respuesta ** 2 - objetivo) >= epsilon:
        print(f'\n  No se encontró la raíz cuadrada de {objetivo}\n')
        # ic(objetivo, ' ', respuesta, ' ', paso, ' ', epsilon)
    else:
        print(f'\n  La raíz cuadrada de {objetivo} es {respuesta}\n')
        # ic(objetivo, ' ', respuesta, ' ', paso, ' ', epsilon)


if __name__ == '__main__':
    run(val)