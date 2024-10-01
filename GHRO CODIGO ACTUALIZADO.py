class Hotel:
    def __init__(self):
        self.habitaciones = {
            101: {'tipo': 'Individual', 'disponible': True, 'precio': 100},
            102: {'tipo': 'Doble', 'disponible': True, 'precio': 150},
            103: {'tipo': 'Suite', 'disponible': True, 'precio': 250},
            104: {'tipo': 'Familiar', 'disponible': True, 'precio': 200},
            105: {'tipo': 'Doble', 'disponible': True, 'precio': 150},
        }
        self.promociones = {
            'DESC10': 0.10,  # 10% de descuento
            'DESC20': 0.20,  # 20% de descuento
        }

    def mostrar_habitaciones(self):
        print("Habitaciones disponibles:")
        for numero, info in self.habitaciones.items():
            estado = "Disponible" if info['disponible'] else "No disponible"
            print(f"Habitación {numero}: Tipo {info['tipo']} - Precio ${info['precio']} - {estado}")

    def reservar_habitacion(self, numero_habitacion):
        if numero_habitacion in self.habitaciones:
            if self.habitaciones[numero_habitacion]['disponible']:
                self.habitaciones[numero_habitacion]['disponible'] = False
                return self.habitaciones[numero_habitacion]['precio']
            else:
                print(f"Habitación {numero_habitacion} no está disponible.")
                return None
        else:
            print("Número de habitación inválido.")
            return None

    def aplicar_promocion(self, codigo_promocion, precio):
        if codigo_promocion in self.promociones:
            descuento = self.promociones[codigo_promocion]
            precio_final = precio * (1 - descuento)
            print(f"Promoción aplicada: {codigo_promocion} - Precio final: ${precio_final:.2f}")
            return precio_final
        else:
            print("Código de promoción inválido.")
            return precio

    def procesar_pago(self, cantidad):
        print(f"Procesando pago de ${cantidad:.2f}...")
        # Aquí puedes agregar lógica para procesar el pago
        print("Pago realizado exitosamente.")

def main():
    hotel = Hotel()
    while True:
        print("\nBienvenido al sistema de reservas del hotel.")
        print("1. Mostrar habitaciones disponibles")
        print("2. Reservar habitación")
        print("3. Ingresar código de promoción")
        print("4. Salir")

        opcion = input("Seleccione una opción (1, 2, 3, 4): ")

        if opcion == '1':
            hotel.mostrar_habitaciones()
        elif opcion == '2':
            try:
                numero_habitacion = int(input("Ingrese el número de habitación que desea reservar: "))
                precio = hotel.reservar_habitacion(numero_habitacion)
                if precio is not None:
                    # Confirmación de la reserva
                    confirmacion = input(f"Confirme su reserva para la habitación {numero_habitacion} (s/n): ")
                    if confirmacion.lower() == 's':
                        # Solicitar código de promoción
                        codigo_promocion = input("Ingrese un código de promoción (o presione Enter para omitir): ")
                        precio_final = hotel.aplicar_promocion(codigo_promocion, precio)
                        hotel.procesar_pago(precio_final)
                    else:
                        print("Reserva cancelada.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == '3':
            print("Funcionalidad de ingreso de promoción ya incluida durante la reserva.")
        elif opcion == '4':
            print("Gracias por usar el sistema de reservas. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
