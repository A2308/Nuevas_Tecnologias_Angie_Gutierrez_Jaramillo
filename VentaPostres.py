import pickle

class Usuario:
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def set_username(self, username):
        self._username = username

    def get_username(self):
        return self._username

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

class Cliente(Usuario):
    def __init__(self, username, password, nombre):
        super().__init__(username, password)
        self._nombre = nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

class TiendaPostres:
    def __init__(self):
        self._usuarios_registrados = []
        self._postres_disponibles = {
            "Pastel de Chocolate": 12000,
            "Tarta de Manzana": 10000,
            "Cupcake de Vainilla": 8000,
            "Helado de Fresa": 9000,
            "Postre de Maracuyá": 11000,
            "Postre Oreo": 11000,
            "Malteadas": 10000,
        }

    def registrar_usuario(self, usuario):
        self._usuarios_registrados.append(usuario)
        self.guardar_usuarios()

    def guardar_usuarios(self):
        with open('usuarios.pkl', 'wb') as file:
            pickle.dump(self._usuarios_registrados, file)

    def cargar_usuarios(self):
        try:
            with open('usuarios.pkl', 'rb') as file:
                self._usuarios_registrados = pickle.load(file)
        except FileNotFoundError:
            self._usuarios_registrados = []

    def iniciar_sesion(self, username, password):
        self.cargar_usuarios()
        for usuario in self._usuarios_registrados:
            if usuario.get_username() == username and usuario.get_password() == password:
                return usuario
        return None

    def mostrar_postres(self):
        print("Postres Disponibles:")
        for nombre, precio in self._postres_disponibles.items():
            print(f"{nombre}: {precio} pesos")

# Ejemplo de uso
tienda = TiendaPostres()

while True:
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        usuario = tienda.iniciar_sesion(username, password)
        if usuario:
            print(f"Bienvenido, {usuario.get_nombre()}!")
            while True:
                print("1. Comprar Postres")
                print("2. Mostrar Postres Disponibles")
                print("3. Salir")
                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    tienda.mostrar_postres()
                    postre_a_comprar = input("Ingrese el nombre del postre que desea comprar: ")
                    if postre_a_comprar in tienda._postres_disponibles:
                        print(f"¡Usted ha comprado {postre_a_comprar} por {tienda._postres_disponibles[postre_a_comprar]} pesos!")
                    else:
                        print("El postre seleccionado no está disponible.")
                elif subopcion == "2":
                    tienda.mostrar_postres()
                elif subopcion == "3":
                    break
                else:
                    print("Opción inválida.")

        else:
            print("Nombre de usuario o contraseña incorrectos.")
    elif opcion == "2":
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        nombre = input("Ingrese su nombre: ")
        cliente = Cliente(username, password, nombre)
        tienda.registrar_usuario(cliente)
        print("Usuario registrado correctamente.")
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")
