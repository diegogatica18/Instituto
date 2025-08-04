import os
clear = os.system("clear")

def LimpiarPantalla():
    os.system = "clear"

class Doctor:
    def __init__(self, nombre, edad, especialidad, recetas):
        self.__nombre = nombre
        self.__edad = edad 
        self.__especialidad = especialidad
        self.__recetas = []

    def mostrar_info(self):
        print(f"el nombre del doctor es {self.__nombre}, su edad es de {self.__edad} y se especialidad es ser {self.__especialidad}")

class Cliente:
    def __init__(self, nombre, apellido, edad, telefono):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__telefono = telefono

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Apellido: {self.__apellido}, Edad: {self.__edad}, Telefono: {self.__telefono}"

    def get_nombre(self):
        return self.__nombre

    
class Gestion:
    def __init__(self, nombre, clientes, doctores):
        self.nombre = nombre
        self.clientes = []
        self.doctores = []
        self.__recetas = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def eliminar_cliente(self, nombre):
        if self.clientes:
            for cliente in self.clientes:
                if cliente.get_nombre() == nombre:
                    self.clientes.remove(cliente)
                    return f"El cliente llamado {nombre} fue eliminado."
        return f"El cliente llamado {nombre} no fue encontrado."
    
    def mostrar_clientes(self):
        if self.clientes:
            return [cliente.mostrar_info() for cliente in self.clientes]
        return "No hay clientes en el sistema."

    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.get_nombre() == nombre:
                return cliente.mostrar_info()
        return f"El cliente llamado {nombre} no fue encontrado."

    def crear_receta(self, paciente, medicamento):
        self.__recetas.append(f"Receta para {paciente}: {medicamento}")
        return f"Receta creada para {paciente} con el medicamento {medicamento}."


    def lista_de_doctores(self):
        if self.doctores:
            return [doctor.mostrar_info() for doctor in self.doctores]
        return "No hay doctores registrados en el sistema."
    
    def ver_recetas_emitidas(self):
        if self.__recetas:
            return self.__recetas
        return "No hay recetas emitidas."

    def eliminar_receta(self, nombre):
        for receta in self.__recetas:
            if nombre in receta:
                self.__recetas.remove(receta)
                return f"Receta para {nombre} ha sido eliminada."
        return f"No se encontró una receta para {nombre}."
    
def menu():
    gestion = Gestion("Gestionsin", [], [])

    while True:
        
        print("\n--- Menu de Gestion de Clientes ---")
        print("\n1. Agregar cliente")
        print("2. Registrar doctor")
        print("3. Ver doctores disponibles")
        print("4. Buscar cliente")
        print("5. Mostrar clientes")
        print("6. Eliminar cliente")
        print("7. Crear receta")
        print("8. Ver recetas")
        print("9. Eliminar receta")
        print("10. Salir")

        opcion = input("seleccione una opcion: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            apellido = input("Ingrese el apellido del cliente: ")
            edad = int(input("Ingrese la edad del cliente: "))
            telefono = int(input("Ingrese el telefono del cliente: "))
            cliente = Cliente(nombre, apellido, edad, telefono)
            gestion.agregar_cliente(cliente)
            print(f"Cliente llamado {nombre} se agrego al sistema.")

        if opcion == "2":
            nombre_doctor = input("Ingrese el nombre del doctor: ")
            edad_doctor = int(input("Ingrese la edad del doctor: "))
            especialidad_doctor = input("Ingrese la especialidad del doctor: ")
            doctor = Doctor(nombre_doctor, edad_doctor, especialidad_doctor, [])
            gestion.doctores.append(doctor)
            print(f"Doctor llamado {nombre_doctor} se agrego al sistema.")
             
        if opcion == "3":
            doctores = gestion.lista_de_doctores()
            if isinstance(doctores, list):
                for doctor in doctores:
                    print(doctor)
            else:
                print(doctores)
        
        if opcion == "4":
                    nombre = input("Ingrese el nombre del cliente que desea buscar: ")
                    print(gestion.buscar_cliente(nombre))

        if opcion == "5":
            clientes = gestion.mostrar_clientes()
            if isinstance(clientes, list):
                for cliente in clientes:
                    print(cliente)
            else:
                print(clientes)
        
        if opcion == "6":
            nombre = input("Ingrese el nombre del cliente que desea eliminar: ")
            print(gestion.eliminar_cliente(nombre))

      
        if opcion == "7":
            nombre_doctor = input("Ingrese el nombre del doctor: ")
            doctor = None
            for d in gestion.doctores:
                if d._Doctor__nombre == nombre_doctor:
                    doctor = d
                    break
            if doctor is None:
                print("Doctor no encontrado. Debe registrarlo primero.")
            else:
                nombre_paciente = input("Ingrese el nombre del paciente: ")
                medicamento = input("Ingrese el medicamento: ")
                receta = gestion.crear_receta(nombre_paciente, medicamento)
                print(receta)

     
        if opcion == "8":
            recetas = gestion.ver_recetas_emitidas()
            if isinstance(recetas, list):
                for receta in recetas:
                    print(receta)
            else:
                print(recetas)

        if opcion == "9":
            receta = input("Ingrese el nombre del cliente que desea cancelarle la receta: ")
            print(gestion.eliminar_receta(receta))


        if opcion == "10":
            print("Saliendo del menu...")
            break
menu()