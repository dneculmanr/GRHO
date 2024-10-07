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
        print("Habitaciones disponibles:")
        for numero, info in self.habitaciones.items():
            estado = "Disponible" if info['disponible'] else "No disponible"
            print(f"Habitación {numero}: Tipo {info['tipo']} - {estado}")

    def reservar_habitacion(self, numero_habitacion):
        if numero_habitacion in self.habitaciones:
            if self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = False
                print(f"Habitación {numero_habitacion} reservada exitosamente.")
            else:
                print(f"Habitación {numero_habitacion} no está disponible.")
        else:
            print("Número de habitación inválido.")

def main():
    hotel = Hotel()
    while True:
        print("\nBienvenido al sistema de reservas del hotel.")
        print("1. Mostrar habitaciones disponibles")
        print("2. Reservar habitación")
        print("3. Salir")

        opcion = input("Seleccione una opción (1, 2, 3): ")

        if opcion == '1':
            hotel.mostrar_habitaciones()
        elif opcion == '2':
            try:
                numero_habitacion = int(input("Ingrese el número de habitación que desea reservar: "))
                hotel.reservar_habitacion(numero_habitacion)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '3':
            print("Gracias por usar el sistema de reservas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

if __name__ == "__main__":
    main()
