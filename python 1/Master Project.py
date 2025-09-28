import turtle
t = turtle.Turtle()
r = turtle.Turtle()
a = turtle.Turtle()
r.speed(10000)
t.shape("triangle")
score = 0
r.penup()
r.goto(0,150)
r.pendown()
for i in range(36):
  r.forward(30)
  r.right(10)
t.penup()
t.forward(174)
import random
f = random.randint(0,360)
a.setheading(f)
a.penup()
a.goto(15,-15)
a.pendown()
def silver():
  a.begin_fill()
  a.forward(174)
  global xo
  global yo
  xo = a.xcor()
  yo = a.ycor()
  a.right(90)
  for i in range(2):
    a.forward(30)
    a.right(10)
  a.left(90)
  xf = a.xcor()
  yf = a.ycor()
  a.backward(174)
  a.color("red")
  global xmin
  xmin = min(xf,xo)
  global xmax
  xmax = max(xf,xo)
  global ymin
  ymin = min(yf,yo)
  global ymax
  ymax = max(yf,yo)
  a.end_fill()
silver()
t.goto(0,150)
global gameState
gameState = True
def stop():
  global gameState
  gameState = False
  print("does it talk, does it work, qwerty")
screen = turtle.Screen()
screen.onkey(stop,"Space")
screen.listen()
def playGame():
  global gameState
  global score
  while gameState:
    print(gameState)
    t.forward(30)
    t.right(10)
  x = t.xcor()
  y = t.ycor()
  if x >= xmin and x <= xmax and y >= ymin and y <= ymax:
    score += 101
  else:
   t.write("why did you lose")
playGame()
def hard():
  global gameState
  t.speed(100)
  gameState = True
  playGame()
if score > 100:
  t.write("you are now verified for SUPER HARD MODE!!")
  hard()
if score > 200:
  t.clear()
  t.write("yay")
  
