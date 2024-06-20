#DIA 5
#Crear un Diccionario: Escribe un programa que cree un diccionario a partir de dos listas dadas: una de claves y otra de valores.

claves = ['nombre', 'edad', 'ciudad']
valores = ['Franco', 24, 'CDE']
combinados = zip(claves, valores)
diccionario = dict(combinados)
print(diccionario)
