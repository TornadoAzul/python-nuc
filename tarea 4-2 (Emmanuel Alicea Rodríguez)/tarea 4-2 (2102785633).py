# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 23 de septiembre de 2023.
# Tarea 4.1.

# Explicación:
# Usando estructura de datos, calculamos los cargos
# del Hotel Sabana Hoyos en su estadía.

# Acá está el módulo completo.
def calcular_precio_estadia(num_personas, es_negocio, personas_mayores):
    # Estos son los precios.
    precios_base = {
        1: 75.00,
        2: 85.00,
        3: 90.00,
        4: 95.00
    }

    # Acá el cargo adicional.
    cargo_adicional = 20.00

    # De ser un negocio, hay descuento.
    descuento_negocio = 0.20

    # De ser mayor de 60 años, también tiene un descuento.
    descuento_persona_mayor = 0.15

    # Acá calculamos el precio base.
    if num_personas <= 4:
        precio_total = precios_base[num_personas]
    else:
        precio_total = precios_base[4] + (num_personas - 4) * cargo_adicional

    # Aquí se aplican los descuentos.
    if es_negocio and not personas_mayores:
        precio_total *= (1 - descuento_negocio)
    elif personas_mayores and not es_negocio:
        precio_total *= (1 - descuento_persona_mayor)

    return precio_total

# Este es el programa persé.
if __name__ == "__main__":
    try:
        num_personas = int(input("🏨 ¡Bienvenido al Hotel Sabana Hoyos!\n👥 ¿Cuantos se hospedarán?: "))
        es_negocio = input("👨‍💼 ¿Es parte del programa Hotel Sabana Hoyos for Business? (Sí/No): ").strip().lower() == "sí"
        personas_mayores = input("👵 ¿Alguien de los que se hospedará tiene 60 años? (Sí/No): ").strip().lower() == "sí"

        costo_estadia = calcular_precio_estadia(num_personas, es_negocio, personas_mayores)

        print(f"💸 El costo total de la estadía en Hotel Sabana Hoyos es: ${costo_estadia:.2f}")
    except ValueError:
        print("🚨 Por favor, ingrese un número válido de personas.")