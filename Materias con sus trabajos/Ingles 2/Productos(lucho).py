import os
clear = os.system("clear")
import tabulate

class Producto:
    def __init__(self):
        self.nombre = []
        self.codigo = []
        self.cantidad = []
        self.precio = []
        self.fecha_vencimiento = []

    def agregar_productos(self, nombre, codigo, cantidad, precio, fecha_vencimiento):
        if nombre in nombre:
            return print("Producto ya registrado")
        else:
            self.nombre.append(nombre)
            self.codigo.append(codigo)
            self.cantidad.append(cantidad)
            self.precio.append(precio)
            self.fecha_vencimiento.append(fecha_vencimiento)
            print(f"Producto agregado con exito\ncogido del producto: {codigo}\nnombre: {nombre}\ncantidad: {cantidad}\nprecio: {precio}\n fecha de vencimiento: {fecha_vencimiento}")
            contiuar = input("desea continuar s/n").lower().strip()

    def buscar_producto(self, codigo_ingresado):
        posicion_lista = 0
        if codigo_ingresado in self.codigo:
            for codigo_producto in self.codigo:
                if codigo_producto == codigo_ingresado:
                    print(f"Producto encontrado\n codigo: {codigo_ingresado}\n nombre: {self.nombre[posicion_lista]}\n precio: {self.precio[posicion_lista]}\n cantidad: {self.cantidad[posicion_lista]}")
                else:
                    posicion_lista += 1
        else:
            print(f"Codigo no existente")
    
    def listar_productos(self):
        print(tabulate(self.codigo, self.nombre, self.cantidad, self.precio, self.fecha_vencimiento, headers = ("Codigo del producto, Nombre, Cantidad, Precio, Fecha de vencimiento"), tableft = "plain"))
    

    def mostrar_codigos(self):
        for codigo in self.codigo.enumerate:
            print(codigo)
        return self.codigo

class Productos_pedecederos(Producto):
    def __init__(self):
        super().__init__()
    
    def agregar_productos(self, nombre, codigo, cantidad, precio, fecha_vencimiento):
        return super().agregar_productos(nombre, codigo, cantidad, precio, fecha_vencimiento)
    
    def buscar_producto(self):
        posicion_lista = super().buscar_producto()
        print(f" fecha de vencimiento: {self.fecha_vencimiento[posicion_lista]}")
    
    def listar_productos(self):
        return super().listar_productos()

def agregar(a):
    while range(10):
        nombre = input("Ingrese el nombre del producto ").lower().strip()
        codigo = input("Ingrese el codigo del producto ").lower().strip()
        cantidad = input("Ingrese la cantidad del producto ").lower().strip()
        precio = input("Ingrese el precio del producto ").lower().strip()
        fecha_vencimiento = input("Ingrese el vencimeinto del producto ").lower().strip()
        a.agregar_productos(nombre, codigo, cantidad, precio, fecha_vencimiento)
        continuar = input("continuar s/n").lower().strip()
        if continuar != "s":
            continue
        else:
            return

while True:
    clear = os.system("clear")
    elegir = input("Seleccione el tipo de producto: No pedecedero, Pedecedero: ").strip().lower()
    if elegir == "no pedecedero":
        print("Ingrese el numero de la opcion a elegir: \n1.agregar producto \n2.buscar producto \n3.listar productos")
        elegir_accion = input().lower().strip()
        if elegir_accion == "1" or elegir_accion == "agregar producto":
            producto = Producto()
            agregar(producto)
            continue
        elif elegir_accion == "2" or elegir_accion == "buscar producto":
            producto = Producto()
            codigos_a_mostrar = producto.mostrar_codigos()
            codigo = input("Ingrese el codigo a ingresar")
            if codigo in codigos_a_mostrar:
                producto.buscar_producto(codigo)
            else:
                print("Error volviendo al inicio")
            continue
        elif elegir_accion == "3" or elegir_accion == "listar productos":
            producto = Producto()
            producto.listar_productos()
            continue
    elif elegir == "predecedero":
        print("Ingrese el numero de la opcion a elegir: \n1.agregar producto \n2.buscar producto \n3.listar productos")
        elegir_accion = input().lower().strip()
        if elegir_accion == "1" or elegir_accion == "agregar producto":
            producto = Productos_pedecederos()
            agregar(producto)
            continue
        elif elegir_accion == "2" or elegir_accion == "buscar producto":
            producto = Productos_pedecederos()
            codigos_a_mostrar = producto.mostrar_codigos()
            codigo = input("Ingrese el codigo a ingresar")
            if codigo in codigos_a_mostrar:
                producto.buscar_producto(codigo)
            else:
                print("Error volviendo al inicio")
            continue
        elif elegir_accion == "3" or elegir_accion == "listar productos":
            producto = Productos_pedecederos()
            producto.listar_productos()
            continue
