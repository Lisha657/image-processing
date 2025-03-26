# How to draw a square and hexagon using the Turtle module in Python

import turtle

# Draw Square
t = turtle.Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)

# Draw Hexagon
for _ in range(6):
    t.forward(100)
    t.right(60)

turtle.done()
