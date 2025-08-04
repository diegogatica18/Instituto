def clear():
    import os
    clear = os.system("clear")

class Animal:

    pass
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("gaauuuu")
    def descripcion(self):
        return "Me llamo {} y tengo {} años".format(self.nombre , self.edad)
    def cumplir_años(self):
        self.edad = (self.edad + 1)
        print(f"Ayer cumplio años y su nueva edad es: {self.edad}")

    def hablar(self):
        print("wauuu wau waauu (hola señores y señoras)")

clear()

perro = Animal("juan", 5)
print(perro.nombre, perro.edad)
perro.hacer_sonido()
print(perro.descripcion())
perro.cumplir_años()
perro.hablar()

class Perro(Animal):
    pass
    def hablar(self):
        print("wauu (adios)")

perro = Perro("adrian", 3)
perro.hablar()

class Vehiculo:
    pass
    def __init__(self, marca):
        self.marca = marca

class Coche(Vehiculo):
    pass
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

compacto = Coche("compacto", 4500)
print(compacto.marca, compacto.modelo)

class Persona:
    pass
    def saludar(self):
        print("las personas podemos saludar con la mano")

class Estudiante(Persona):
    pass
    def quejarse(self):
        print("los estudiantes podemos quejarnos de la tarea")

juan = Estudiante()
juan.saludar()
juan.quejarse()

class Figura:
    pass

    def area(self):
        b, = [int(input("ingresar base: "))]
        h, = [int(input("ingresar altura: "))]
        a = b * h
        return "el resultado es: ", a

rectangulo = Figura()
print(rectangulo.area())

class Cuadrado(Figura):
    pass
    def area(self):
        l, = [int(input("ingresar lado: "))]
        a = l * l
        return "el resultado es: ", a

figura_cuadrado = Cuadrado()
print(figura_cuadrado.area())

