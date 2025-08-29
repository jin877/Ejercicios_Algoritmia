# numero: programa para saber si el numero es multiplo de 5

# entrada:
# numero: primer numero
# numero: segundo numero

#salida: 
# iniciales: el primer numero es multiplo del segundo

# proceso: pide el primero numero que es multiplicado por el segundo para mostrar el resultado de si es multiplo o no lo es

# pedir los numeros 
numero = int(input("ingrese el primer numeros: "))
numero = int(input("ingres el segundo numero: "))

# mostrar resultado
if (numero % 5 == 0 ):
    print("el primer numero es multiplo del segundo")
else:
    print("no es multiplo")