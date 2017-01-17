#!/usr/bin/env python3
import turtle 
def draw_triangle(turt): 
  for i in range(1,4):
    turt.forward(100)
    turt.right(120)


def draw():
  window = turtle.Screen()
  window.bgcolor("yellow")
  doyle = turtle.Turtle()
  doyle.shape("turtle")
  doyle.color("black")
  for i in range(1,37):
    doyle.left(10)
    draw_triangle(doyle)

  window.exitonclick()
  
draw()
