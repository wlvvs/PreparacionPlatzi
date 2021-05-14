'''

Python Cardio - Reto 2

Escribe un programa en donde juegues piedra, papel o tijeras con 
la máquina

Bonus: Que sea un dos de tres

'''
import random
import os
import time

def clearenv():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def winner(choose):
    PLAY = (1, 2, 3, 4, 5)
    compare = []
    machine_op = random.choice(PLAY)

    try:
        if (choose in PLAY):
            if machine_op == 1:
                if choose in (4, 3):
                    compare = [1,0]
                elif choose in (2, 5):
                    compare = [1,1]
                else:
                    compare = [1,-1]
            elif machine_op == 2:
                if choose in (1, 5):
                    compare = [2,1]
                elif choose in (3, 4):
                    compare = [2,0]
                else:
                    compare = [2,-1]
            elif machine_op == 3:
                if choose in (2, 4):
                    compare = [3,1]
                elif choose in (1, 5):
                    compare = [3,0]
                else:
                    compare = [3,-1]
            elif machine_op == 4:
                if choose in (5, 2):
                    compare = [4,1]
                elif choose in (3, 1):
                    compare = [4,0]
                else:
                    compare = [4,-1]
            elif machine_op == 5:
                if choose in (3, 1):
                    compare = [5,1]
                elif choose in (2, 4):
                    compare = [5,0]
                else:
                    compare = [5,-1]
        else:
            raise ValueError
    except ValueError:
        return [-9,-9]

    return compare


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

            if played[0] == 1:
                if played[1] == 1:
                    print('  Ganó la máquina, eligió piedra  ')
                    w_machine += 1
                elif played[1] == 0:
                    print('  Ganaste, la máquina eligió piedra  ')
                    w_people += 1
                elif played[1] == -1:
                    print('  Empate, la máquina eligió piedra  ')
            
            elif played[0] == 2:
                if played[1] == 1:
                    print('  Ganó la máquina, eligió papel  ')
                    w_machine += 1
                elif played[1] == 0:
                    print('  Ganaste, la máquina eligió papel  ')
                    w_people += 1
                elif played[1] == -1:
                    print('  Empate, la máquina eligió papel  ')
            
            elif played[0] == 3:
                if played[1] == 1:
                    print('  Ganó la máquina, eligió tijeras  ')
                    w_machine += 1
                elif played[1] == 0:
                    print('  Ganaste, la máquina eligió tijeras  ')
                    w_people += 1
                elif played[1] == -1:
                    print('  Empate, la máquina eligió tijeras  ')

            elif played[0] == 4:
                if played[1] == 1:
                    print('  Ganó la máquina, eligió lagarto  ')
                    w_machine += 1
                elif played[1] == 0:
                    print('  Ganaste, la máquina eligió lagarto  ')
                    w_people += 1
                elif played[1] == -1:
                    print('  Empate, la máquina eligió lagarto  ')

            elif played[0] == 5:
                if played[1] == 1:
                    print('  Ganó la máquina, eligió Spock  ')
                    w_machine += 1
                elif played[1] == 0:
                    print('  Ganaste, la máquina eligió Spock  ')
                    w_people += 1
                elif played[1] == -1:
                    print('  Empate, la máquina eligió Spock  ')
            else:
                raise ValueError
        except ValueError:
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