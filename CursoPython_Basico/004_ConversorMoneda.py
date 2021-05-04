# Uso de funciones
def convierte (valor_dolar, cambio):
   dolares = input("Ingresa el número de dólares a convertir:  ")
   dolares = float(dolares)
   pesos = dolares * valor_dolar
   pesos = round(pesos, 2)
   pesos = str(pesos)
   print("Tienes " + pesos + " " + cambio)


menu = """
Bienvenido al conversor de dólares 😊
Elige la opción que requieres realizar:

[1] Dólares a pesos mexicanos
[2] Dólares a pesos argentinos
[3] Dólares a pesos colombianos   """
selector = input (menu)
selector = int(selector)
if selector == 1:
   convierte(19.87, "pesos mexicanos")
elif selector == 2:
   convierte(92.94, "pesos argnetinos")
elif selector == 3:
   convierte(3613.96, "pesos colombianos")
else:
   print("Elige una opción válida")