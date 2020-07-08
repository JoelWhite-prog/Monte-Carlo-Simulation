from tkinter import *
import random
import math

class Dot:
   def __init__(self,x,y,color):
      self.radius = 2
      self.color = color
      self.object = canvas.create_oval(x-self.radius,y-self.radius,x+self.radius,y+self.radius,fill=self.color)

tk = Tk()
canvas = Canvas(width=500, height=500)
canvas.pack()

domain = canvas.create_rectangle(99,99,401,401)
origin_x = 100
origin_y = 400
iterations = 100000
dots_in_quadrant = 0
dots = []

for n in range(0,iterations):
   x = random.randint(100,400)
   y = random.randint(100,400)
   actual_x = (x - origin_x)/300
   actual_y = (origin_y - y)/300
   if math.sqrt((actual_x**2+actual_y**2)) < 1:
      dots.append(Dot(x,y,"red"))
      dots_in_quadrant = dots_in_quadrant + 1
   else:
      dots.append(Dot(x,y,"blue"))

print("Dots in quadrant: " + str(dots_in_quadrant))
print("Ratio: "+ str(dots_in_quadrant / iterations))
print("Pi approximation: "+str(4*dots_in_quadrant / iterations))
      
