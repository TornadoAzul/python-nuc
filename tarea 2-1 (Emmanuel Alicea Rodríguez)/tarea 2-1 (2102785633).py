# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 9 de septiembre de 2023.
# Tarea 2.1.

# Explicación:
# El programa utiliza la función input() para solicitar al usuario que ingrese tres números, que se almacenan en las variables N1, N2 y N3.
# El programa utiliza operaciones matemáticas como la suma, multiplicación, división, raíz cuadrada y exponente para realizar cálculos con
# los números ingresados. Luego, muestra los resultados de estos cálculos en la consola, lo que demuestra cómo se pueden realizar operaciones matemáticas básicas en Python.

# Importamos el paquete "math".
import math

# Aquí se solicita al usuario los números requeridos.
N1 = int(input("5️⃣ ¡Por favor! Ingresa un número (entero) de 5 dígitos: "))
N2 = int(input("2️⃣ ¡Gracias! Ahora ingresa un número (entero) de 2 dígitos: "))
N3 = float(input("🔢 ¡Genial! Ahora un número décimal: "))

# Acá se formatean los números.
N1_formatted = f"{N1:05d}"
N2_formatted = f"{N2:02d}"
N3_formatted = f"{N3:.2f}"

# Aquí se realizan los calculos pertinentes.
A = N1 + N2 + N3
B = N1 * N2 + N3
C = N1 / N2
D = math.sqrt(N1)
E = N2 ** 2

# Acá se muestran los resultados.

print(f"🧮 Aquí los resultados:")
print(f"A = {N1} + {N2} + {N3} = {A}")
print(f"B = {N1} * {N2} + {N3} = {B}")
print(f"C = {N1} / {N2} = {C}")
print(f"D = La raíz cuadrada de {N1} = {D}")
print(f"E = {N2} es elevado a la 2 = {E}")

# Cambiamos los formatos.
N1 = float(N1)
N2 = float(N2)
N3 = int(N3)

# Redondeamos los números a décimales.
N3 = round(N3)

#Acá finaliza el programa mostrando los números convertidos.
print("\n📽️ Resultados con números convertidos:")
print(f"N1 = {N1} (decimal)")
print(f"N2 = {N2} (decimal)")
print(f"N3 = {N3} (entero)")