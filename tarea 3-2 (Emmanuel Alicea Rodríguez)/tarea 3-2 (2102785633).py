# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Viernes, 15 de septiembre de 2023.
# Tarea 3.2.

# Explicación:
# Facilita la entrada y manipulación de fechas, incluyendo la resta y
# suma de días o semanas, el formato de fechas personalizadas y la
# modificación de días específicos.

# Acá importamos las bibliotecas requeridas.
from datetime import datetime, timedelta

# Acá se ingresa las fechas.
def ingresar_fecha():
    año = int(input("🎆 Ingresa el año: "))
    mes = int(input("🗓️ Ingresa el mes: "))
    dia = int(input("🕦 Ingresa el día: "))
    return datetime(año, mes, dia)

# Acá se resta los días de una fecha dada.
def restar_dias(fecha, cantidad_dias):
    nueva_fecha = fecha - timedelta(days=cantidad_dias)
    return nueva_fecha

# Aquí se suma los días.
def sumar_semanas(fecha, cantidad_semanas):
    nueva_fecha = fecha + timedelta(weeks=cantidad_semanas)
    return nueva_fecha

# Acá convierte en formato de fecha los datos.
def formato_fecha(fecha_str):
    fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
    return fecha

# Aquí se modifica los datos ingresados.
def modificar_dia(fecha, nuevo_dia):
    nueva_fecha = fecha.replace(day=nuevo_dia)
    return nueva_fecha

# Esta es la función principal.
def main():
    fecha_ingresada = ingresar_fecha()
    print("⭐️ ~ ~ ~ ~ ~ 👑 ~ ~ ~ ~ ~ ⭐️")

    dias_a_restar = int(input("Ingrese la cantidad de días a restar: "))
    nueva_fecha = restar_dias(fecha_ingresada, dias_a_restar)
    print(f"💙 La fecha {fecha_ingresada.strftime('%Y-%m-%d')} menos {dias_a_restar} días es {nueva_fecha.strftime('%Y-%m-%d')}")
    print("⭐️ ~ ~ ~ ~ ~ 👑 ~ ~ ~ ~ ~ ⭐️")

    semanas_a_sumar = int(input("Ingrese la cantidad de semanas a sumar: "))
    nueva_fecha = sumar_semanas(fecha_ingresada, semanas_a_sumar)
    print(f"💚 La fecha {fecha_ingresada.strftime('%Y-%m-%d')} más {semanas_a_sumar} semanas es {nueva_fecha.strftime('%Y-%m-%d')}")
    print(f"💛 La fecha {nueva_fecha.strftime('%Y-%m-%d')} es {nueva_fecha.strftime('%A').upper()}")
    print("⭐️ ~ ~ ~ ~ ~ 👑 ~ ~ ~ ~ ~ ⭐️")

    fecha_str = input("Ingrese la fecha con el formato (dd/mm/yyyy): ")
    fecha = formato_fecha(fecha_str)
    print(f"🧡 La fecha ingresada con formato %d/%m/%Y es año {fecha.year} mes {fecha.month:02d} día {fecha.day:02d}.")
    print("⭐️ ~ ~ ~ ~ ~ 👑 ~ ~ ~ ~ ~ ⭐️")

    nuevo_dia = int(input("Ingrese el número de día para modificar en la fecha: "))
    nueva_fecha = modificar_dia(fecha, nuevo_dia)
    print(f"❤️ De la fecha {fecha.strftime('%Y-%m-%d')} cambiamos el día {fecha.day:02d} por {nuevo_dia:02d}, la nueva fecha es {nueva_fecha.strftime('%Y-%m-%d')}.")

# Verificamos que esté corriendo en un programa independiente. 😎
if __name__ == "__main__":
    main()
