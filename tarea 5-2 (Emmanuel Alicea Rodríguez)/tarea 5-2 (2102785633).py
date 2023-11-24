# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 1 de octubre de 2023.
# Tarea 5.2.

# Explicación:
# Este es un juego donde el usuario podrá establecer un número base
# y un número máximo y adivinará entre estos.

# Aquí tenemos mis 5 colores.
colores = "azul naranja rojo morado cian"

# Acá hacemos la búsqueda de los nombres.
for color in colores.split():
    print("Color:", color)

    # Acá nos detenemos al encontrar el color cian.
    if color == "cian":
        print("🩵 He encontrado el color cian. Uno muy bonito. Hemos terminando el bucle.")
        break

# Continuar después de encontrar el color cian.
for color in colores.split():
    # Omitir ahora el color cian.
    if color == "cian":
        continue

    print("Color:", color)

# Ahora mostraremos 10 números.
print("💙 FOR para mostrar los 10 números:")
for numero in range(1, 11):
    print(numero, end=" ")

# Mostraremos del 5 al 10.
print("\n💜 FOR para mostrar del 5 al 10:")
for numero in range(5, 11):
    print(numero, end=" ")

# Añadiremos números adicionales.
print("\n🧡 FOR para mostrar del 1 al 12:")
for numero in range(1, 13):
    print(numero, end=" ")

# Usando el WHILE, ahora mostraremos 10 números.
print("\n❤️ WHILE para mostrar los 10 números:")
numero = 1
while numero <= 10:
    print(numero, end=" ")
    numero += 1

# Ahora a mostrar del 5 al 10.
print("\n💚 WHILE para mostrar del 5 al 10:")
numero = 5
while numero <= 10:
    print(numero, end=" ")
    numero += 1

# Ahora para agregar números adicionales.
print("\n💛 WHILE para mostrar del 1 al 12:")
numero = 1
while numero <= 12:
    print(numero, end=" ")
    numero += 1