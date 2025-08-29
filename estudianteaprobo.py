# nota: programa para signar una nota a un estudiante

# entradas: 
# nota: nota del estudiante

#salida
#iniciales: el numero de 1 al 100

#proceso: pide un numero de 1 al 100 de la nota del estudiante, extrae la nota para confirmar que el estudiante aprobo o reprobo.

note = int(input("ingrese la nota del estudiante del 1 al 100: "))

# mostrar resultado
if (note >= 60):
    print("el estudiante aprobo")
else:
    print("el estudiante reprobo")