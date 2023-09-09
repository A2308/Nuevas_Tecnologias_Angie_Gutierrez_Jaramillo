#Reciban por consola el valor de una compra
#Poder ingresar el numero de cuotas
#Calcular el valor de la cuota
#Usando WHILE mostrar el plan de pago y muestre el cupo liberado por cada pago

#MÍO
valCompra = int(input("Ingrese el valor de su compra "))
cuotas = int(input("Ingrese a cuantas cuotas lo desea registrar "))
total=valCompra/cuotas
print("El total de su credito es de: ", total)

CantCuotas = int(input("Ingrese valor de pago"))

while CantCuotas == cuotas and valCompra != 0:
    valCompra-=CantCuotas
    print(CantCuotas)
    
    
    
    #COMPAÑEROS
