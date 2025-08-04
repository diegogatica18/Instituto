import turtle

# Configuración de la ventana
wn = turtle.Screen()
wn.title("Calculadora con Turtle")
wn.setup(width=400, height=600)
wn.tracer(0)

# Variables globales
expresion = ""

# Dibujar pantalla
pantalla = turtle.Turtle()
pantalla.hideturtle()
pantalla.penup()
pantalla.goto(-180, 220)
pantalla.pendown()
pantalla.fillcolor("lightgray")
pantalla.begin_fill()
for _ in range(2):
    pantalla.forward(360)
    pantalla.right(90)
    pantalla.forward(80)
    pantalla.right(90)
pantalla.end_fill()

# Mostrar texto en pantalla
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.goto(-170, 180)

def actualizar_pantalla():
    texto.clear()
    texto.write(expresion, font=("Arial", 24, "normal"))

# Botones
botones = [
    ("7", -120, 100), ("8", -40, 100), ("9", 40, 100), ("/", 120, 100),
    ("4", -120, 30),  ("5", -40, 30),  ("6", 40, 30),  ("*", 120, 30),
    ("1", -120, -40), ("2", -40, -40), ("3", 40, -40), ("-", 120, -40),
    ("0", -120, -110), (".", -40, -110), ("=", 40, -110), ("+", 120, -110),
    ("C", -120, -180)
]

boton_turtles = []

def dibujar_boton(label, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(2):
        t.forward(60)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()
    t.penup()
    t.goto(x + 20, y - 40)
    t.write(label, font=("Arial", 24, "normal"))
    boton_turtles.append((label, x, y, x+60, y, x+60, y-60, x, y-60))
    t.penup()

for label, x, y in botones:
    dibujar_boton(label, x, y)

# Manejar clics
def click(x, y):
    global expresion
    for label, bx, by, bx2, by2, bx3, by3, bx4, by4 in boton_turtles:
        if bx <= x <= bx2 and by-60 <= y <= by:
            if label == "=":
                try:
                    expresion = str(eval(expresion))
                except:
                    expresion = "Error"
            elif label == "C":
                expresion = ""
            else:
                expresion += label
            actualizar_pantalla()
            break

actualizar_pantalla()
wn.update()
wn.onclick(click)

while True:
    wn.update()