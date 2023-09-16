#Los set son conjuntos, son más rígidos
# Los conjuntos son inmutables
# Son desordenados, quiere decir que cuando se imprime no se tiene certeza en el orden que los mostrará
# Son indexados
# No permite duplicados

vocales = {"a", "e", "i", "o", "u"}
print(len(vocales))
print(type(vocales))

# Para recorrer los conjuntos se usa IN
for i in vocales:
    print(vocales)
    print("---------------")

for i in vocales:
    print(vocales)
    print("---------------")

for i in vocales:
    print(vocales)
    print("---------------")

#Los diccionarios tiene el método add y el método remove, ya que permite que el conjunto creado se le pueda añadir o eliminar (no son inmutables totalmente)

vocales.add("@")
for i in vocales:
    print(vocales)

#Podemos remover

vocales.remove("@")
for i in vocales:
    print(vocales)

    # Elimina cualquiera al asar
vocales.pop()
for i in vocales:
    print(vocales)

