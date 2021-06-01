print("Selecciona que tipo de If quieres revisar")
selector = int(input("[1] If normal || [2] If anidado  "))
if selector == 1:
    edad = int(input("Escribe tu edad:   "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
else:
    edad = int(input("Escribe tu edad:   "))
    if edad > 18:
        print("Tienes mas de 18 años")
    elif edad == 18:
        print("Tienes exactamente 18 años")
    else:
        print("Tienes menos de 18 años")

