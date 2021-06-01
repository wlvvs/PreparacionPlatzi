# Juego del ahorcado.
# De una serie de nombre de películas predefinidas, se elige una al azar y después se procede a tratar de adivinarla.
# Se tienen 5 intentos para adivinar letras.
# Cada turno eliges una letra y al final, ya sea que juntes todas las letras que conforman el nombre o
# acumules los 5 errores, debes ingresar el nombre de la película. Si escribes el nombre de la pelicula, ganas, sino, pierdes

def revisa_letra(cadena):

    intento = 5
    corte = 0
    letras = ""
    acierto = 0
    winner = list(set(cadena.replace(" ","")))
        
    while True:
        letra = input ("""
Escribe una letra de la A a la Z:   """)
        letra = letra.upper()
        if len(letra.upper()) != 1:
            intento -= 1
            print("""El valor que ingresaste (""" + letra.upper() + """) es incorrecto.
Tus oportunidades de acertar se restan en uno, ahora tienes """ + str(intento) + """. Las letras que
haz acertado son """ + str(list(letras)) + """ y te restan por adivinar """ + str(len(winner) - acierto) + """ letras!""")
            print("")
        
        if letra.upper() in letras:
            print("""El valor que ingresaste (""" + letra.upper() + """) ya está dentro de las letras que adivinaste! 
Las letras que haz acertado son """ + str(list(letras)) + """ y te restan por adivinar """ + str(len(winner) - acierto) + """ letras!""")
            print("")
        elif letra.upper() in winner and letra.upper() not in letras:
            letras = letras + letra.upper()
            acierto = acierto + 1
            print("""El valor que ingresaste (""" + letra.upper() + """) es correcto! 
Las letras que haz acertado son """ + str(list(letras)) + """ y te restan por adivinar """ + str(len(winner) - acierto) + """ letras!""")
            print("")
        else:
            intento -= 1
            print("""El valor que ingresaste (""" + letra.upper() + """) es incorrecto.
Tus oportunidades de acertar se restan en uno, ahora tienes """ + str(intento) + """. Las letras que
haz acertado son """ + str(list(letras)) + """ y te restan por adivinar """ + str(len(winner) - acierto) + """ letras!""")
            print("")
        
        if acierto == len(winner):
            corte = 1
            respuesta = input ("""
Ya tienes todas las letras que forman el nombre de la película.
Estas son: """ + str(list(letras)) + """ - Escribe el nombre de la película que se forma con
esas letras:   """)
            respuesta = respuesta.upper().replace(" ","")
            frase = cadena.upper().replace(" ","")
            if respuesta == frase:
                print("")
                print("G A N A S T E !!!! - (" + cadena + ") ES LA RESPUESTA CORRECTA!!! :D :D :D ")
                print("")
            else:
                print("")
                print("P E R D I S T E !!!! - (" + cadena + ") ES LA RESPUESTA CORRECTA!!! :( :( :( ")
                print("")
        elif intento == 0:
            corte = 1
            respuesta = input ("""
Se acabaron tus intentos! Intenta adivinar el nombre de la película con las letras que encontraste!
Estas son: """ + str(list(letras)) + """ - Escribe el nombre de la película que se forma con
esas letras:   """)
            respuesta = respuesta.upper().replace(" ","")
            frase = cadena.upper().replace(" ","")
            if respuesta == frase:
                print("")
                print("G A N A S T E !!!! - (" + cadena + ") ES LA RESPUESTA CORRECTA!!! :D :D :D ")
                print("")
            else:
                print("")
                print("P E R D I S T E !!!! - (" + cadena + ") ES LA RESPUESTA CORRECTA!!! :( :( :( ")
                print("")

        if corte == 1:
            break  
    

def peliculas(eleccion):

    print("""
Bienvenido al juego del ahorcado con temática de peliculas infantiles.
La pelicula que debes adivinar, tiene """ + str(len(eleccion.replace(" ",""))) + """ letras
de la A a la Z. No contiene ningún número. Tienes 5 intentos para adivinar letras y
al final, el nombre de la película. ¿Podrás ganarme en este reto?
    """)
    revisa_letra(eleccion)


def run():
    import random
    FILME = ("DUMBO", "MULAN", "POCAHONTAS", "TOY STORY", "EL VIAJE DE CHIHIRO", "EL CASTILLO VAGABUNDO", "HARRY POTTER", "SPIDERMAN", "LILO Y STITCH")

    eleccion = random.choice(FILME)
    peliculas(eleccion)

if __name__ == '__main__':
    run()