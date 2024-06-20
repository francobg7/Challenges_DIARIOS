#DIA 4
#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.
numeros_usuarios = input("Por favor, introduce una lista de números separados por espacios: ")
lista_numeros = [int(numero) for numero in numeros_usuarios.split()]
n = len(lista_numeros)
for i in range(n):
    for j in range(0, n - i - 1):
        if lista_numeros[j] > lista_numeros[j + 1]:
            # Intercambiamos los elementos si están en el orden incorrecto.
            lista_numeros[j], lista_numeros[j + 1] = lista_numeros[j + 1], lista_numeros[j]

# Finalmente, mostramos la lista ordenada.
print("Lista ordenada:", lista_numeros)
