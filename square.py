#!/usr/bin/env python

import turtle



def quit():
    turtle.bye()
def square(t,x: float, y: float):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(4):
            t.left(90)
            t.forward(100)
    """draw a square at postion (x,y) parameters:
      t : the turtle
      x : the start x position
      y : the start y position
    """    


# crest my main turtle
guigui = turtle.Turtle()
guigui.shape("turtle")
#tell the screen to listen for key events
turtle.Screen().listen()
#if the escape kkey is pressed exit
turtle.onkeypress(quit, key="Escape")
#enter main loop so window stays in view
square(guigui,500,10)
turtle.mainloop()
