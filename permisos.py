# contraseña: programa para ingresar una contraseña

# entrada:
# contraseña: contraseña correcta

# salida:
# iniciales: la contraseña

# proceso: pide que ingreses una contraseña y si es correcta saldra que eres bienvenido administrador

#pedir contraseña
contraseña = str(input("ingrese la contraseña: "))

# mostrar resultado
if (contraseña == "Sueñito123"):
    print("bienvenido administrador")
else:
    print("no eres administrador")