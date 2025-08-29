# Nombre: Programa para obtener iniciales en mayusculas

#Entradas: 
# Nombre: nombre de la persona ,
# Apellido: apellido de la persona

# Salidas
# Iniciales: la primera letras de nombre y apellido

# Proceso: pide el nombre y apellido de la persona, extrae la primera letra del nombre y el apellido. Imprime en mayuscula las iniciales

# Pedir nombre y apellido
nombre = input("ingrese su nombre: ")
apellido = input("ingresa tu apellido: ")

# Tomar la primera letra de cada uno y ponerla en mayuscula
iniciales = nombre[0].upper() + apellido[0].upper()

# Mostrar resultado
print("tus iniciales son:", iniciales)