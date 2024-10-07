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
        self.reservas = {}  # Para almacenar las reservas realizadas

    def mostrar_habitaciones(self):
        habitaciones_disponibles = "Habitaciones disponibles:\n"
        for numero, info in self.habitaciones.items():
            estado = "Disponible" if info['disponible'] else "No disponible"
            habitaciones_disponibles += f"Habitación {numero}: Tipo {info['tipo']} - {estado}\n"
        return habitaciones_disponibles.strip()

    def reservar_habitacion(self, numero_habitacion, nombre_cliente):
        if numero_habitacion in self.habitaciones:
            if self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = False
                self.reservas[numero_habitacion] = nombre_cliente  # Guardar la reserva
                return f"Habitación {numero_habitacion} reservada exitosamente para {nombre_cliente}."
            else:
                return f"Habitación {numero_habitacion} no está disponible."
        else:
            return "Número de habitación inválido."

    def check_in(self, numero_habitacion, nombre_cliente):
        if numero_habitacion in self.habitaciones and nombre_cliente in self.reservas.values():
            if not self.habitaciones[numero_habitacion]['disponible']:
                return f"Check In exitoso para {nombre_cliente} en la habitación {numero_habitacion}."
            else:
                return "La habitación está disponible. No hay reservas."
        else:
            return "Número de habitación inválido o cliente no reservado."

    def check_out(self, numero_habitacion):
        if numero_habitacion in self.habitaciones:
            if not self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = True
                if numero_habitacion in self.reservas:
                    del self.reservas[numero_habitacion]  # Eliminar la reserva
                return f"Check Out exitoso de la habitación {numero_habitacion}."
            else:
                return "La habitación ya está disponible."
        else:
            return "Número de habitación inválido."


# Clase para la ventana de login
class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x200")

        self.label_username = ctk.CTkLabel(master, text="Usuario:")
        self.label_username.pack(pady=(20, 5))

        self.entry_username = ctk.CTkEntry(master)
        self.entry_username.pack(pady=(0, 10))

        self.label_password = ctk.CTkLabel(master, text="Contraseña:")
        self.label_password.pack(pady=(10, 5))

        self.entry_password = ctk.CTkEntry(master, show='*')
        self.entry_password.pack(pady=(0, 20))

        self.button_login = ctk.CTkButton(master, text="Iniciar Sesión", command=self.login)
        self.button_login.pack(pady=(10, 0))

        self.hotel = Hotel()  # Instancia del hotel

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "recepcion" and password == "adminrecepcion":
            messagebox.showinfo("Login", "Inicio de sesión exitoso.")
            self.master.destroy()  # Cierra la ventana de login
            self.show_main_menu()  # Muestra el menú principal
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

    def show_main_menu(self):
        menu_window = ctk.CTkToplevel()
        menu_window.title("Menú Principal")
        menu_window.geometry("400x400")

        button_habitaciones = ctk.CTkButton(menu_window, text="Habitaciones Disponibles", command=self.mostrar_habitaciones)
        button_habitaciones.pack(pady=(20, 10))

        button_reservas = ctk.CTkButton(menu_window, text="Reservas", command=self.hacer_reserva)
        button_reservas.pack(pady=(10, 10))

        button_check_in = ctk.CTkButton(menu_window, text="Check In", command=self.check_in)
        button_check_in.pack(pady=(10, 10))

        button_check_out = ctk.CTkButton(menu_window, text="Check Out", command=self.check_out)
        button_check_out.pack(pady=(10, 10))

    def mostrar_habitaciones(self):
        habitaciones = self.hotel.mostrar_habitaciones()
        messagebox.showinfo("Habitaciones Disponibles", habitaciones)

    def hacer_reserva(self):
        reserva_window = ctk.CTkToplevel()
        reserva_window.title("Reservar Habitación")
        reserva_window.geometry("300x200")

        label_habitacion = ctk.CTkLabel(reserva_window, text="Número de habitación:")
        label_habitacion.pack(pady=(20, 5))

        entry_habitacion = ctk.CTkEntry(reserva_window)
        entry_habitacion.pack(pady=(0, 10))

        label_cliente = ctk.CTkLabel(reserva_window, text="Nombre del cliente:")
        label_cliente.pack(pady=(10, 5))

        entry_cliente = ctk.CTkEntry(reserva_window)
        entry_cliente.pack(pady=(0, 10))

        button_reservar = ctk.CTkButton(reserva_window, text="Reservar", command=lambda: self.reservar_habitacion(entry_habitacion.get(), entry_cliente.get()))
        button_reservar.pack(pady=(10, 0))

    def reservar_habitacion(self, numero_habitacion, nombre_cliente):
        try:
            numero_habitacion = int(numero_habitacion)
            resultado = self.hotel.reservar_habitacion(numero_habitacion, nombre_cliente)
            messagebox.showinfo("Resultado de la Reserva", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para la habitación.")

    def check_in(self):
        check_in_window = ctk.CTkToplevel()
        check_in_window.title("Check In")
        check_in_window.geometry("300x200")

        label_habitacion = ctk.CTkLabel(check_in_window, text="Número de habitación:")
        label_habitacion.pack(pady=(20, 5))

        entry_habitacion = ctk.CTkEntry(check_in_window)
        entry_habitacion.pack(pady=(0, 10))

        label_cliente = ctk.CTkLabel(check_in_window, text="Nombre del cliente:")
        label_cliente.pack(pady=(10, 5))

        entry_cliente = ctk.CTkEntry(check_in_window)
        entry_cliente.pack(pady=(0, 10))

        button_check_in = ctk.CTkButton(check_in_window, text="Check In", command=lambda: self.procesar_check_in(entry_habitacion.get(), entry_cliente.get()))
        button_check_in.pack(pady=(10, 0))

    def procesar_check_in(self, numero_habitacion, nombre_cliente):
        try:
            numero_habitacion = int(numero_habitacion)
            resultado = self.hotel.check_in(numero_habitacion, nombre_cliente)
            messagebox.showinfo("Resultado de Check In", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para la habitación.")

    def check_out(self):
        check_out_window = ctk.CTkToplevel()
        check_out_window.title("Check Out")
        check_out_window.geometry("300x200")

        label_habitacion = ctk.CTkLabel(check_out_window, text="Número de habitación:")
        label_habitacion.pack(pady=(20, 5))

        entry_habitacion = ctk.CTkEntry(check_out_window)
        entry_habitacion.pack(pady=(0, 10))

        button_check_out = ctk.CTkButton(check_out_window, text="Check Out", command=lambda: self.procesar_check_out(entry_habitacion.get()))
        button_check_out.pack(pady=(10, 0))

    def procesar_check_out(self, numero_habitacion):
        try:
            numero_habitacion = int(numero_habitacion)
            resultado = self.hotel.check_out(numero_habitacion)
            messagebox.showinfo("Resultado de Check Out", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para la habitación.")


# Crear la ventana principal
if __name__ == "__main__":
    root = ctk.CTk()
    app = LoginWindow(root)
    root.mainloop()

