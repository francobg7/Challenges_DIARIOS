#DIA 2
#Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

#pedir que se ingrese el numero
numero = int(input("Introduzca el numero: ")) 
# tabla de multiplicar
print("Tabla de multiplicar del" , numero)
for i in range(1,11):
    print(numero, "x", i, "=", numero * i)
