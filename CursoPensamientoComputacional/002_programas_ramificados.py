from icecream import ic

def run():
    nombre1, edad1 = input('\nDame el nombre y la edad de la primera persona separados por un espacio: ').split()
    nombre2, edad2 = input('Dame el nombre y la edad de la segunda persona separados por un espacio: ').split()

    if int(edad1) < int(edad2):
        print(f'\n{nombre2} tiene {edad2} años, mientras que {nombre1} tiene {edad1}. {nombre2} es el mayor')
    elif int(edad1) > int(edad2):
        print(f'\n{nombre2} tiene {edad2} años, mientras que {nombre1} tiene {edad1}. {nombre1} es el mayor')
    else:
        print(f'\n{nombre2} tiene {edad2} años, mientras que {nombre1} tiene {edad1}. Ambos tienen la misma edad')


if __name__ == '__main__':
    run()