# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 4 de octubre de 2023.
# Tarea 6.2.

# Explicación:
# Este es un juego de Battleship.

import random

# Crear un tablero de 5x5
tablero = [[0 for _ in range(5)] for _ in range(5)]

# Posicionar el barco en una ubicación aleatoria
barco_fila = random.randint(0, 4)
barco_columna = random.randint(0, 4)

intentos_maximos = 7

for intento in range(intentos_maximos):
    # Pedir al usuario que ingrese fila y columna
    fila_usuario = int(input("↔️ Ingresa un número de fila (0-4): "))
    columna_usuario = int(input("↕️ Ingresa un número de columna (0-4): "))

    # Verificar si los valores ingresados son iguales a la posición del barco
    if fila_usuario == barco_fila and columna_usuario == barco_columna:
        print("💥 ¡FELICITACIONES! ¡Has hundido el barco!")
        break
    else:
        print("🧨 Intento incorrecto. Intenta de nuevo.")

    # Mostrar la cantidad de intentos restantes
    intentos_restantes = intentos_maximos - (intento + 1)
    if intentos_restantes > 0:
        print(f"💣 Te quedan {intentos_restantes} intentos.")
    else:
        print("😓 Lo siento, has agotado todos tus intentos. El barco estaba en la fila", barco_fila, "y columna", barco_columna)
