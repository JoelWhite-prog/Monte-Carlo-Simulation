import random
import math

domain = [100,100,100]

iterations = 100000
points = []
points_within_condition = 0

for i in range(0,iterations):
   x = random.randint(0,100)
   y = random.randint(0,100)
   z = random.randint(0,100)
   if math.sqrt((x/100)**2 + (y/100)**2 + (z/100)**2) < 1:
      points_within_condition = points_within_condition+1
   points.append([x,y,z])
print("Points within boundary: "+str(points_within_condition))
print("Pi approximation: "+str(6*points_within_condition/iterations))
