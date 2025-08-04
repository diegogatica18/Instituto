# inicio
# registrar producto
# buscar producto 
# mostrar lista de productos
# calcular valor total del inventario
# Mostrar el total del inventario

import os
clear = os.system("clear")

def LimpiarPantalla():
    os.system = "clear"

"""Esta clase se encarga de lo que seria el producto con un metodo que retorna la informacion de la misma"""
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

"""Esta clase es la que se encarga de los movimientos con los productos, contiene metodos que te permiten agregar, buscar y motrar productos. Tambien permite hacr un calculo del inventario"""
class Inventario:
    def __init__(self):
        self.__productos = []
    
    """Si el largo de la lista de producos es menor a 10 deja agregar sino no lo permite"""
    def agregar_productos(self, producto):
        if len(self.__productos) < 10:
            self.__productos.append(producto)
            print("El producto se agrego exitosamente")
        else:
            print("No se pueden agregar más productos al inventario")
    
    """Busca el nombre del producto dentro de la lista de productos y la retorna"""
    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.nombre == nombre:
                return producto.mostrar_informacion()
        return "El producto no se encuentra en el inventario"
    
    """Se encarga de devolver los productos con su debida informacion"""
    def mostrar_productos_inventario(self):
        if not self.__productos:
            return "No hay productos en el inventario"
        return "\n".join(producto.mostrar_informacion() for producto in self.__productos)
    
    """Calcula la cantidad de productos multiplicando el precio por la cantidad"""
    def calcular_valor_total(self):
        total_inventario = sum(Producto.cantidad * Producto.precio for Producto in self.__productos)
        return f"Valor total del inventario: {total_inventario}"
    
def menu():
    inventario = Inventario()
   
    while True:
        print("." * 50)
        print("Menu para la gestion de productos en el inventario")
        print("\n1. Agregar producto")
        print("2. Buscar producto")
        print("3. Mostrar productos del inventario")
        print("4. Ver total del inventario")
        print("5. Salir")
        print("-" * 50)

        opcion = input("Seleccione la opcion que necesite: ")
        if opcion == "1":
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad < 0:
                print("la cantidad no puede ser negativa, por favor ingresar un numero valido")
                continue
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo, por favor ingresar un precio valido")
                continue
            producto = Producto(nombre, cantidad, precio)
            inventario.agregar_productos(producto)
            
        elif opcion == "2":
            nombre = input("Ingrese el nombre del producto que desee buscar: ")
            resultado = inventario.buscar_producto(nombre)
            print(resultado)

        elif opcion == "3":
            productos = inventario.mostrar_productos_inventario()
            print(productos)
        
        elif opcion == "4":
            total_inventario = inventario.calcular_valor_total()
            print(total_inventario)

        elif opcion == "5":
            print("Gracias por usar el sistema de gestion de inventario ¡Vuelva pronto!")
            break
        
        else:
            print("Opcion no valida, ingrese un numero valido")

menu()
    


