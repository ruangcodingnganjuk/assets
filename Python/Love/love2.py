import numpy as np
import turtle

# Membuat objek turtle
# t = turtle.Turtle()

# Mengubah warna pen turtle menjadi pink
# t.color('pink')

# Mengubah background jendela turtle menjadi gelap
turtle.bgcolor('black')
t = turtle.Turtle()
t.color('blue')
t.pensize(10)
t.speed(5)

# Membuat data koordinat
t_values = np.linspace(0, 4*np.pi, 100)
x_values = 160*np.sin(t_values)**3
y_values = 130*np.cos(t_values) - 50*np.cos(2*t_values) - 20*np.cos(3*t_values) - np.cos(4*t_values)

# Menampilkan garis koordinat
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)

# Memplot garis dengan turtle
for i in range(len(x_values)):
    t.goto(x_values[i], y_values[i])

# Menampilkan jendela turtle
turtle.done()

