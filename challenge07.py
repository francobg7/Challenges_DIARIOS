import random

# Definimos las opciones
opciones = ["piedra", "papel", "tijera"]

# Función para elegir una opción aleatoria para la computadora
def elegir_opcion():
    return random.choice(opciones)

# Función para determinar el resultado del juego
def resultado_juego(opcion_usuario, opcion_computadora):
    if opcion_usuario == opcion_computadora:
        return "Empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijera") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
         (opcion_usuario == "tijera" and opcion_computadora == "papel"):
        return "Usuario gana"
    else:
        return "Computadora gana"

# Simulamos el juego
def juego():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    
    while True:
        opcion_usuario = input("Elige tu opción (piedra, papel, tijera): ").lower()
        
        # Validar la opción del usuario
        while opcion_usuario not in opciones:
            print("Opción inválida. Por favor, elige piedra, papel o tijera.")
            opcion_usuario = input("Elige tu opción (piedra, papel, tijera): ").lower()
        
        opcion_computadora = elegir_opcion()
        print(f"Usuario elige: {opcion_usuario}")
        print(f"Computadora elige: {opcion_computadora}")
        
        resultado = resultado_juego(opcion_usuario, opcion_computadora)
        print(f"Resultado: {resultado}")
        
        if resultado != "Empate":
            break
        else:
            print("Empate, ¡vamos a jugar de nuevo!")

# Ejecutamos el juego
if __name__ == "__main__":
    juego()
