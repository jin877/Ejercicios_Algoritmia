# año: programa para saber si una persona puede votar en Colombia

# entradas:
# edad: edad de la persona
# nacionalidad: nacionalidad de la persona

# salida:
# iniciales: la edad y nacionalidad 

# procesos: pide la edad de la persona y la nacionalidad para saber si puede votar la persona, para votar debe de tener una mayoria de edad y ser de Colombia

# pedir la edad y nacionalidad
age = int(input("ingrese su edad: "))
nationality = str(input("ingrese su nacionalidad: "))

# mostrar resultado
if (age >= 18) & (nationality == "Colombia"):
    print("puedes votar")
else:
    print("no puede votar")