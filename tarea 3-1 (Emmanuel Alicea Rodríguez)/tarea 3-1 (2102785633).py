# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Miercoles, 13 de septiembre de 2023.
# Tarea 3.1.

# Explicación:
# Este porgrama te dirá cuales monedas serán necesarias para llegar
# al valor necesario para llegar a lo que el usuario ingresó.

# Acá se define para cacular el valor monetario que el usuario ingresó.
def validar_valor_monetario():
    while True:
        valor_monetario = input("🙌 ¡Ingresa un valor monetario y te diré qué monedas necesitarás!: ")
        try:
            valor_monetario = float(valor_monetario)
            if valor_monetario >= 0:
                return valor_monetario
            else:
                print("¡Uy! El valor no puede ser cero. 😬")
        except ValueError:
            print("¡Esto no es un valor monetario! Ej: 1.23, 24.32 o 33.00. 💸")

# Acá se desglosa el valor monetario que el usuario ingresó.
def desglosar_efectivo(valor):
    denominaciones = [20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01]
    nombres_denominaciones = ["billetes de $20", "billetes de $10", "billetes de $5", "billetes de $1", "centavos de 25", "centavos de 10", "centavos de 5", "centavos de 1"]

    print(f"💵 Desglose de ${valor:.2f} en denominaciones:")
    # Ahora duplicamos las valoraciones en diferentes monedas.
    for i in range(len(denominaciones)):
        cantidad = int(valor // denominaciones[i])
        if cantidad > 0:
            # Imprimimos las monedas y sus valores.
            print(f"{cantidad} {nombres_denominaciones[i]}")
            valor -= cantidad * denominaciones[i]

# Acá se llaman las funciones requeridas.
if __name__ == "__main__":
    valor = validar_valor_monetario()  # Solicitar valor.
    desglosar_efectivo(valor)  # Acá la tabla de contenido.