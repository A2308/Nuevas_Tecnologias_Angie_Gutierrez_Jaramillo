# Para crear una clase en python, usamos la palabra
# Class



class Persona:

    # AHora vamos a crear un metodo constructor

    def __init__(self, id: object, nombre: object, apellido: object, correo: object, password: object) -> object:
        self._id = id
        self._nombre = nombre
        self._apellido= apellido
        self._correo = correo
        self._password = password
        # Este contiene la palabrada reservada self, similar a this en Java, por ejemplo

        # encapsulamiento con python
        # Se usa underscore al principio de la variable para indiccar que sera encapsulada.
        # Ahora usaremos decoradores para crear los getter y setters
        # @property ? > indica los getters
        # @var.setter => indica los getters

        #Esto es un setter

        # Esto es un getter

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self,id):
            self._id=id


        #Vamos a hacer lo mismp para cada uno de los

        @property
        def nombre(self):
            return self._nombre

        @nombre.setter
        def nombre(self,nombre):
            self._nombre= nombre

        @property
        def apellido(self):
            return self._apellido

        @apellido.setter
        def apellido(self, apellido):
            self._apellido = apellido

        @property
        def correo(self):
            return self._correo

        @correo.setter
        def correo(self, correo):
            self._correo = correo

        @property
        def password(self):
            return self._password

        @apellido.setter
        def password(self,password):
            self._password = password



    def imprimir_persona(self):
        print(f"Id: {self._id} nombre: {self._nombre} apellido {self._apellido}")