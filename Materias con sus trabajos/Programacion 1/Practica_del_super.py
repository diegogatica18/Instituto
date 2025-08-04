class Vehiculo:
    def __init__ (self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_infor(self):
        print(f"la marca del vehiculo es {self.marca}, y su modelo es {self.modelo}")

class Automovil(Vehiculo):
    def __init__ (self, marca, modelo, numero_de_puertas):
        super().__init__(marca, modelo)
        self.numero_de_puertas = numero_de_puertas

    def mostrar_info(self):
        super().mostrar_infor()
        print(f"contiene {self.numero_de_puertas} puertas")

mi_autito = Automovil("Ferrari", 2025, 4)
mi_autito.mostrar_info()
    

