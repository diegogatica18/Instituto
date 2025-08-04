class golosinas:
    def __init__ (self, nombre, stock):
        self.nombre = 0

        self.stock = []

    def obtener_precio(self):
        return self.precio
    
    def verificar_stock(self):
        if self.stock > 0:
            print(f"el stock es de {self.stock} unidades")
            return True
        else:        
            self.stock == 0
            print(f"no nos queda stock de la marca {self.nombre}")
            return False
    
class caramelos(golosinas):
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock

    def obtener_precio(self):
        return self.precio
    
    def verificar_stock(self):
        if self.stock > 0:
            print(f"el stock es de {self.stock} unidades")
            return True
        else:        
            self.stock == 0
            print(f"no nos queda stock de la marca {self.nombre}")
            return False
        
    def obtener_gusto(self):
        return self.gusto
    
    def verificar_gusto(self):
        if self.gusto == "frutilla" or self.gusto == "limon" or self.gusto == "naranja":
            print(f"el gusto es {self.gusto}")
            return True
        else:
            self.gusto != "frutilla" or self.gusto != "limon" or self.gusto != "naranja"
            print(f"no tenemos el gusto {self.gusto}")
            return False

    
class verificador:
    def __init__ (self):
        self.golosinas = []

    def agregar_golosina(self, golosina):   
        self.golosinas.append(golosina)
        print(f"se agrego la golosina {golosina.nombre} a la lista")
        return self.golosinas
    
    
    def verificar_stock(self):
        for golosina in self.golosinas:
            if golosina.verificar_stock() == True:
                print(f"el stock es de {golosina.stock} unidades")
                return True
            else:
                print(f"no nos queda {golosina.nombre}")
                return False
            
        
# Ejemplo de uso
caramelo_de_frutilla = caramelos("caramelo de frutilla", 5)
caramelo_de_limon = caramelos("caramelo de limon", 0)
caramelo_de_naranja = caramelos("caramelo de naranja", 10)
caramelo_de_uva = caramelos("caramelo de uva", 5)
verificador = verificador()

verificador.agregar_golosina()
verificador.verificar_stock()
verificador.verificar_precio()
verificador.verificar_gusto()







    
        
