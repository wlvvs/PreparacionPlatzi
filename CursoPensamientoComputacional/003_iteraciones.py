from icecream import ic

def run():
    # Prueba de ciclo while simple
    contador = 0
    
    while contador < 10:
        ic(contador)
        contador += 1
    
    # Prueba de ciclos anidados
    contador_externo = 0
    contador_interno = 0
    
    while contador_externo < 5:
        while contador_interno < 6:
            ic(contador_externo, contador_interno)
            contador_interno += 1
            # Este break contempla sólo el bloque interno, el bloque externo se sigue ejecutando
            if contador_interno == 5:
                break
    
        contador_externo += 1
        contador_interno = 0


if __name__ == '__main__':
    run()