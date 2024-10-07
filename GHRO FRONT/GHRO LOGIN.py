import customtkinter

import customtkinter as ctk

import customtkinter as ctk
import tkinter.messagebox as messagebox

# Configuración de la apariencia de customtkinter
ctk.set_appearance_mode("Light")  # Puedes cambiar a "Dark" si lo prefieres
ctk.set_default_color_theme("blue")  # Cambia el tema de color si lo deseas

# Función para manejar el evento de inicio de sesión
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Aquí puedes agregar lógica de validación (por ejemplo, comparar con datos de una base de datos)
    if username == "usuario" and password == "contraseña":  # Cambia esto a tus credenciales
        messagebox.showinfo("Inicio de sesión exitoso", f"Bienvenido, {username}!")
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos.")

# Crear la ventana principal
app = ctk.CTk()
app.title("Bienvenido a Ghro")
app.geometry("400x300")

# Crear los widgets
label_username = ctk.CTkLabel(app, text="Nombre de usuario:")
label_username.pack(pady=(20, 5))

entry_username = ctk.CTkEntry(app)
entry_username.pack(pady=(0, 10))

label_password = ctk.CTkLabel(app, text="Contraseña:")
label_password.pack(pady=(10, 5))

entry_password = ctk.CTkEntry(app, show='*')
entry_password.pack(pady=(0, 20))

button_login = ctk.CTkButton(app, text="Iniciar sesión", command=login)
button_login.pack(pady=(10, 0))

# Iniciar el bucle de la interfaz
app.mainloop()

