# triangulo: programa para asignar si el triangulo es equilatero, isosceles, escaleno

# entradas:
# lado1: ingresar el primer numero para la medida 
# lado2: ingresar el segundo numero para la medida
# lado3: ingresar el tercer numero para la medida

#salida: 
# triangulo: el resultado de las medidas dadas para determinar el tipo de triangulo

# pedir los tres numero de las medidas de los lados del triangulo
lado1 = int(input("ingrese el primer numero del triangulo: "))
lado2 = int(input("ingrese el segundo numero del triangulo: "))
lado3 = int(input("ingrese el tercer numero del triangulo: "))

#mostrar resultado
if lado1 == lado2 == lado3:
    print("el triangulo es equilatero")
elif (lado1 == lado2 or lado2 == lado3 or lado3 == lado1):
    print("el triangulo es isosceles")
else: 
    print("el triangulo es escaleno")