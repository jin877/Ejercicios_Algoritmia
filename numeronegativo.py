# numero: programa para saber si es numero negativo

# salida:
# numero: numero es negativo

#entrada:
#iniciales

#proceso: pide el un numero menor a 0 que muestre que el resultado es negativo y si es mayor a 0 el sultado se mostrar como "el numero no es negativo"

# pedir numero
number = int(input("ingrese un numero: "))

#mostrar resultado
if (number < 0 ):
    print("el numero es negativo")
else:
    print("el numero no es negativo")