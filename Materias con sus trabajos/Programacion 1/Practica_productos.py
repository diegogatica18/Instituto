import os
clear = os.system("clear")

def LimpiarPantalla():
    os.system = "clear"

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def Info(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"
    
class Producto_perecedero(Producto):
    def __init__(self, nombre, cantidad, precio, fecha_vencimiento):
        super().__init__(nombre, cantidad, precio)
        self.fecha_vencimiento = fecha_vencimiento

    def Info(self):
        return f"{super().Info()}, Fecha de vencimiento: {self.fecha_vencimiento} y es un producto perecedero"
    
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto.Info()
        return "Producto no encontrado"

    def listar_productos(self):
        if not self.productos:
            return "No hay productos en el inventario"
        return "\n".join(producto.Info() for producto in self.productos)
    
def Menu(): 
    inventario = Inventario()
    
    while True:
        print("\n1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio: "))
            tipo = input("¿Es un producto perecedero? (s/n): ")
            
            if tipo.lower() == 's':
                fecha_vencimiento = input("Ingrese la fecha de vencimiento (DD/MM/AAAA): ")
                producto = Producto_perecedero(nombre, cantidad, precio, fecha_vencimiento)
            else:
                producto = Producto(nombre, cantidad, precio)
                
            inventario.agregar_producto(producto)
            print("Producto agregado exitosamente.")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            print(inventario.buscar_producto(nombre))
        
        elif opcion == '3':
            print(inventario.listar_productos())
        
        elif opcion == '4': 
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

Menu()