from Persona import Persona

class Empleado(Persona):

    def __init__(self, id, nombre, apellido, correo, contrasena, cargo, salario,tipo_contrato):
        super().__init__(id,nombre,apellido,correo,contrasena)
        self.cargo = cargo
        self._salario = salario
        self._tipo_contrato = tipo_contrato

        #GET
    @property
    def salario (self, salario):
        return self._salario

    #Set
    @salario.setter
    def cargo (self, salario):
        self._salario = salario

    #GET
    @property
    def tipo_contrato(self, tipo_contrato):
        return self._tipo_contrato

    #Set
    @tipo_contrato.setter
    def cargo(self,tipo_contrato):
        self._tipo_contrato = tipo_contrato


    ##Se sobreescriben los métodos
    def registrar_usuario(self):
        id = input(f"Ingrese el id del usuario")
        nombre = input(f"Ingrese el nombre del usuario")
        apellido = input(f"ingrese el apellido del usuario")
        correo = input(f"Ingrese el correo del usuario")
        contrasena = input(f"Ingrese la contraseña del usuario")
        salario = float(input(f"Ingrese la contraseña del usuario"))
        cargo = input(f"Ingrese la contraseña del usuario")
        tipo_contrato = input(f"Ingrese la contraseña del usuario")

    def imprimir_registro(self):
        super().imprimir_registro()
        print(f"Cargo: {self._cargo} Salario: {self._salario} Tipo de contrato {self._tipo_contrato}")



    def iniciar_sesion(self):
        correo_emp=input("Ingrese el correo registrado")
        contras_emp=input("Ingrese la contraseña: ")

        if correo_emp == self._correo and contras_emp == self._contrasena:
            return True
        else:
            return False


    def appEmpleado(self, iniciar_sesion, imprimir_registro):
        iniciar_sesion(True)
        imprimir_registro()