class Vehiculo:
    def __init__ (self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__kilometros = 0

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_kilometros(self):
        return self.__kilometros

    def descripcion(self):
        return f"marca: {self.__marca}, modelo: {self.__modelo}, kilometros: {self.__kilometros}"
    
    def mover(self, km):
        self.__kilometros += km

    def costo_mantenimiento(self):
        pass

    def costo_nafta(self, costo_por_km):
        return self.__kilometros * costo_por_km

class Auto(Vehiculo):
    
    def costo_mantenimiento(self):
        return self.get_kilometros() * 0.1

class Camion(Vehiculo):

    def costo_mantenimiento(self):
        return self.get_kilometros() * 0.2 + 50

class Moto(Vehiculo):

    def costo_mantenimiento(self):
        return self.get_kilometros() * 0.05
    
mi_auto = Auto("Toyota", 2004)
mi_camion = Camion("Volvo", 2025)
mi_moto = Moto("Honda", 2023)
mi_auto.mover(150)
print(mi_auto.descripcion())
print(mi_auto.costo_mantenimiento())
print(mi_auto.costo_nafta(10))
mi_moto.mover(80)
print(mi_moto.descripcion())
print(mi_moto.costo_mantenimiento())
print(mi_moto.costo_nafta(5))

