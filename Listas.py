#Las litas son estructuras de datos lineales, se crean usando un bracket. Ejmplo: My list[]
#Las listas son ordenanas (orden de sincercion), es decir, el último dato tiene la ultima posicion
#Emplea metodos para manejar items de la misma como los array, su primer posicion es 0
#permite items duplicados, son mutables, es decir se puede agregar, actualizar o mover items
#puede contener distintos tipos de datos

nombres=["Juan","Pepito","Maria", "Lisa"]

#El metodo len() valida el tamaño de la lista
print(len(nombres))
print(type(nombres))

listaDatos =["Pedro", "Perez", 100100100, 1.80, True]
print(f" El numero de documento es: {listaDatos[2]}")

#Slicing de datos
print(listaDatos[0:2])
#Para imprimir los elementos entre apellido y altura
print(listaDatos[1:4])
#Que imprima todo menos TRUE
print(listaDatos[4])
#Para que imprima del dos hasta el último
print(listaDatos[2:1])
#Para que imprima de adelante hacia atrás
print(listaDatos[:-1])
print(listaDatos[:-2])
print(listaDatos[:-3])
print(listaDatos[-4:-1])
print(listaDatos[1:4])