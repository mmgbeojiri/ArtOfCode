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

def infinBG(times=256, r=255, g=255, b=255, radius=25):
  jump(0, 0)
  for i in range(times):
    c = (darkToColor(r,g,b, i, times))
    
    bob.begin_fill()
    bob.color(c)
    bob.circle(radius)
    bob.end_fill()
    bob.penup()
    bob.forward(i*0.3333)
    bob.right(35)
    bob.pendown()

def infiniteStairs(times=256, r=255, g=255, b=255, sides=3, dist=10):
  jump(0, 0)
  for i in range(times):
    #brown is deep orange, so that is Shades of Brown   Coffee	#6F4E37	rgb(111, 78, 55)
    
    c = (darkToColor(r,g,b, i, times))
    bob.begin_fill()
    polygon(c,sides,dist) #lets make this a circle
    bob.end_fill()
    
    bob.penup()
    
    #I would like to use a number that is a bit small
    bob.forward(i*0.1)
    bob.right(35)
    bob.pendown()


def fireSwirl(offset=0, r=255, g=255, b=255, times=100, anotherVariable=25):
  jump(0, 0)
  for i in range(times):
    c = darkToColor(r,g,b, i, times)
    comet(c, i/2, anotherVariable)



infinBG(1024, 173,231,255, 25)


infiniteStairs(1024, 196,164,132, 8, 10)
infiniteStairs(512, 150,111,214, 5, 10)
infiniteStairs(256, 255,241,146, 4, 10)

fireSwirl(0,221,235,233, 25, 25)

turtle.hideturtle()

turtle.done()
