# Emmanuel Alicea Rodríguez.
# Número de estudiante: 2102785633.
# Sábado, 13 de octubre de 2023.
# Tarea 7.1.

# Explicación:
# Este programa creará una ventana en Python con un formulario.

# Acá importamos la librería.
import tkinter as tk

# Acá definimos el mensaje.
def mostrar_mensaje():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    modalidad = radio_var.get()
    intereses = [check_var1.get(), check_var2.get(), check_var3.get()]

    mensaje = f"🙋‍♂️ ¡Saludos, {nombre} {apellido}! Usted ha seleccionado modalidad "
    if modalidad == 1:
        mensaje += "ONLINE"
    else:
        mensaje += "PRESENCIAL"

    mensaje += ", indicando interés en: "
    intereses_seleccionados = []
    if intereses[0]:
        intereses_seleccionados.append("Web Development")
    if intereses[1]:
        intereses_seleccionados.append("System Analyst")
    if intereses[2]:
        intereses_seleccionados.append("Otro Interés")
    
    mensaje += ", ".join(intereses_seleccionados)
    mensaje_label.config(text=mensaje)

# Acá presentamos la ventana del formulario.
root = tk.Tk()
root.title("Formulario")

# Acá creamos los elementos y los posicionamos.
label_titulo = tk.Label(root, text="Formulario de Intereses")
label_titulo.pack()

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

check_var1 = tk.IntVar()
check_var2 = tk.IntVar()
check_var3 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Web Development", variable=check_var1)
check1.pack()
check2 = tk.Checkbutton(root, text="System Analyst", variable=check_var2)
check2.pack()
check3 = tk.Checkbutton(root, text="Otro Interés", variable=check_var3)
check3.pack()

radio_var = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Presencial", variable=radio_var, value=0)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Online", variable=radio_var, value=1)
radio2.pack()

boton_mostrar = tk.Button(root, text="Mostrar ahora", command=mostrar_mensaje)
boton_mostrar.pack()

mensaje_label = tk.Label(root, text="")
mensaje_label.pack()

# Ahora iniciamos el bucle.
root.mainloop()