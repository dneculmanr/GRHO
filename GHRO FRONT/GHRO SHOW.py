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


# Función para mostrar las habitaciones
def mostrar_habitaciones():
    habitaciones = hotel.mostrar_habitaciones()
    messagebox.showinfo("Habitaciones Disponibles", habitaciones)

# Crear la instancia del hotel
hotel = Hotel()

# Crear la ventana principal
app = ctk.CTk()
app.title("Mostrar Habitaciones del Hotel")
app.geometry("400x200")

# Crear el botón para mostrar habitaciones
button_mostrar = ctk.CTkButton(app, text="Mostrar Habitaciones", command=mostrar_habitaciones)
button_mostrar.pack(pady=(50, 20))

# Iniciar el bucle de la interfaz
app.mainloop()

