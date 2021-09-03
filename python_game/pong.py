"""
project: pong game tutorial from freecodecamp
will also make this into a multiplayer game as well 

date:  08/25/2021

"""

import turtle


wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width = 800, height =600)
wn.tracer(0) #this stops window from updating


# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")

paddle_a.shapesize(stretch_wid = 5,stretch_len= 1)
paddle_a.penup()
paddle_a.goto(350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")

paddle_b.shapesize(stretch_wid = 5,stretch_len= 1)
paddle_b.penup()
paddle_b.goto(-350,0)

#ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")

ball.shapesize()
ball.penup()
ball.goto(0,0)
ball.dx = 1
ball.dy = 1


#function paddle a 
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#function paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")  
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down") 

# Main game loop 
while True: 
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking 
    #Top and Bottom
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() <  -290: 
        ball.sety(-290)
        ball.dy *= -1 
    #Left and Right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1 

    if ball.xcor() <  -390:
        ball.goto(0,0)
        ball.dx *= -1 

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350 and  (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50)):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() > -340 and ball.xcor() < -350 and  (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50)):
            ball.setx(-340)
            ball.dx *= -1
    