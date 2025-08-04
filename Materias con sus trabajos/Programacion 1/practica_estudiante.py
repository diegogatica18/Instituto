import statistics

class Estudiante:
    def __init__ (self, nombre, edad, calificaciones):
        self.__nombre = nombre
        self.__edad = edad
        self.__calificaciones = []

    def mostrar_nombre(self):
        print(f"El nombre del estudiante es: {self.__nombre}")
    
    def mostrar_edad(self):
        print(f"Su edad es de: {self.__edad} años")
    
    def ingresar_calificaciones(self):
        while True:
            calificacion = input("Ingrese una calificación o fin para terminar: ").strip()
            if calificacion.lower() == 'fin':
                break
            try:
                calificacion = float(calificacion)
                if 0 <= calificacion <= 10:
                    self.__calificaciones.append(calificacion)
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Ingresar un numero valido.")
    
    def mostrar_calificaciones(self):
        print(f"Las calificaciones son: {self.__calificaciones}")
    
    def mostrar_promedio(self):
        suma = 0
        for calificacion in self.__calificaciones:
            suma += calificacion
        promedio = suma / len(self.__calificaciones)
        print(f"el promedio de las calificaciones es de: {promedio}")
    
yo = Estudiante("Luciano", 16, [])

yo.mostrar_nombre()
yo.mostrar_edad()
yo.ingresar_calificaciones()
yo.mostrar_calificaciones()
yo.mostrar_promedio()





    
        