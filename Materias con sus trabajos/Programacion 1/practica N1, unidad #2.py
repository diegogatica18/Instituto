"""#defino la clase
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad

#agrego un metodo que imprime un sonido
    def hacer_sonido(self):
        sonido = ("wau wau wau")
        return sonido
    
    def descripcion(self):
        return "mi perra se llama {} y tiene {} años".format(self.nombre, self.edad)
        
    def cumplir_años(self):
        self.edad = (self.edad + 1)
        return f"hoy es su cumple y su nueva edad es de {self.edad} años"


#creo la instancia de la clase
mi_animal = Animal("lola", 5)


print(f"mi perrita se llama {mi_animal.nombre} y cuando pasa gente por la calle hace {mi_animal.hacer_sonido()}")
print(mi_animal. descripcion())
print(mi_animal.cumplir_años())

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        print(f"{self.nombre} puede hablar")

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"mi perro {self.nombre} ¡hace wau wau!")
    
mi_animal = Animal("lola")
mi_perro = Perro("lola")

mi_animal.hablar()
mi_perro.hablar()

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_coche = Coche("toyota", 2004)

print(f"mi auto es un {mi_coche.marca}, del año {mi_coche.modelo}")


class Persona:
    pass

    def saludar(self):
        print("hola, como va?")
    
class Estudiante(Persona):
    pass

    def estudiar(self):
        print("tengo que estudiar")

alumno = Estudiante()
alumno.saludar()
alumno.estudiar()


class Figura:

    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado
    
mi_cuadrado = Cuadrado(4)
print(f"El área del cuadrado es de: {mi_cuadrado.area()}")


class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        

    def trabajar(self):
        print(f"{self.nombre} está trabajando")

class Gerente(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        super().trabajar()
        
el_empleado = Empleado("Juan", 100)
el_empleado.trabajar()
el_gerente = Gerente("Diego", 1000)
el_gerente.trabajar()

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Electronico(Producto):
    def __init__(self, nombre, precio):
        super().__init__(nombre)
        self.precio = precio

Producto_electronico = Electronico("tele", 100000)
print(f"El producto es un {Producto_electronico.nombre} y su precio es de {Producto_electronico.precio}")


class Instrumento:
    def __init__(self, nombre):
        self.nombre = nombre

    def tocar(self):
        print(f"Mi {self.nombre} está sonando")

class Guitarra(Instrumento):
    def __init__(self, nombre):
        super().__init__(nombre)

    def afinar(self):
        print(f"Mi {self.nombre} se está afinado")

mi_guitarra = Guitarra("guitarra")

mi_guitarra.tocar()
mi_guitarra.afinar()


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

class Ebook(Libro):
    def __init__(self, titulo, formato):
        super().__init__(titulo)
        self.formato = formato

mi_ebook = Ebook("El gran libro", "PDF")
print(f"El libro se llama {mi_ebook.titulo} y su formato es {mi_ebook.formato}")

class Vehiculo:
    def moverse(self):
        print("El vehículo esta avanzando")

class Bicicleta(Vehiculo):
    def moverse(self):
        super().moverse()
        print("La bicicleta se mueve pedaleando")

mi_bicicleta = Bicicleta()
mi_bicicleta.moverse()


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def presentarse(self):
        print(f"Me llamo {self.nombre}")

class Profesor(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    def enseñar(self):
        print(f"Mi nombre es {self.nombre} y enseño {self.materia}")

profesor = Profesor("Juan", "Matemáticas")
profesor.presentarse()
profesor.enseñar()
"""








    

        
