from turtle import TurtleScreen
from myfunctions import *
turtle.colormode(255)
turtle.tracer(100)
bob.speed(0)


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
    bob.color(darkToColor(13,119,238, i, times))
    bob.begin_fill()
    bob.circle(25) #lets make this a circle
    bob.end_fill()
    
    bob.penup()
    
    #I would like to use a number that is a bit small
    bob.forward(i*0.333)
    bob.right(35)
    bob.pendown()

infiniteStairs(1024)

def fireSwirl(offset=0, r=255, g=255, b=255, times=100, anotherVariable=25):
  jump(0, 0)
  for i in range(times):
    c = darkToColor(r,g,b, i, times)
    comet(c, i/2, anotherVariable)

fireSwirl(720, 8,9,66, 200,17)
fireSwirl(540,34,28,105, 175,19)
fireSwirl(360,67,28,118, 150,21)
fireSwirl(180,102,59,148, 125, 23)
fireSwirl(0,132,77,163, 100,25)

fireSwirl(0,142,119,173, 50,25)


turtle.done()
