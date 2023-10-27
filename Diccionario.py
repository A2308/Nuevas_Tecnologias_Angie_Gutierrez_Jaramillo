#Los diccionarios permiten tener clave : valor
# Son cambiables
# No permiten duplicados
# Desde Python 3.7 son ordenadas
# Permiten agregar, remover items
# Son iterables
# Poseen distintos metodos para manipular los datos
# Admiten distintos tipos de datos

usuario = {"nombre":"Pepito",
            "Apellido": "Perez",
            "Edad": 25}

#Imprime las claves
print(usuario.keys())

# Imprime los valores
print(usuario.values())

#Para conocer el tamaño del diccionario usamos el metodo len()
print(len(usuario))
print(type(usuario))

#Cuando queremos buscar un item especifico podemos usar get()
print(usuario.get("nombre"))
print(usuario["nombre"])

#Podemos agregar nuevos items
usuario["correo"] = "pepito@gmail.com"
print(usuario.keys)
print(usuario.get("correo"))

#Podemos actualizar un valor 
usuario.update({"correo":"pperez@gmail.com"})

print(usuario.get("correo"))

#Para remover
"""
usuario.pop("nombre")
print(usuario.keys())
usuario.popitem()
print(usuario.keys())
del usuario["Edad"]
print(usuario.keys())
"""

#Para recorrer el diccionario podemos elegir entre: recorrer las claves, recorrer los valores o recorrer ambos

#AMBOS
for x,y in usuario.items():
    print(x,y)

#RECORRER CLAVES
for x in usuario.keys:
    print(x)

#RECORRER VALORES
for y in usuario.values():
    print(y)

# Podemos tener un diccionario de diccionarios
usuarios = {"usuario1":{"nombre":"Juan", "Edad":12}, "usuario2":{"nombre":"Maria", "Edad": 15}, "usuario3":{"nombre":"Julia", "Edad":18}}

estudiante1 = {"nota1":4.5, "nota2":4.3}
estudiante2 = {"nota1":4.0, "nota2":3.3}
estudiante3 = {"nota1":3.5, "nota2":2.3}

estudiantes = {
    "estudiante1":estudiante1,
    "estudiante2":estudiante2,
    "estudiante3":estudiante3
}
print(estudiantes["estudiante2"]["nota2"])
