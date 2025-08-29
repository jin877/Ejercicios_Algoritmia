# rol: programa de ingreso de rol

# entrada: 
# rol: admin o usuario

# salida:
# iniciales: cual es su rol

# proceso: pide el que rol eres, si eres admin o usario para permitirte el acceso  

# pedir el rol
rol = str(input("ingrese su rol admin o usuario: "))

# mostrar resultado
if (rol == "admin"):
    print("acceso permitido")
else:
    print("acceso denegado")