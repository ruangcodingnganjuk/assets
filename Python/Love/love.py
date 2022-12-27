import turtle
import numpy as n
import tkinter as tk


turtle.bgcolor('black')
pen = turtle.Turtle()
pen.color('pink')
pen.pensize(10)
pen.speed(0)

def heart(t):
    return [160*n.sin(t)**3,130*n.cos(t)-50*n.cos(2*t)-20*n.cos(3*t)-n.cos(4*t)]

t=0
dt = 0.01*n.pi

while True:
    pen.goto(heart(t)[0],heart(t)[1])
    t+=dt