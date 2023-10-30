class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = 0.2  
        self.precio_de_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        try:
            precio_venta = self.costo / (1 - self.margen_de_venta)
            return round(precio_venta, 2)
        except ZeroDivisionError:
            print("Error: El margen de venta no puede ser 1 (100%)")
            return None

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto
            print(f"Producto '{producto.nombre}' agregado correctamente.")
        else:
            print(f"Error: Producto con ID '{producto.id}' ya existe en el inventario.")

    def imprimir_productos(self):
        print("Listado de Productos:")
        for producto_id, producto in self.productos.items():
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Descripción: {producto.descripcion},"
                  f" Costo: {producto.costo}, Cantidad: {producto.cantidad}, Precio de Venta: {producto.precio_de_venta}")


if __name__ == "__main__":
    inventario = Inventario()

    
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    costo = float(input("Ingrese el costo del producto: "))

    
    producto = Producto(id=id, nombre=nombre, descripcion="", costo=costo, cantidad=cantidad)
    
    inventario.agregar_producto(producto)
    inventario.imprimir_productos()

