import turtle as T
import random
import time


def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branch / 2)
        else:
            t.color('sienna')
            t.pensize(branch / 10)
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


def Petal(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def draw_fancy_text():
    """Dibuja texto con estilo decorativo"""
    text_turtle = T.Turtle()
    text_turtle.hideturtle()
    text_turtle.speed(0)
    text_turtle.penup()
    
    # Posicionar para el texto principal
    text_turtle.goto(0, -280)
    
    # Palabra "bonito" - en rosa suave con sombra
    text_turtle.color('hotpink')
    text_turtle.write("b", align="center", font=("Comic Sans MS", 28, "bold"))
    text_turtle.forward(25)
    text_turtle.write("o", align="center", font=("Comic Sans MS", 28, "bold"))
    text_turtle.forward(25)
    text_turtle.write("n", align="center", font=("Comic Sans MS", 28, "bold"))
    text_turtle.forward(25)
    text_turtle.write("i", align="center", font=("Comic Sans MS", 28, "bold"))
    text_turtle.forward(25)
    text_turtle.write("t", align="center", font=("Comic Sans MS", 28, "bold"))
    text_turtle.forward(25)
    text_turtle.write("o", align="center", font=("Comic Sans MS", 28, "bold"))
    
    # Palabra "día" - en naranja con corazón
    text_turtle.color('orange')
    text_turtle.goto(0, -320)
    text_turtle.write("d", align="center", font=("Arial", 30, "italic", "bold"))
    text_turtle.forward(25)
    text_turtle.color('lightcoral')
    text_turtle.write("í", align="center", font=("Arial", 30, "italic", "bold"))
    text_turtle.color('orange')
    text_turtle.forward(25)
    text_turtle.write("a", align="center", font=("Arial", 30, "italic", "bold"))
    
    # Corazón decorativo
    text_turtle.color('red')
    text_turtle.forward(30)
    text_turtle.write("❤", align="center", font=("Arial", 25, "bold"))
    
    # Palabra "mi" - en azul suave
    text_turtle.color('skyblue')
    text_turtle.goto(-70, -360)
    text_turtle.write("m", align="center", font=("Verdana", 26, "bold"))
    text_turtle.forward(25)
    text_turtle.write("i", align="center", font=("Verdana", 26, "bold"))
    
    # Palabra "niña" - en morado con flor
    text_turtle.color('mediumpurple')
    text_turtle.goto(20, -360)
    text_turtle.write("n", align="center", font=("Georgia", 32, "bold"))
    text_turtle.forward(30)
    text_turtle.write("i", align="center", font=("Georgia", 32, "bold"))
    text_turtle.forward(30)
    text_turtle.write("ñ", align="center", font=("Georgia", 32, "bold"))
    text_turtle.forward(30)
    text_turtle.write("a", align="center", font=("Georgia", 32, "bold"))
    
    # Decoración floral
    text_turtle.color('lightcoral')
    text_turtle.goto(150, -360)
    text_turtle.write("✿", align="center", font=("Arial", 25, "bold"))
    
    # Palabra "bonita" - en rosa degradado con estrellas
    text_turtle.goto(0, -400)
    
    # Letras de "bonita" con diferentes tonos
    colors = ['deeppink', 'hotpink', 'pink', 'lightpink', 'deeppink', 'hotpink']
    letters = ['b', 'o', 'n', 'i', 't', 'a']
    
    for i in range(6):
        text_turtle.color(colors[i])
        text_turtle.write(letters[i], align="center", font=("Impact", 34, "bold"))
        text_turtle.forward(28)
    
    # Estrellas decorativas
    text_turtle.color('gold')
    text_turtle.goto(-110, -390)
    text_turtle.write("★", align="center", font=("Arial", 20, "bold"))
    text_turtle.goto(180, -390)
    text_turtle.write("★", align="center", font=("Arial", 20, "bold"))


# Configuración principal
t = T.Turtle()
w = T.Screen()

t.hideturtle()
t.getscreen().tracer(5, 0)
w.screensize(bg='wheat')
w.bgcolor('wheat')
w.title("Para la más bonita 💖")

# Posicionar el árbol
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')

# Dibujar el árbol
Tree(60, t)

# Dibujar pétalos
Petal(200, t)

# Dibujar texto decorativo
draw_fancy_text()

# Añadir algunos corazones flotantes alrededor del texto
def draw_floating_hearts():
    heart_turtle = T.Turtle()
    heart_turtle.hideturtle()
    heart_turtle.speed(0)
    heart_turtle.penup()
    
    heart_colors = ['red', 'pink', 'lightcoral', 'hotpink']
    positions = [(-200, -300), (200, -300), (-150, -350), (150, -350), 
                 (-220, -380), (220, -380), (-180, -420), (180, -420)]
    
    for pos in positions:
        heart_turtle.goto(pos)
        heart_turtle.color(random.choice(heart_colors))
        heart_turtle.write("♥", align="center", font=("Arial", random.randint(15, 25), "bold"))

draw_floating_hearts()

w.exitonclick()