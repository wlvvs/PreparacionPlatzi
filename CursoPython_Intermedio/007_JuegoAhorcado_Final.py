import random
import os

def clearenv():
    if os.name == 'posix':
        os.system ('clear')
    elif os.name == 'ce' or os.name == 'nt' or os.name == 'dos':
        os.system ('cls')


def secretchain(option, str_letters):
    act_chain = ""

    for check in range(len(option)):
        if option[check] in str_letters or option[check] == ' ':
            act_chain = act_chain + option[check]
        else:
            act_chain = act_chain + '_'
    return act_chain


def check_string(option):

    count_try = 8
    count_cut = 0
    str_letters = ''
    count_win = 0
    winner = list(set(option.replace(' ','')))
        
    while True:
        single_letter = input ('''
        
        Escribe una letra de la A a la Z:   ''')
        clearenv()

        if len(single_letter.upper()) != 1:
            count_try -= 1
            print('')
            print('''El valor que ingresaste (''', single_letter.upper(), ''') es incorrecto. Tienes''', str(count_try), '''intentos de adivinar.''')
            print('')
            print(secretchain(option, str_letters))
            print('')
        
        if single_letter.upper() in str_letters:
            print('''El valor que ingresaste (''', single_letter.upper(), ''') ya está dentro de las letras que adivinaste!''')
            print('')
            print(secretchain(option, str_letters))
            print('')
        elif single_letter.upper() in winner and single_letter.upper() not in str_letters:
            str_letters = str_letters + single_letter.upper()
            count_win += 1
            print('''El valor que ingresaste (''', single_letter.upper(), ''') es correcto!''')
            print('')
            print(secretchain(option, str_letters))
            print('')
        else:
            count_try -= 1
            print('''El valor que ingresaste (''', single_letter.upper(), ''') es incorrecto. Tienes''', str(count_try), '''intentos de adivinar.''')
            print('')
            print(secretchain(option, str_letters))
            print('')
        
        if count_win == len(winner):
            count_cut = 1
            print('G A N A S T E !!!! La respuesta correcta es',option)
        elif count_try == 0:
            count_cut = 1
            print('')
            answer = input ('''Se acabaron tus intentos! Intenta adivinar el nombre de la película con las letras que encontraste!
Escribe el nombre de la película que se forma con esas letras:   ''')

            answer = answer.upper().replace(' ','')
            phrase = option.upper().replace(' ','')

            if answer == phrase:
                print('')
                print('G A N A S T E !!!! La respuesta correcta es',option)
                print('')
            else:
                print('')
                print('P E R D I S T E !!!! La respuesta correcta es',option)
                print('')

        if count_cut == 1:
            break
    

def run():
    films = []
    
    print('')
    print('''

    Bienvenido al juego del ahorcado con temática de peliculas.
    Las películas pertenecen al cine internacional.
    Ingresa una letra de la A a la Z. No están permitidos números.
    Tienes 8 intentos para adivinar letras.
    Si agotas tus intentos, podrás tratar de adivinar el nombre de la película.
    
''')

    with open("./files/movies.txt","r",encoding= "utf-8") as film:
        for item in film:
            films.append(item)
    option = random.choice(films).upper()

    
    check_string(option[:-1])

if __name__ == '__main__':
    run()