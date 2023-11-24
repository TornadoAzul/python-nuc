# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 9 de septiembre de 2023.
# Tarea 2.2.

# Explicación:
# Creará un recibo donde calcule los impuestos y el total de una
# compra de 5 productos en total que el usuario decidirá su valor.

# Acá deberá el usuario ingresar el valor de cada producto.
productos = []
for i in range(5):
    producto = float(input(f"🛍️ ¿Cual es el valor del producto {i + 1}?: "))
    productos.append(producto)

# Aquí calculamos el total de la compra.
totalcompra = sum(productos)

# Acá calculamos el total de los impuestos.
ivuestatal = totalcompra * 0.07
ivumunicipal = totalcompra * 0.015

# Ahora sumamos el total de compra y el de los impuestos.
totalpagar = totalcompra + ivuestatal + ivumunicipal

# Aquí se obtienen las posibles propinas.
propina_a = totalpagar * 0.15
propina_b = totalpagar * 0.18
propina_c = totalpagar * 0.20

# Imprimir el recibo de compras
print("\nRecibo de Barceloneta Diamante Store")
print("~ ~ ~ { 💎 = 💠 = 💎 } ~ ~ ~")
for i, producto in enumerate(productos, start=1):
    print(f"💎 Producto {i}: ${producto:.2f}")
print(f"🧮 Total de Compra: ${totalcompra:.2f}")
print(f"🇵🇷 IVU Estatal (7%): ${ivuestatal:.2f}")
print(f"🏙️ IVU Municipal (1.5%): ${ivumunicipal:.2f}")
print(f"💯 Total a Pagar: ${totalpagar:.2f}")
print(f"💙 Propina Sugerida (15%): ${propina_a:.2f}")
print(f"💚 Propina Sugerida (18%): ${propina_b:.2f}")
print(f"🧡 Propina Sugerida (20%): ${propina_c:.2f}")