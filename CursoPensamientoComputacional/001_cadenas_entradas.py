from icecream import ic

def run():
    my_str = 'la academia de Platzi'
    ic(len(my_str))
    ic('Yo amo a '+ my_str)
    ic(f'Yo amo a {my_str}')
    ic(my_str.count('a'))
    ic(my_str.replace('a', 'e'))
    ic(my_str.split())
    ic(my_str[0])
    ic(my_str[1])
    ic(my_str[2])
    ic(my_str[3])
    ic(my_str[4])
    ic(my_str[5])
    # Notación de slice: [comienzo:final:pasos]
    ic(my_str[:1:5])
    ic(my_str[1::3])
    ic(my_str[:5:])
    ic(my_str[::-1])
    ic(input('Dame un valor: '))


if __name__ == '__main__':
    run()