# Prueba de diccionarios
def run():

    menu = {
        'Lunes': ('Sopa de papa', 'Arroz colorado', 'Filete de pescado con ensalada', 'Flan napolitano'),
        'Martes': ('Sopa de verduras', 'Arroz con cúrcuma', 'Sopecitos con bistec', 'Plátanos fritos'),
        'Miercoles': ('Crema de champiñones', 'Moros y cristianos', 'Enchiladas potosinas', 'Jericallas'),
        'Jueves': ('Sopa de lentejas', 'Ensalada de nopales', 'Mole de olla', 'Fresas con crema'),
        'Viernes': ('Consomé de pollo', 'Arroz poblano', 'Chamorros', 'Gelatina de frambuesa')
    }
    
    eleccion = input("""
Fonda La Chiquita

Elije la opción de tu preferencia:
(1) Muestra los días que hay menú disponible
(2) Muestra el menú de todos los días
(3) Muestra el menú de un día en específico

""")

    if int(eleccion) == 1:
        for dia in menu.keys():
            print('')
            print(dia)
    elif int(eleccion) ==2:
        for dia, comida in menu.items():
            print('')
            print('La comida del día ' + dia +' es: ' + str(comida))
    elif int(eleccion) ==3:
        print('')
        consulta = input ('Escribe el día del que quieres conocer el menú:  ')
        print('')
        print ('El menú del día '+ consulta.lower().capitalize().replace(" ","") + ' es: ')
        print (menu[consulta.lower().capitalize().replace(" ","")])
        print('')
    else:
        print ('El valor ingresado no forma parte de las opciones :(')


if __name__ == '__main__':
    run()