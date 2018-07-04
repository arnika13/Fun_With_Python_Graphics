# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:44:40 2018

@author: LocalUser
"""
import turtle

turtle.bgcolor("black")

colors=["yellow","blue","red","green","orange","purple","pink"]

t = turtle.Turtle()

t.speed(20)

for x in range(360):
    t.pencolor(colors[x%len(colors)])
    t.width(x/150+1)
    t.forward(x)
    t.left(60)
    
turtle.done()
