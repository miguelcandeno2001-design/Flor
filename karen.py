import turtle
import time
import random
import math

# ===== PANTALLA =====
s = turtle.Screen()
s.bgcolor("black")
s.setup(700, 800)
s.title("Buenas noches niña bonita")
s.tracer(0)

# ===== FLOR =====
flor = turtle.Turtle()
flor.hideturtle()
flor.speed(0)
flor.width(1)
flor.color("gold")

# ===== TEXTO =====
texto1 = turtle.Turtle()
texto1.hideturtle()
texto1.penup()
texto1.speed(0)

texto2 = turtle.Turtle()
texto2.hideturtle()
texto2.penup()
texto2.speed(0)

# ===== LUNA =====
luna = turtle.Turtle()
luna.hideturtle()
luna.penup()
luna.speed(0)

# ===== ESTRELLAS =====
estrellas = []
estrellas_info = []
estrellas_colores = ["white", "gold", "lightblue", "lightyellow", "lightcyan"]

# Crear múltiples tortugas para estrellas
for _ in range(60):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    estrellas.append(t)

# ===== PASTO =====
pasto = turtle.Turtle()
pasto.hideturtle()
pasto.speed(0)
pasto.color("#1fa32a")
pasto.width(2)

# =============================
# 🌙 LUNA MEJORADA (CON BRILLO)
# =============================
def dibujar_luna():
    # Luna principal (más brillante)
    luna.goto(230, 300)
    luna.color("white")
    luna.begin_fill()
    luna.circle(35)
    luna.end_fill()
    
    # Efecto de brillo (círculo más pequeño y claro en el centro)
    luna.goto(230, 320)
    luna.color("lightyellow")
    luna.begin_fill()
    luna.circle(20)
    luna.end_fill()
    
    # Cráteres pequeños para dar realismo
    luna.goto(250, 290)
    luna.color("lightgray")
    luna.begin_fill()
    luna.circle(5)
    luna.end_fill()
    
    luna.goto(200, 310)
    luna.color("lightgray")
    luna.begin_fill()
    luna.circle(7)
    luna.end_fill()

# =============================
# ⭐ ESTRELLAS CON DESTELLO
# =============================
def crear_estrellas():
    for i in range(60):
        x = random.randint(-330, 330)
        y = random.randint(120, 360)
        size = random.randint(3, 8)
        color = random.choice(estrellas_colores)
        blink_speed = random.uniform(0.5, 2.0)
        
        estrellas_info.append({
            "x": x,
            "y": y,
            "size": size,
            "color": color,
            "blink_speed": blink_speed,
            "phase": random.random() * 10,
            "max_size": size + 3,
            "min_size": max(1, size - 2)
        })
        
        # Dibujar estrella inicial
        estrellas[i].goto(x, y)
        estrellas[i].color(color)
        estrellas[i].dot(size)

# =============================
# ✨ ANIMACIÓN DE DESTELLO DE ESTRELLAS
# =============================
def animar_estrellas():
    current_time = time.time()
    
    for i in range(len(estrellas)):
        info = estrellas_info[i]
        t = estrellas[i]
        
        # Calcular tamaño basado en función seno para efecto de destello
        phase = info["phase"] + current_time * info["blink_speed"]
        pulse = (math.sin(phase) + 1) / 2
        
        # Interpolar tamaño entre min y max
        current_size = info["min_size"] + pulse * (info["max_size"] - info["min_size"])
        
        # Cambiar intensidad de color basado en el color original
        color_intensity = 0.7 + 0.3 * pulse
        
        if info["color"] == "white":
            adjusted_color = (color_intensity, color_intensity, color_intensity)
        elif info["color"] == "gold":
            adjusted_color = (color_intensity, color_intensity * 0.8, 0)
        elif info["color"] == "lightblue":
            adjusted_color = (color_intensity * 0.7, color_intensity * 0.9, color_intensity)
        elif info["color"] == "lightyellow":
            adjusted_color = (color_intensity, color_intensity, color_intensity * 0.7)
        elif info["color"] == "lightcyan":
            adjusted_color = (color_intensity * 0.7, color_intensity, color_intensity)
        else:
            adjusted_color = info["color"]
        
        # Actualizar estrella
        t.clear()
        t.goto(info["x"], info["y"])
        
        # Configurar color según el modo de color de turtle
        if isinstance(adjusted_color, tuple):
            # Convertir valores 0-1 a 0-255 si es necesario
            if s.colormode() == 255:
                r = int(adjusted_color[0] * 255)
                g = int(adjusted_color[1] * 255)
                b = int(adjusted_color[2] * 255)
                t.color((r, g, b))
            else:
                t.color(adjusted_color)
        else:
            t.color(adjusted_color)
            
        t.dot(current_size)

# =============================
# 🎨 DIBUJAR ELEMENTOS INICIALES
# =============================
dibujar_luna()
crear_estrellas()
s.update()

# =============================
# ✍️ TEXTO ORDENADO
# =============================
texto1.goto(0, -280)
texto1.color("white")
texto1.write(
    "Muy buenas noches",
    align="center",
    font=("Arial", 20, "bold")
)

texto2.goto(0, -520)
texto2.color("gold")
texto2.write(
    "Mi niña bonita",
    align="center",
    font=("Arial", 28, "bold")
)

# =============================
# 🌿 PASTO BIEN HECHO (FRANJA)
# =============================
pasto.penup()
pasto.goto(-350, -380)
pasto.pendown()

for x in range(-650, 651, 6):
    pasto.penup()
    pasto.goto(x, -520)
    pasto.setheading(90)
    pasto.pendown()
    pasto.forward(random.randint(25, 40))

s.update()

# =============================
# 🌻 FLOR ESPIRAL
# =============================
def dibujar_flor(rot):
    flor.clear()
    flor.penup()
    flor.goto(0, 60)
    flor.setheading(rot)
    flor.pendown()

    for i in range(150):
        flor.circle(180 - i, 90)
        flor.left(90)
        flor.circle(180 - i, 90)
        flor.left(18)

# =============================
# 🔁 ANIMACIÓN PRINCIPAL
# =============================
rot = 0
ultimo_tiempo_estrellas = time.time()

while True:
    # Dibujar flor
    dibujar_flor(rot)
    rot += 0.4
    
    # Animar estrellas (actualizar cada 0.1 segundos para mejor rendimiento)
    tiempo_actual = time.time()
    if tiempo_actual - ultimo_tiempo_estrellas > 0.1:
        animar_estrellas()
        ultimo_tiempo_estrellas = tiempo_actual
        s.update()  # Actualizar pantalla
    
    time.sleep(0.03)