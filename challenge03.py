#DIA 3
#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.
cadena = input("por favor ingrese una cadena:  ")
print(f"la palabra ingresada fue:",(cadena))

def contar_vocales(cadena):

    vocales = 'aeiou'
    contador_vocales = 0
    
    for letra in cadena.lower():
        
        if letra in vocales:
            contador_vocales += 1

    return contador_vocales

resultado = contar_vocales(cadena)
print(f"El número de vocales en la cadena es: {resultado}")






