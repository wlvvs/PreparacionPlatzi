from icecream import ic

def divide_elementos(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        ic(e)
        return lista


def run():
    lista = list(range(10))
    divisor = 0

    print(divide_elementos(lista, divisor))


if __name__ == '__main__':
    run()