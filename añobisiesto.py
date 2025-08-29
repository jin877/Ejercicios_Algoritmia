#año: programa para saber si el año es bisiesto

# entradas:
# año: el año es bisiesto o no lo es

# salida:
# iniciales: el año que quieras ingresar

# proceso: pide que ingreses un año, extrae la informacion para la confirmacion de si es un año bisiesto. 

# tomar el año
year = int(input("ingrese un año: "))

# mostrar resultado
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")