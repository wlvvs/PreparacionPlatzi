# If anidado con uso de cadena con salto de carro
menu = """
Bienvenido al conversor de dólares 😊
Elige la opción que requieres realizar:

[1] Dólares a pesos mexicanos
[2] Dólares a pesos argentinos
[3] Dólares a pesos colombianos

"""
selector = input (menu)
selector = int(selector)
if selector == 1:
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   valor_dolar = 19.87
   pesos = dolares * valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " pesos mexicanos")
elif selector == 2:
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   valor_dolar = 92.94
   pesos = dolares * valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " pesos argentinos")
elif selector == 3:
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   valor_dolar = 3613.96
   pesos = dolares * valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " pesos colombianos")
else:
   print("Elige una opción válida")