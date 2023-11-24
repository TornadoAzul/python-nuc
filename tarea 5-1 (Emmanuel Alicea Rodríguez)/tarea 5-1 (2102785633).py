# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 1 de octubre de 2023.
# Tarea 5.1.

# Explicación:
# Este es un juego donde el usuario podrá establecer un número base
# y un número máximo y adivinará entre estos.

# Acá importamos los paquetes necesarios.

import random
import time

# Aquí definimos la función para establecer los números en los
# que adivinará el usuario en si.

def obtener_numero_usuario(minimo, maximo):
    while True:
        try:
            numero = int(input(f"🧮 Ingresa un número entre {minimo} y {maximo} (o escribe 'END' para salir): "))
            if minimo <= numero <= maximo:
                return numero
            else:
                print(f"🚨 Por favor, ingresa un número dentro del rango {minimo} y {maximo}.")
        except ValueError:
            print("🚨 Por favor, ingresa un número válido.")

# Ahora definimos el número aleratorio.

def generar_numero_aleatorio(minimo, maximo):
    return random.randrange(minimo, maximo + 1)

#Ahora establecemos la función de jugar.

def jugar_juego():
    minimo = int(input("💙 Ingresa el número mínimo para el rango: "))
    maximo = int(input("🧡 Ingresa el número máximo para el rango: "))
    numero_aleatorio = generar_numero_aleatorio(minimo, maximo)
    intentos = 0
    tiempo_inicio = time.time()

    while True:
        numero_usuario = obtener_numero_usuario(minimo, maximo)

        if numero_usuario == "END":
            print(f"👉 El número generado aleatoriamente fue: {numero_aleatorio}")
            break

        intentos += 1

        if numero_usuario < numero_aleatorio:
            print("👆El número es mayor. Intenta de nuevo.")
        elif numero_usuario > numero_aleatorio:
            print("👇 El número es menor. Intenta de nuevo.")
        else:
            tiempo_fin = time.time()
            tiempo_total = tiempo_fin - tiempo_inicio
            print(f"🎉 ¡Enorabuena! ¡Has adivinado! Lo lograste en {intentos} intentos.")
            print(f"⌛️ Tiempo total: {tiempo_total:.2f} segundos.")
            break

if __name__ == "__main__":
    jugar_juego()
