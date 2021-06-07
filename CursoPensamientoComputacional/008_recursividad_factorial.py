from icecream import ic

def factorial(n):
    """
    Calcula el factorial de n

    n int > 0
    return n!
    """
    # Se comienza escribiendo el caso base, para evitar loops infinitos
    ic(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)    


def run():
    """
    Función principal del código
    """

    n = int(input('''\nIngresa un entero para calcular el factorial: '''))
    print(f'El factorial de {n} es {factorial(n)}')


if __name__ == '__main__':
    run()