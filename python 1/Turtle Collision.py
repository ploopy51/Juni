import turtle
import random
b = random.randint(-200,200)
c = random.randint(-200,200)
t = turtle.Turtle()
a = turtle.Turtle()
screen = turtle.Screen()
def right():
  t.right(5)
def left():
  t.left(5)
def right2():
  a.right(5)
def left2():
  a.left(5)
screen.onkey(left,"Left")
screen.onkey(left2,"A")
screen.onkey(right,"Right")
screen.onkey(right2,"D")
screen.listen()
a.penup()
a.goto(b,c)
a.pendown()
while True:
  if abs(t.xcor() - a.xcor()) < 10 and abs(t.ycor() - a.ycor()) < 10:
    t.write("collision")
  t.forward(1)
  a.forward(1)
