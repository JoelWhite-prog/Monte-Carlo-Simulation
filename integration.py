from tkinter import *
import math
import random

class Dot:
   def __init__(self,x,y,color):
      self.radius = 2
      self.color = color
      self.object = canvas.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill=self.color)

tk = Tk()
canvas = Canvas(width=500,height=500)
canvas.pack()

domain = canvas.create_rectangle(99,99,401,401)
dots = []
in_boundary = 0
iterations = 10000

## This function describes the domain (Currently set to a hyperbola)
def function(x,y):
   if -2*x**2+2*x > y or 2*x**2-2*x + 1 < y:
      return True
   else:
      return False

for i in range(0,iterations):
   x = random.randint(100,400)
   y = random.randint(100,400)
   actual_x = (x-100)/300
   actual_y = (400-y)/300
   if function(actual_x,actual_y):
      in_boundary = in_boundary + 1
      dots.append(Dot(x,y,"red"))
   else:
      dots.append(Dot(x,y,"blue"))
print("Result = "+str(in_boundary/iterations))
