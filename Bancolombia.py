
empleados = {
    1: {"id": 1, "nombres": "Angie", "apellidos": "Gutierrez", "cargo": "Desarrolladora", "area": "Tecnología", "salario": 2000000},
    2: {"id": 2, "nombres": "Andres", "apellidos": "David", "cargo": "Analista", "area": "Gestión Humana", "salario": 1800000},

}


def calcular_salario_neto(salario):
    salario_minimo = 1160000
    if salario < 2 * salario_minimo:
        salario_neto = salario + 106454  
    else:
        salario_neto = salario
    return salario_neto


def gestionar_nominas():
    while True:
        print("\n1. Listar empleados\n2. Buscar colilla de pago\n3. Ver pago total de la nómina\n4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Lista de empleados:")
            for empleado in empleados.values():
                print(f"{empleado['id']}. {empleado['nombres']} {empleado['apellidos']}")

        elif opcion == "2":
            id_empleado = int(input("Ingrese el ID del empleado: "))
            empleado = empleados.get(id_empleado)
            if empleado:
                salario_neto = calcular_salario_neto(empleado["salario"])
                print(f"Colilla de pago para {empleado['nombres']} {empleado['apellidos']}:")
                print(f"Cargo: {empleado['cargo']}")
                print(f"Área: {empleado['area']}")
                print(f"Salario Neto: {salario_neto}")
            else:
                print("Empleado no encontrado.")

        elif opcion == "3":
            total_nominas = sum(calcular_salario_neto(empleado["salario"]) for empleado in empleados.values())
            print(f"Pago total de la nómina: {total_nominas}")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtelo de nuevo.")

gestionar_nominas()
