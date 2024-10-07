import customtkinter as ctk
import tkinter.messagebox as messagebox

class Hotel:
    def __init__(self):
        self.habitaciones = {
            101: {'tipo': 'Individual', 'disponible': True},
            102: {'tipo': 'Doble', 'disponible': True},
            103: {'tipo': 'Suite', 'disponible': True},
            104: {'tipo': 'Familiar', 'disponible': True},
            105: {'tipo': 'Doble', 'disponible': True},
        }

    def mostrar_habitaciones(self):
        habitaciones_disponibles = "Habitaciones disponibles:\n"
        for numero, info in self.habitaciones.items():
            estado = "Disponible" if info['disponible'] else "No disponible"
            habitaciones_disponibles += f"Habitación {numero}: Tipo {info['tipo']} - {estado}\n"
        return habitaciones_disponibles.strip()

    def reservar_habitacion(self, numero_habitacion):
        if numero_habitacion in self.habitaciones:
            if self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = False
                return f"Habitación {numero_habitacion} reservada exitosamente."
            else:
                return f"Habitación {numero_habitacion} no está disponible."
        else:
            return "Número de habitación inválido."


# Funciones para la interfaz gráfica
def mostrar_habitaciones():
    habitaciones = hotel.mostrar_habitaciones()
    messagebox.showinfo("Habitaciones Disponibles", habitaciones)

def reservar_habitacion():
    try:
        numero_habitacion = int(entry_habitacion.get())
        resultado = hotel.reservar_habitacion(numero_habitacion)
        messagebox.showinfo("Resultado de la Reserva", resultado)
        entry_habitacion.delete(0, ctk.END)  # Limpiar la entrada
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Crear la instancia del hotel
hotel = Hotel()

# Crear la ventana principal
app = ctk.CTk()
app.title("Sistema de Reservas del Hotel")
app.geometry("400x400")

# Crear el botón para mostrar habitaciones
button_mostrar = ctk.CTkButton(app, text="Mostrar Habitaciones", command=mostrar_habitaciones)
button_mostrar.pack(pady=(20, 10))

# Crear la entrada para el número de habitación
label_habitacion = ctk.CTkLabel(app, text="Ingrese número de habitación:")
label_habitacion.pack(pady=(20, 5))

entry_habitacion = ctk.CTkEntry(app)
entry_habitacion.pack(pady=(0, 20))

# Crear el botón para reservar habitación
button_reservar = ctk.CTkButton(app, text="Reservar Habitación", command=reservar_habitacion)
button_reservar.pack(pady=(10, 0))

# Iniciar el bucle de la interfaz
app.mainloop()
