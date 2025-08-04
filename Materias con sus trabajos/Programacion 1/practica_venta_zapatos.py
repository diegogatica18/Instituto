class Producto:
    def __init__ (self):
        self.precio = 0
        self.stock = 0
        self.productos = []

    def obtener_precio(self):
        pass

    def verificar_stock(self):
        pass

class zapato(Producto):
    def __init__(self, marca, precio, stock):
        self.marca = marca
        self.precio = precio
        self.stock = stock
    
    def obtener_precio(self):
        return self.precio
    
    def verificar_stock(self):
        if self.stock > 0:
            print(f"el stock es de {self.stock} unidades")
            return True
        else:        
            self.stock == 0
            print(f"no nos queda stock de la marca {self.marca}")
            return False
        
class zapatilla(Producto):
    def __init__(self, marca, precio, stock):
        self.marca = marca
        self.precio = precio
        self.stock = stock
    
    def obtener_precio(self):
        return self.precio
    
    def verificar_stock(self):
        if self.stock > 0:
            print(f"el stock es de {self.stock} unidades")
            return True
        else:        
            self.stock == 0
            print(f"no nos queda stock de la marca {self.marca}")
            return False
    
class Metodo_pago:
    def __init__(self, metodo, saldo):
        self.metodo = metodo
        self.saldo = saldo

    def obtener_metodo(self):
        return self.metodo
    
    def obtener_saldo(self):
        return self.saldo

class verificador:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def verificar_stock(self):
        for producto in self.productos:
            if not producto.verificar_stock():
                print(f"El producto {producto.marca} no está disponible.")
    
    def metodo_pago(self, metodo, saldo):
        self.metodo = Metodo_pago(metodo, saldo)
        print(f"El método de pago es {self.metodo.obtener_metodo()} y el saldo es {self.metodo.obtener_saldo()}.")

    def mostrar_precios(self):
        for producto in self.productos:
            print(f"El precio del producto {producto.marca} es de {producto.obtener_precio()}.")
    
# Crear instancias de zapato y zapatilla
zapato1 = zapato("Nike", 100, 10)
zapatilla1 = zapatilla("Adidas", 80, 0)
metodo_pago1 = Metodo_pago("Tarjeta de crédito", 500)
# Crear instancia de verificador
verificador_de_productos = verificador()
# Agregar productos al verificador
verificador_de_productos.agregar_producto(zapato1)
verificador_de_productos.agregar_producto(zapatilla1)
# Verificar stock y mostrar precios
verificador_de_productos.verificar_stock()
verificador_de_productos.mostrar_precios()
# Mostrar método de pago y saldo
verificador_de_productos.metodo_pago(metodo_pago1.obtener_metodo(), metodo_pago1.obtener_saldo())