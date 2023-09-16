#Las tuplas son similares a las listas, ya que se pueden ingresar distintos tipos de datos, pero a diferencia de las listas, estas
#son inmutables, ya que no se pueden modificar
#Si se requiere añadir algo, se debe convertir primero en una lista y después de ello se puede modificar la TUPLA
# Se puede acceder la tupla indicando el índice de la misma, el índice comienza desde cero
#Para recorrer la tupla usamos el ciclo FOR
# Podeos hacer JOINS entre tuplas (a una tupla añadirle otra tupla que tenga)
# Para reconocer el tamaño usamos la funcion: len()

dias_semana = ("Lunes", "Martes", "Miercoles","Jueves", "Viernes", "Sabado", "Domingo")
print(type(dias_semana))

"""#Son inmutables
print(dir(dias_semana))

#Imprime el tamaño de la lista
print(len(dias_semana))

#Mostrar que hay en cada posición []
print(dias_semana[0])
print(dias_semana[1])
print(dias_semana[2])
print(dias_semana[3])
print(dias_semana[4])
print(dias_semana[5])
print(dias_semana[6])
print(dias_semana[7])"""

"""#Podemos hacer slicing indicando el rango que queremos imprimir
print(dias_semana[:6])
print(dias_semana[0:])
print(dias_semana[-1:])
print(dias_semana[2:5])


#Para recorrer la tupla usamos FOR para iterar por los indices
for i in range (len(dias_semana)):
    print(i)
"""
#Para cambiar algún valor de la tupla o añadir, debemos primero convertirla a una lista:
dias_semana_lista = list(dias_semana)

print(type(dias_semana_lista)) 

dias_semana_lista.append("Festivo")

print(dias_semana_lista[:8])

dias_semana_lista.pop()

dias_semana=tuple(dias_semana_lista)
print(type(dias_semana))