# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 4 de octubre de 2023.
# Tarea 6.1.

# Explicación:
# Este programa usará un array de invitados al paintball para
# añadirle al mismo nuevos datos, organizarlos y vizualizarlos.

# Crear el array inicial
invitados_paintball = ["Gustavo", "Emmanuel", "Nayelis", "Génesis", "Jafet", "Raysha", "José", "Ián"]
print("📋 Lista de invitados inicial:")
print(invitados_paintball)

# Preguntar cuántos datos quiere agregar al arreglo
num_nuevos_datos = int(input("🖐️ ¿Cuantas personas invitarás? "))

# Rutina de repetición para ingresar nuevos valores utilizando append()
for i in range(num_nuevos_datos):
    nuevo_invitado = input("🙋‍♂️ Ingrese el nuevo invitado: ")
    invitados_paintball.append(nuevo_invitado)
    print("👥 Así será la lista de invitados:")
    print(invitados_paintball)

# Usar los comandos count(), insert(), len() y modificar el valor en la posición [3]
print("#️⃣ Número de invitados al Paintball:", len(invitados_paintball))
print("🔣 Número de veces que aparece 'Génesis':", invitados_paintball.count("Génesis"))
nuevo_valor = input("3️⃣ Ingrese el nuevo invitado para la posición [3]: ")
invitados_paintball[3] = nuevo_valor
print("👥 Lista de invitados después de modificar la posición [3]:")
print(invitados_paintball)

# Ordenar el arreglo utilizando sort()
invitados_paintball.sort()
print("🧹 La lista de invitados después de ordenarla:")
print(invitados_paintball)

# Mostrar el contenido del arreglo utilizando un bucle for
print("🔁 Lista de invitados en bucle FOR.")
for invitado in invitados_paintball:
    print(invitado)
