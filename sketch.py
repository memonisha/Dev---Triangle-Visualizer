from p5 import *


def setup():
  createCanvas(windowWidth,windowHeight)
  global a, b, c, distance1, distance2, distance3
  a=createMovableCircle(200,450,20)
  b=createMovableCircle(500,500,20)
  c=createMovableCircle(400,200,20)
  angleMode(DEGREES)
  
  

def draw():
  background('black')
  #drawTickAxes()
  fill ('white')
  
  push ()
  strokeWeight (10)
  stroke (50, 98, 168)
  line (a.x, a.y, b.x, b.y)
  stroke (235, 9, 69)
  line (b.x, b.y, c.x, c.y)
  stroke (9, 235, 99)
  line (c.x, c.y, a.x, a.y)
  pop ()
  fill ("white")
  a.draw()
  fill (150, 158, 153)
  b.draw ()
  fill (61, 61, 61)
  c.draw ()
  cordtext ()
  distances ()
  angles ()

def cordtext ():
  fill ("white")
  text ("-COORDS-", 50, 90)
  text (f"({a.x}, {a.y})", 50, 70)
  fill (150, 158, 153)
  text (f"({b.x}, {b.y})", 50, 50)
  push ()
  fill (61, 61, 61)
  strokeWeight (0.9)
  stroke ("white")
  text (f"({c.x}, {c.y})", 50, 30)
  pop ()
def distances ():
  global distance1, distance2, distance3
  distance1 = round(sqrt ((a.x-b.x)**2 + (a.y-b.y)**2))
  distance2 = round(sqrt((b.x-c.x)**2 + (b.y-c.y)**2))
  distance3 = round(sqrt ((c.x-a.x)**2+(c.y-a.y)**2))
  fill ("white")
  text ("-DISTANCES-", 300, 90)
  fill (50, 98, 168)
  text (f"{distance1}", 300, 70)
  fill (235, 9, 69)
  text (f"{distance2}", 300, 50)
  fill (9, 235, 99)
  text (f"{distance3}", 300, 30)

def angles ():
  global angle1, angle2, angle3 
  #a = distance1
  #b = distance2
  #c = distance3
  Angle1 = acos ((distance2**2+distance3**2-distance1**2)/2*distance2*distance3)
  Angle2 = acos ((distance1**2+distance3**2-distance2**2)/2*distance1*distance3)
  Angle3 = acos ((distance1**2+distance2**2-distance3**2)/2*distance1*distance2)
  angle1 = round(Angle1)
  angle2 = round(Angle2)
  angle3 = round(Angle3)
  fill ("White")
  text ("-ANGLES-", 600, 90)
  text (f"{angle1}", 600, 70)
  fill (150, 158, 153)
  text (f"{angle2}", 600, 50)
  fill (61, 61, 61)
  strokeWeight (0.9)
  stroke (255, 255, 255)
  text (f"{angle3}", 600, 30)
  
  