"""class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else :
            print("no se aceptan numeros negativos")
        
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("dinero depositado correctamente")

    def retirar(self, monto):
        if monto < self.__saldo:
            self.__saldo -= monto
            print("el saldo fue retirado correctamente")
        
    def mostrar_info(self):
        return f"el titular de la cuenta es {self.__titular} y su saldo es de {self.__saldo}"

tipo = CuentaBancaria("Chucho", 0)
tipo.depositar(100)
tipo.retirar(50)
print(tipo.mostrar_info())
        
class Alumno:
    def __init__(self, nombre, DNI):
        self.__nombre = nombre
        self.__DNI = DNI
        self.__notas = []

    def get_nombre(self):
        return self.__nombre

    def get_DNI(self):
        return self.__DNI 
    
    def agregar_nota(self, nota):
        if 1 <=  nota <= 10:
            self.__notas.append(nota)
            return print(f"La nota de {nota} se agrego al sistema")
        
    def promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)
       
       
    
    def mostrar_info(self):
        print(f"Nombre: {self.__nombre} DNI: {self.__DNI} Promedio: {self.promedio():.2f}")
    

alumno = Alumno("Diego", 46366900)

alumno.agregar_nota(5)
alumno.agregar_nota(6)
alumno.agregar_nota(7)
print(alumno.promedio())
alumno.mostrar_info()

# 🧱 Clase base: Persona (para herencia)
class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre

    def get_dni(self):
        return self.__dni

    def mostrar_info(self):
        print(f"👤 Persona: {self.__nombre} - DNI: {self.__dni}")


# 📗 Clase: Libro
class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponible = True

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    def mostrar_info(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        print(f"📘 '{self.__titulo}' por {self.__autor} - Estado: {estado}")


#  Clase: Usuario (hereda de Persona)
class Usuario(Persona):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self.__libros_prestados = []

    def prestar_libro(self, libro):
        if libro.esta_disponible():
            if libro.prestar():
                self.__libros_prestados.append(libro)
                print(f"{self.get_nombre()} ha prestado: '{libro.get_titulo()}'")
        else:
            print(f"❌ El libro '{libro.get_titulo()}' no está disponible.")

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            libro.devolver()
            self.__libros_prestados.remove(libro)
            print(f" {self.get_nombre()} devolvió: '{libro.get_titulo()}'")
        else:
            print(f" {self.get_nombre()} no tiene ese libro.")

    def mostrar_info(self):  # Polimorfismo: redefine método
        print(f"Usuario: {self.get_nombre()} - Libros prestados:")
        for libro in self.__libros_prestados:
            print(f"   → {libro.get_titulo()}")

libro1 = Libro("1984", "George Orwell")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

usuario1 = Usuario("Martina", "40666777")

usuario1.prestar_libro(libro1)
usuario1.prestar_libro(libro2)
usuario1.prestar_libro(libro1)  # ya está prestado

usuario1.mostrar_info()
libro1.mostrar_info()

usuario1.devolver_libro(libro1)
libro1.mostrar_info()

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__libros = []
        self.__libros.append(self.__titulo)

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def esta_disponible(self):
        if self.__titulo in self.__libros:
            print(f"El libro esta disponible")
        else:
            print(f"El libro {self.__titulo} no esta disponible")

    def prestar(self):
        if self.__titulo in self.__libros:
            print(f"Se te entrego el libro llamado {self.__titulo} ")
            self.__libros.remove(self.__titulo)
        else:
            print(f"El libro {self.__titulo} esta en uso")

    def devolver(self):
        if not self.__titulo in self.__libros:
            print(f"El libro {self.__titulo} fue devuelto con exito")
            self.__libros.append(self.__titulo)
        else:
            print(f"El libro {self.__titulo} no ya esta en la lista")
        
    def mostrar_info(self):
        return f"Titulo: {self.__titulo} Autor: {self.__autor}"


class Persona:
    def __init__(self, nombre, dni):
        self.__nombre = nombre
        self.__dni = dni

    def get_nombre(self):
        return self.__nombre
    
    def get_dni(self):
        return self.__dni
    
    def mostrar_info(self):
        return f"nombre: {self.__nombre} DNI: {self.__dni}"
    
class Usuario(Persona):
    def __init__ (self, nombre, dni):
        super().__init__(nombre, dni)
        self.__libros_prestados = []


mi_libro = Libro("El principito", "luciano")
mi_libro.esta_disponible()
mi_libro.prestar()
mi_libro.esta_disponible()
mi_libro.devolver()
mi_libro.esta_disponible()"""


    
        
    


        
    
