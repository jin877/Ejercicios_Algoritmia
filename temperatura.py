# temperatura: programa para saber si la temperatura es menor a 0

# entrada: 
# temperaura: la temperatura en la que se congela el agua

# salida:
# iniciales: temperatura 

# proceso: pide una temperatura por si un liquido como agua o un jugo se congela a la temperatura de 0 gradoss y si es mayor a cero se queda igual en liquido

# pedir temperatura
temperatura = int(input("ingrese una temperatura para congelar: "))

# mostrar  resultado
if (temperatura <= 0):
    print("temperatura adecuada")
else:
    print("la temperatura no es adecuada")