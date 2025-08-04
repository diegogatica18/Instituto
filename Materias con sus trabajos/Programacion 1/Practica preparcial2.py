class biblioteca:
    def __init__ (self, usuarios):
        self.catalago = []
        self.usuarios = usuarios

    def agregar_libro(self, libro):
        libro = input(f"Ingresar titulo del libro que desea agregar: ")
        if libro not in self.catalogo:
            libro.append in self.catalogo
            print("El libro fue agregado con exito")
        else:
            print("el libro ingresado ya se encuentra en el catalogo")

    def prestar_libro(self, libro):
        if libro not in self.catalogo:
            print(f"EL libro ya fue prestado")
        else:
            print(f"puede llevarse el libro llamado {libro}")

    def devolver_libro(self, libro):
        devolver = (f"Ingresar el libro que desea devolver: ")
        if devolver not in self.catalogo:
            print(f"{libro} se devolvio correctamente")
            devolver.append in self.catalogo

class Libro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
  

    def mostrar_info(self):
        print(f"El libro se llama {self.__titulo} y su autor es {self.__autor}. ")


    def agregar_libro(self, libro):
        libro = input(f"Ingresar titulo del libro que desea agregar: ")
        if libro not in self.catalogo:
            libro.append in self.catalogo
            print("El libro fue agregado con exito")
        else:
            print("el libro ingresado ya se encuentra en el catalogo")


    def devolver_libro(self):
        super().devolver_libro()
  

    def is_disponible(self):
        eleccion = input("ingresar el nombre del libro que quiere: ")
        if eleccion in self.__disponible:
            print("el libro esta disponible")
        else:
            print("el libro no se encuentra en este momento")


libro = Libro("hola", "hola")
libro.mostrar_info()
libro.agregar_libro(0)

libro.is_disponible



    
    

    



