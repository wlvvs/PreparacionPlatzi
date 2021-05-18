'''

Python Cardio - Reto 2

Escribe un programa en donde juegues piedra, papel o tijeras con 
la máquina

Bonus: Que sea un dos de tres
Reto personal: Lograrlo usando pandas

'''
import random
import os
import time
import pandas as pd

def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def winner(choose):
    PLAY = (1, 2, 3, 4, 5)
    machine_op = int(random.choice(PLAY))
    df = pd.read_csv("game.csv")

    try:
        result = int(df.iloc[int(choose) - 1, machine_op])

        if choose < 0:
            raise ValueError
        else:
            if result == machine_op:
                return [1,machine_op]
            elif result == choose:
                return [0,machine_op]
            elif result == -9:
                return [-9,machine_op]
            else:
                raise ValueError

    except ValueError:
        return [7,7]
    except IndexError:
        return [7,7]


def run():
    cut = 0
    w_machine = 0
    w_people = 0

    while True:
        clearenv()
        try:
            print('')
            print ('       M A R C A D O R')
            print('')
            print('     Máquina:', w_machine,'     Tú:', w_people)
            print('')
            print('')
            choose = input('''
Juego de piedra, papel, tijeras, lagarto y Spock (oh hell yes, baby!)
Igualito al convencional, pero mas geek.
Las reglas son las siguientes:

_________________________________
    
 Las tijeras cortan el papel
 El papel cubre la piedra
 La piedra aplasta el lagarto
 El lagarto envenena a Spock
 Spock aplasta las tijeras
 Las tijeras decapitan el lagarto
 El lagarto se come el papel
 El papel refuta a Spock
 Spock vaporiza la piedra
 La piedra aplasta a las tijeras

_________________________________

(1) Piedra   (2) Papel   (3) Tijeras   (4) Lagarto   (5) Spock

        Elige tu opción, patea a la máquina   ''')
        
            played = winner(int(choose))
            print('')
            if int(played[0]) == 1:
                print('Ganó la máquina! Tu elegiste', choose, 'y la máquina eligió', played[1])
                w_people += 1

            elif int(played[0]) == 0:
                print('Ganaste! Tu elegiste', choose, 'y la máquina eligió', played[1])
                w_machine += 1

            elif int(played[0]) == -9:
                print('Esto es un empate! Tu elegiste', choose, 'y la máquina eligió', played[1])

            else:
                raise ValueError
        
        except ValueError:
            print('')
            print('')
            print('    El valor insertado es incorrecto :(    ')
        except IndexError:
            print('')
            print('')
            print('    El valor insertado es incorrecto :(    ')

        if w_people == 3 or w_machine == 3:
            cut = 1
            if w_people < w_machine:
                print('')
                print('    Se acabaron los intentos, ganó la máquina!!')
            else:
                print('    Se acabaron los intentos, ganaste!!')
            
        time.sleep(3)
        
        if cut == 1:
            clearenv()
            print('')
            print ('       M A R C A D O R   F I N A L ')
            print('')
            print('     Máquina:', w_machine,'     Tú:', w_people)
            print('')
            print('')
            break


if __name__ == '__main__':
    run()