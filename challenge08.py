#DIA 8
#Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable 
#(entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.
import random
import string

def generar_contraseña(longitud):
    # Definimos los grupos de caracteres
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Creamos una lista que contiene al menos un carácter de cada grupo
    contraseña = [
        random.choice(mayusculas),
        random.choice(minusculas),
        random.choice(numeros),
        random.choice(simbolos)
    ]

    # Rellenamos el resto de la contraseña con caracteres aleatorios de todos los grupos combinados
    todos_los_caracteres = mayusculas + minusculas + numeros + simbolos
    contraseña += random.choices(todos_los_caracteres, k=longitud - 4)

    # Mezclamos la lista para que la contraseña no tenga un patrón predecible
    random.shuffle(contraseña)

    # Convertimos la lista a una cadena y la devolvemos
    return ''.join(contraseña)

def obtener_longitud():
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña (entre 8 y 16 caracteres): "))
            if 8 <= longitud <= 16:
                return longitud
            else:
                print("La longitud debe estar entre 8 y 16 caracteres.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    # Obtenemos la longitud de la contraseña del usuario
    longitud = obtener_longitud()

    # Generamos la contraseña
    contraseña_segura = generar_contraseña(longitud)
    print(f"Tu contraseña segura es: {contraseña_segura}")

if __name__ == "__main__":
    main()
