class Publicacion:
    def __init__ (self, titulo, autor, anio_publicacion):
        self.titulo = titulo 
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_infor(self):
        pass

class Libro(Publicacion):
    def __init__ (self, titulo, autor, anio_publicacion, precio, disponibilidad):
        super().__init__(titulo, autor, anio_publicacion)
        self.precio = precio 
        self.disponibilidad = disponibilidad

    def info_libro(self):
        print(f"el libro se titula: {self.titulo}")
        print(f"su autor es: {self.autor}")
        print(f"el mismo se publico en el año {self.anio_publicacion}")
        if self.disponibilidad == "si":
            print(f"El libro llamado {self.titulo} del autor {self.autor} esta disponible.")
        elif self.disponibilidad == "no":
            print(f"El libro llamado {self.titulo} del autor {self.autor} no esta disponible en este momento.")

    def mostrar_infor(self):
        super().mostrar_infor()
        print(f"Su precio es de {self.precio}, y el libro {self.disponibilidad} esta disponible")

    def cambiar_precio(self, precio_nuevo):
        precio_nuevo = input("Ingresar nuevo precio: ")
        self.precio = precio_nuevo
        print(f"Su precio se actualizo a ${precio_nuevo}")


class Revista(Publicacion):
    def __init__ (self, titulo, autor, anio_publicacion, precio, disponibilidad, la_tiene):
        super().__init__(titulo, autor, anio_publicacion)
        self.precio = precio
        self.disponibilidad = disponibilidad
        self.__la_tiene = la_tiene
    
    def info_revista(self):
        print(f"La revista se titula: {self.titulo}")
        print(f"Su autor es: {self.autor}")
        print(f"Se publico en el año {self.anio_publicacion}")
    
    def mostrar_infor(self):
        super().mostrar_infor()
        print(f"Su precio es de {self.precio}, la revista {self.disponibilidad} esta disponible, la tiene {self.__la_tiene}.")

    def cambiar_portador(self, portador):
        portador = input("Ingrese quien es el nuevo portador de la revista: ")
        self.__la_tiene = portador
        print(f"El nuevo portador de la revista es {portador}")

class Periodico(Publicacion):
    def __init__ (self, titulo, autor, anio_publicacion, precio, disponibilidad, cantidad):
        super().__init__(titulo, autor, anio_publicacion)
        self.precio = precio
        self.diponibilidad = disponibilidad
        self.cantidad = cantidad

    def info_periodico(self):
        print(f"El periodico se titula: {self.titulo}")
        print(f"Su autor es: {self.autor}")
        print(f"Se publico en el año {self.anio_publicacion}")

    def mostrar_infor(self):
        super().mostrar_infor()
        print(f"El precio del periodico es de {self.precio}, el mismo {self.diponibilidad} esta disponible, y nos quedan {self.cantidad} en stock. ")

    def cambiar_cantidad(self, nueva_cantidad):
        nueva_cantidad = input(f"Ingresar nueva cantidad de periodicos: ")
        self.cantidad = nueva_cantidad
        print(f"el stock se actualizo a {nueva_cantidad} periodicos")


mi_libro = Libro("Odisea", "Homero", 2024, "$50", "si")
mi_libro.info_libro()
mi_libro.mostrar_infor()
mi_libro.cambiar_precio(0)

mi_revista = Revista("Clarin", "el pais", 2025, "$5000", "no", "michael")
mi_revista.info_revista()
mi_revista.mostrar_infor()
mi_revista.cambiar_portador("michael")

mi_periodico = Periodico("La nacion", "el pais", 2025, "$100","si", 10)
mi_periodico.info_periodico()
mi_periodico.mostrar_infor()
mi_periodico.cambiar_cantidad(0)

