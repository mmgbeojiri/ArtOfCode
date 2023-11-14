from turtle import TurtleScreen
from myfunctions import *
turtle.colormode(255)
turtle.tracer(50)


# First Step: infinite brown triangle bg
# Second Step: reference the ten flowers of gayness into one big flower
# go crazy go stupid
theTenFlowersOfPride = ["red", "orange", "yellow", "green", "cyan",  "blue", "indigo","magenta","violet", "pink",]


'''
[x] Demonstrate the use of mathematical operations.  c = (int(196*(i/256)),int(164*(i/256)),int(132*(i/256)))
[x] Demonstrate the use of the loop variable in conjunction with your process.     bob.forward(i*1.3333)
[x] Demonstrate the creative application of turtle functions beyond moving and colors. tracer(10)
[x] Create functions that incorporate existing functions you've created. - myfunctions.py
'''

def infiniteStairs(times=256):
  for i in range(times):
    #brown is deep orange, so that is Shades of Brown   Coffee	#6F4E37	rgb(111, 78, 55)
    
    c = (int(255*(i/times)),int(255*(i/times)),int(255*(i/times)))
    
    polygon(darkToColor(255, 255, 255, i, times), 4, 90) #lets make this a minecraft square.
    bob.penup()
    #I would like to use a number that is a bit small
    bob.forward(i*0.333)
    bob.right(35)
    bob.pendown()

infiniteStairs(1024)

for i in range(180):
  bob.left(5)
  jump(0, 0)
  comet(theTenFlowersOfPride[i%10], i, 33)

bob.setheading(0)
times2 = 64 
for i in range(times2):
  #c = (int(111*(i/times2)),int(78*(i/times2)),int(55*(i/times2)))
  bob.color(darkToColor(111, 78, 55, i, times2))
  jump(0, 0)
  bob.circle(50)
  bob.right(int(360/times2))

turtle.done()
