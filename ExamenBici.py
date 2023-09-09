registro = []
bicicletas_disponibles = [1, 2, 3, 4, 5]
prestamos = []

while True:
    print("\nAlquiler de bicicletas")
    print("1. Registrar un nuevo usuario")
    print("2. Tomar una bicicleta")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        nombre = input("Ingrese el nombre del usuario: ")
        numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
        registro.append({"nombre": nombre, "numero_tarjeta": numero_tarjeta})
        print("Usuario registrado con éxito.")

    elif opcion == "2":
        numero_tarjeta = input("Ingrese el número de tarjeta del usuario: ")
        usuario_existente = None
        for usuario in registro:
            if usuario["numero_tarjeta"] == numero_tarjeta:
                usuario_existente = usuario
                break

        if usuario_existente is None:
            print("Usuario no encontrado. Por favor, regístrese primero.")
        else:

            print("Bicicletas disponibles:")
            for bicicleta in bicicletas_disponibles:
                print(f"Bicicleta {bicicleta}")

            bicicleta_elegida = int(input("Ingrese el número de la bicicleta que desea tomar: "))

            if bicicleta_elegida in bicicletas_disponibles:
                origen = input("Ingrese el origen del viaje: ")
                destino = input("Ingrese el destino del viaje: ")

                alquiler = {
                    "usuario": usuario_existente["nombre"],
                    "bicicleta": bicicleta_elegida,
                    "origen": origen,
                    "destino": destino,
                }
                prestamos.append(alquiler)
                bicicletas_disponibles.remove(bicicleta_elegida)
                print(f"¡Bicicleta {bicicleta_elegida} alquilada!")
            else:
                print("La bicicleta seleccionada no está disponible.")

    elif opcion == "3":
        print("Gracias por usar el sistema de alquiler de bicicletas.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
