import turtle
bob = turtle.Turtle()

def polygon(c,sides, distance ):
  bob.color(c)
  angle = 360 / sides
  bob.begin_fill()
  for times in range(sides):
    bob.forward(distance)
    bob.left(angle)
  bob.end_fill()

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()

def home():
  bob.penup()
  bob.home()
  bob.pendown()

def swirl():
  for times in range(120):
    value = times * 2
    c = (value,0,255 - value)
    bob.color(c)
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    bob.left(1)
    bob.forward(1)

  for times in range(120):
    value = times * 2
    c = (240 - value,0,value)
    bob.color(c)
    bob.begin_fill()
    bob.circle(20)
    bob.end_fill()
    bob.right(1)
    bob.forward(0.5)

def comet(c, distance, angle):
  bob.color(c)
  for times in range(10):
    bob.pensize(times)
    bob.forward(distance)
    bob.left(angle)

