# nombre: programa para saber si el numero es mayor o menor

# entradas:
# numero: numero digitado

# salida: 
# iniciales: ingrese cualquier numero

# proceso: pide un numero que si es mayor a 100 es positivo, si es menor a -0 es negativo y si es esta en 0 a 100  saldra entre la cantidad

number = int(input("ingrese un numero: "))

# mostrar resultado
if (number >= 100):
    print("es mayor a cien")
elif (number < 0):
    print("es menor a cien")
else:
    print("es entre el 100 a 0")