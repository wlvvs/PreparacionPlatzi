# Básico inicial
print("Bienvenido al conversor de monedas, elige que acción quieres realizar.")
selector = input ("[1] Convertir dólares a pesos mexicanos || [2] Convertir pesos mexicanos a dólares   ")
selector = int(selector)
if selector == 1:
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   valor_dolar = 19.87
   pesos = dolares * valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " pesos mexicanos")
else:
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   valor_dolar = 19.87
   pesos = dolares / valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " dolares")
