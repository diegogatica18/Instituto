class Producto:
    def __init__(self, nombre, precio, cantidad_en_stock):
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad_en_stock = cantidad_en_stock

    def obtener_nombre(self):
        return self.__nombre

    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def obtener_precio(self):
        return self.__precio

    def establecer_precio(self, nuevo_precio):
        if nuevo_precio >= 0:
            self.__precio = nuevo_precio
        else:
            print("El precio no puede ser negativo.")

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__cantidad_en_stock += cantidad
        else:
            print("La cantidad a agregar debe ser positiva.")

    def retirar_stock(self, cantidad):
        if 0 < cantidad <= self.__cantidad_en_stock:
            self.__cantidad_en_stock -= cantidad
        else:
            print("Cantidad no válida para retirar.")

producto = Producto("Laptop", 1500, 10)
print(f"Nombre: {producto.obtener_nombre()}")
print(f"Precio: {producto.obtener_precio()}")
producto.establecer_precio(1600)
print(f"Nuevo Precio: {producto.obtener_precio()}")
producto.agregar_stock(5)
print(f"Cantidad en stock: {producto._Producto__cantidad_en_stock}")
producto.retirar_stock(3)
print(f"Cantidad en stock después de retirar: {producto._Producto__cantidad_en_stock}")
    

