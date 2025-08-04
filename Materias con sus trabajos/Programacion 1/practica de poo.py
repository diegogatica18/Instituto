""""
class Auto:
    marca = ""
    modelo = 2004
    laca = ""

taxi = Auto()
print(taxi.modelo)

#otra clase 
class Jugadores_A:
    j1 = "messi"
    j2 = "c.ronaldo"

class Jugadores_B:
    j3 = "marcelo"
    j1 = "falcao"

print(Jugadores_B.j1)

class Auto_taxi:
    marca = "nissan"
    modelo = 2004
    placa = "123-ABC"

class Auto_patrulla:
    marca = "toyota"
    modelo = 2017
    placa = "789-XYZ"

#otra clase

class Nombre:
    pass

victor = Nombre()
maria = Nombre()

victor.edad = 30
victor.sexo = "masculino"
victor.pais = "bolivia"

maria.edad = 25
maria.sexo = "femenino"
maria.pais = "colombia"

print(victor.edad)
print(maria.edad)

class Auto_n():
    pass

taxi = Auto()
patrullero = Auto()

taxi.marca = "nissan"
taxi.modelo = 2004
taxi.placa = "123_ABC"

patrullero.marca = "toyota"
patrullero.modelo = 2017
patrullero.placa = "789_XYZ"

print(taxi.marca)
print(patrullero.marca)

class Matematica:
    def suma (self):

        self.numero1 = 10
        self.numero2 = 10

s = Matematica()
s.suma()
print(s.numero1 + s.numero2)

#otra clase
class Auto:
    def caracteristicas (self):

        self.marca = "nissan"
        self.modelo = 2004
        self.placa = "123_ABC"

a = Auto()
a.caracteristicas()
print("la marca del auto es:", a.marca)


class Ropa:
    def __init__ (self):

        self.marca = "nike"
        self.talla = "xl"
        self.color = "negro"

camisa = Ropa()
print(camisa.marca)
print(camisa.talla)
print(camisa.color)

class Auto:
    def __init__ (self):

        self.marca = "nissan"
        self.modelo = 2004
        self.placa = "123-ABC"

autito = Auto()
print(f"la marca del auto es: {autito.marca}")

class Calculadora:
    def __init__ (self, n1, n2):
        
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.multiplicacion = n1 * n2
        self.division = n1 / n2

operacion = Calculadora(10, 5)
print(f"la suma es: {operacion.suma}")

class Auto:
    def __init__ (self, marca, modelo, placa):

        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def saludo_taxi(self):
        print(f"hola, mi marca es {self.marca} y mi modelo es {self.modelo} y mi placa es {self.placa}")

taxi = Auto("nissan", 2004, "123-ABC")
taxi.saludo_taxi()

class Persona:
    edad = 27
    nombre = "victor"
    pais = "bolivia"

doctor = Persona()

print("la edad es:", doctor.edad)
print("la edad es:", getattr(doctor, "edad"))

print("el doctor tiene una edad?", hasattr(doctor, "edad"))
print("el doctor tiene una edad?", hasattr(doctor, "apellido"))

print("antes era:", doctor.nombre)
setattr(doctor, "nombre", "hector")
print("ahora es:", doctor.nombre)

#borrar atributo
delattr(Persona, "pais")
print(doctor,pais)


#usarlo para el taxi y la patrulla
class Pokemon:
    pass
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def descripcion(self):
        return "{} es un pokemon de tipo: {}".format(self.nombre, self.tipo)
    
class Pikachu(Pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

class Charmander(Pokemon):
    def ataque(self, tipoataque):
        return "{} tipo de ataque: {}".format(self.nombre, tipoataque)

nuevo_pokemon = Pikachu("body", "elctrico")
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque("impacto de trueno pffffffffffffffff")) 
"""

class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]
#coloco un algoritmo para definir el dato

    def ingresardato(self):
        self.datos = [int(input("ingresar dato " + str(i+1)+ "=")) for i in range(self.n)]

class op_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 2)

    def suma(self):
        a,b, = self.datos
        s = a + b
        print("el resultado es: ", s)

    def resta(self):
        a,b, = self.datos
        s = a - b
        print("el resultado es: ", s)

    def multiplicacion(self):
        a,b, = self.datos
        s = a * b
        print("el resultado es: ", s)

    def division(self):
        a,b, = self.datos
        s = a / b
        print("el resultado es: ", s)

class Raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        import math
        a, = self.datos
        print("el resultado es: ", math.sqrt(a))

#para obtener resultados
"""ejemplo = Raiz()
print(ejemplo.ingresardato())
print(ejemplo.cuadrada())

ejemplo = op_basicas()
print(ejemplo.ingresardato())
print(ejemplo.suma())
"""

#comprobacion para saber si esta trabajando con la funcion indicada
"""print(issubclass(Calculadora, op_basicas))
print(issubclass(op_basicas, Calculadora))
"print(issubclass(potencia, Calculadora))"
print(issubclass(Raiz, Calculadora))
"""

class Telefono():
    def __init__(selft):
        pass
    
    def llamar(self):
        print("llamando....")
    
    def ocuapado(self):
        print("ocuapdo.....")

class Camara:
    def __init__(self):
        pass

    def fotografia(self):
        print("Tomando fotos......")
    
class Reproduccion:
    def __init__(self):
        pass

    def reproducciones(self):
        print("reproduciendo musica.....")

    def reproducirvideo(self):
        print("reproduciendo video.....")
    
class Smartphone(Telefono, Camara, Reproduccion):
    def __del__(self):
        print("telefono apagado")

movil = Smartphone()
movil.fotografia()
movil.llamar()