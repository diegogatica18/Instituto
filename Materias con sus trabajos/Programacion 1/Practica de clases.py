import statistics

#Crear una clase para representar un círculo y calcular su área y perímetro.
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    #formulas
    # area = pi * radio^2
    # perimetro = 2 * pi * radio

    def area(self):
        return 3.14 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.radio

calculo = Circulo(10)
print("circulo:")
print("Área:", calculo.area())
print("Perímetro:", calculo.perimetro())


#Crear una clase para representar un rectángulo y calcular su área y perímetro.
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    #formulas
    # area = base * altura
    # perimetro = 2 * (base + altura)

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

calculo = Rectangulo(5, 10)    
print("rectangulo:")
print("Área:", calculo.area())
print("Perímetro:", calculo.perimetro())


#Crear una clase para representar un triángulo y calcular su área y perímetro.
class Triangulo:
    def __init__(self, base, altura, lado1, lado2):
        self.base = base
        self.altura = altura
        self.lado1 = lado1 
        self.lado2 = lado2



    #formulas
    # area = (base * altura) / 2
    # perimetro = suma de los 3 lados

    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        return self.base + self.lado1 + self.lado2
    
calculo = Triangulo(5, 10, 5, 10)
print("triangulo:")
print("Área:", calculo.area())
print("Perímetro:", calculo.perimetro())


#Crear una clase para representar una cuenta bancaria con métodos para depositar y retirar dinero.
class Cuenta_bancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular 
        self.saldo = saldo_inicial  

    def depositar(self, dinero):
        if dinero > 0:
            self.saldo += dinero 
            print(f"Depósito de {dinero} exitoso. Nuevo saldo: {self.saldo}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, dinero):
        if dinero > 0:
            if dinero <= self.saldo:
                self.saldo -= dinero 
                print(f"Retiro de {dinero} exitoso. Nuevo saldo: {self.saldo}")
            else:
                print("No tienes suficiente saldo para realizar este retiro.")
        else:
            print("El monto a retirar debe ser mayor que 0.")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")

mi_cuenta = Cuenta_bancaria("Diego Gatica", 1000)  
mi_cuenta.mostrar_saldo()  
mi_cuenta.depositar(500)  
mi_cuenta.retirar(300) 
mi_cuenta.mostrar_saldo()


#Crear una clase para representar un estudiante con atributos de nombre, edad y calificaciones. Incluir métodos para calcular el promedio de calificaciones.
class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return statistics.mean(self.calificaciones)
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Promedio de calificaciones: {self.promedio()}")

estudiante1 = Estudiante("Diego Gatica", 20, [8, 6, 5, 8])
estudiante1.mostrar_informacion()


#Crear una clase para representar un libro con atributos de título, autor y número de páginas. Incluir métodos para mostrar la información del libro.
class libro:
    def __init__(self, titulo, autor, n_paginas):
        self.titulo = titulo
        self.autor = autor
        self.n_paginas = n_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.n_paginas}")

libro1 = libro("El principito", "Antoine de Saint-Exupéry", 96)
libro1.mostrar_informacion()


#Crear una clase para representar un vehículo con atributos de marca, modelo y año. Incluir métodos para mostrar la información
del vehículo.
class vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")

mi_vehiculo = vehiculo("Toyota", "Corolla", 2020)
mi_vehiculo.mostrar_informacion()


#Crear una clase para representar una persona con atributos de nombre y edad. Incluir métodos para mostrar la información de la persona y verificar si es mayor de edad.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        if self.es_mayor_de_edad():
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")
persona1 = Persona("Diego Gatica", 17)
persona1.mostrar_informacion()

#Crear una clase para representar una tienda con atributos de nombre y lista de productos. Incluir métodos para agregar productos a la lista y mostrar la información de la tienda.
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto '{producto}' agregado a la tienda '{self.nombre}'.")
 
    def mostrar_informacion(self):
        print(f"Tienda: {self.nombre}")
        print("Productos disponibles:")
        for producto in self.productos:
            print(f"- {producto}")

mi_tienda = Tienda("Tienda de Diego")
mi_tienda.agregar_producto("Laptop")
mi_tienda.agregar_producto("Celular")
mi_tienda.agregar_producto("Tablet")
mi_tienda.mostrar_informacion()

#Crear una clase para representar una mascota con atributos de nombre y tipo (perro, gato, etc.). Incluir métodos para mostrar la información de la mascota.
class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
mi_mascota = Mascota("Firulais", "Perro")
mi_mascota.mostrar_informacion()









