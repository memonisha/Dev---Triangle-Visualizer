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

  fill (255, 255, 255)
  if distance1==distance2 and distance2==distance3:
    text ("This triangle is equilateral", 800, 90)
  elif distance1==distance2 or distance2==distance3 or distance3==distance1:
    text ("This triangle is isosceles", 800, 90)
  else:
    text ("This triangle is scalene", 800, 90)


  
  



def angles ():
  global angle1, angle2, angle3 
  #a = distance1
  #b = distance2
  #c = distance3
  '''
  Angle1 = acos((distance2**2+distance3**2-distance1**2)/2*distance2*distance3)
  Angle2 = acos((distance1**2+distance3**2-distance2**2)/2*distance1*distance3)
  Angle3 = acos((distance1**2+distance2**2-distance3**2)/2*distance1*distance2)
  angle1 = round(Angle1)
  angle2 = round(Angle2)
  angle3 = round(Angle3)
  '''

  
  a = distance1
  b = distance2
  c = distance3
  a2=a*a
  b2=b*b
  c2=c*c
  angle1 = round(acos((b2+c2-a2) / (2*b*c)))
  angle2 = round(acos((a2+c2-b2) / (2*a*c)))
  angle3 = round(180 - (angle1 + angle2))
  fill (255, 255, 255)
  if angle1==90 or angle2==90 or angle3==90:
    text ("This angle is right-angled", 800, 70)
  elif angle1<90 and angle2<90 and angle3<90:
    text ("This angle is acute", 800, 70)
  elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    text ("This angle is obtuse", 800, 70)
  
  
  
  fill ("White")
  text ("-ANGLES-", 600, 90)
  text (f"{angle1}", 600, 70)
  fill (150, 158, 153)
  text (f"{angle2}", 600, 50)
  fill (61, 61, 61)
  strokeWeight (0.9)
  stroke (255, 255, 255)
  text (f"{angle3}", 600, 30)
  
  