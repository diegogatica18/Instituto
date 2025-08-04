class Examen:
    def __init__(self, nombre, fecha, hora):
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.preguntas = []

    def agregar_pregunta(self, pregunta):
        self.preguntas.append(pregunta)

    def mostrar_examen(self):
        print(f"Examen: {self.nombre}")
        print(f"Fecha: {self.fecha}")
        print(f"Hora: {self.hora}")
        print("Preguntas:")
        for pregunta in self.preguntas:
            print(f"- {pregunta}")
    
    def info(self):
        return f"Examen: {self.nombre}, Fecha: {self.fecha}, Hora: {self.hora}, Preguntas: {len(self.preguntas)}"



        


