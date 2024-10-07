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

    def reservar_habitacion(self, numero_habitacion):
        if numero_habitacion in self.habitaciones:
            if self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = False
                return f"Habitación {numero_habitacion} reservada exitosamente."
            else:
                return f"Habitación {numero_habitacion} no está disponible."
        else:
            return "Número de habitación inválido."


# Función para reservar una habitación
def reservar_habitacion():
    try:
        numero_habitacion = int(entry_habitacion.get())
        resultado = hotel.reservar_habitacion(numero_habitacion)
        messagebox.showinfo("Resultado de la Reserva", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un número válido.")

# Crear la instancia del hotel
hotel = Hotel()

# Crear la ventana principal
app = ctk.CTk()
app.title("Reservar Habitación del Hotel")
app.geometry("400x300")

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
