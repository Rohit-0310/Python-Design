import turtle
import colorsys

Tur = turtle.Turtle()
Scr = turtle.Screen()
Tur.speed(0)
Scr.bgcolor("black")
n = 10
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1/n
    Tur.color(c)
    Tur.left(10)
    for j in range(5):
        Tur.forward(230)
        Tur.left(144)


# for i in range(500):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h += 1/n
#     Tur.color(c)
#     Tur.forward(i*2)
#     Tur.left(145)