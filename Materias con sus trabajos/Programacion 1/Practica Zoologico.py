import os
clear = os.system("clear")

def LimpiarPantalla():
    os.system = "clear"

class Animal:
    def __init__ (self, nombre, especie, edad, salud):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.salud = salud

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Especie: {self.especie}, Edad: {self.edad}, Salud: {self.salud}"
    
    def actualizar_salud(self, nueva_salud):
        self.salud = nueva_salud
        return f"La salud de {self.nombre} se actualizo a {self.salud}."

class Zoologico:
    def __init__ (self, nombre, ubicacion, animales, animales_exoticos):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.animales = []
        self.animales_exoticos = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, nombre):
        if self.animales:
            for animal in self.animales:
                if animal.nombre == nombre:
                    self.animales.remove(animal)
                    return f"Animal {nombre} eliminado."
        return f"Animal {nombre} no encontrado."

    def buscar_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                return animal.mostrar_informacion()
        return f"Animal {nombre} no encontrado."
    
    def mostrar_animales(self):
        if self.animales:
            return [animal.mostrar_informacion() for animal in self.animales]
        return "No hay animales autonomos en el zoológico."
    
    def mostrar_animales_exoticos(self):
        if self.animales_exoticos:
            return [animal.ver_exoticos() for animal in self.animales_exoticos]
        return "No hay animales exóticos en el zoológico."
    
class Animal_exotico(Animal):
    def __init__(self, nombre, especie, edad, salud, pais_origen, nivel_riesgo):
        super().__init__(nombre, especie, edad, salud)
        self.pais_origen = pais_origen
        self.nivel_riesgo = nivel_riesgo

    def mostrar_informacion_exotico(self):
        return f"{super().mostrar_informacion()}, País de origen: {self.pais_origen} y su nivel de riesgo es {self.nivel_riesgo} y es un animal exotico."
    
    def buscar_animal(self, nombre):
        for animal in self.animales_exoticos:
            if animal.nombre == nombre:
                return animal.mostrar_informacion_exotico()
        return f"Animal {nombre} no encontrado."

    def ver_exoticos(self):
        return f"El animal {self.nombre} es exótico, su especie es {self.especie}, su edad es {self.edad}, su estado de salud es {self.salud}, su país de origen es {self.pais_origen} y su nivel de riesgo es {self.nivel_riesgo}."
    
def Menu():
    zoo = Zoologico("Zoológico de chucho", "San Jeronimo", [], [])
    
    while True:
        print("\n1. Agregar animal")
        print("2. Agregar animal exótico")
        print("3. Buscar animal")
        print("4. Mostrar animales")
        print("5. Mostrar animales exóticos")
        print("6. Eliminar animal")
        print("7. Actualizar salud de un animal")
        print("8. Buscar animal exótico")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del animal: ")
            especie = input("Ingrese la especie del animal: ")
            edad = int(input("Ingrese la edad del animal: "))
            salud = input("Ingrese el estado de salud del animal: ")
            animal = Animal(nombre, especie, edad, salud)
            zoo.agregar_animal(animal)
            print(f"Animal {nombre} agregado al zoológico.")
        
        elif opcion == '2':
            nombre = input("Ingrese el nombre del animal exótico: ")
            especie = input("Ingrese la especie del animal exótico: ")
            edad = int(input("Ingrese la edad del animal exótico: "))
            salud = input("Ingrese el estado de salud del animal exótico: ")
            pais_origen = input("Ingrese el país de origen del animal exótico: ")
            nivel_riesgo = input("Ingrese el nivel de riesgo del animal exótico: ")
            animal_exotico = Animal_exotico(nombre, especie, edad, salud, pais_origen, nivel_riesgo)
            zoo.animales_exoticos.append(animal_exotico)
            print(f"Animal exótico {nombre} agregado al zoológico.")
       
        elif opcion == '3':
            nombre = input("Ingrese el nombre del animal a buscar: ")
            print(zoo.buscar_animal(nombre))
        
        elif opcion == '4':
            animales = zoo.mostrar_animales()
            if isinstance(animales, list):
                for animal in animales:
                    print(animal)
            else:
                print(animales)
        
        elif opcion == '5':
            animales_exoticos = zoo.mostrar_animales_exoticos()
            if isinstance(animales_exoticos, list):
                for animal in animales_exoticos:
                    print(animal)
            else:
                print(animales_exoticos)

        elif opcion == '6':
            nombre = input("Ingrese el nombre del animal a eliminar: ")
            print(zoo.eliminar_animal(nombre))
        
        elif opcion == '7':
            nombre = input("Ingrese el nombre del animal para actualizar su salud: ")
            nueva_salud = input("Ingrese la nueva salud del animal: ")
            for animal in zoo.animales:
                if animal.nombre == nombre:
                    print(animal.actualizar_salud(nueva_salud))
                    break
            else:
                print(f"Animal {nombre} no encontrado.")

        elif opcion == '8':
            nombre = input("Ingrese el nombre del animal exótico a buscar: ")
            for animal in zoo.animales_exoticos:
                if animal.nombre == nombre:
                    print(animal.mostrar_informacion_exotico())
                    break
            else:
                print(f"Animal exótico {nombre} no encontrado.")

        elif opcion == '9':
            print("Saliendo del menú.")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")

Menu()

