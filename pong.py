import turtle
from home_screen import home
from paddles import *
import winsound
from balls import balls
import time


wn = turtle.Screen()
wn.title("Ping_Pong Kacper Bąkowski")
wn.bgcolor("black")
wn.tracer(0)
wn.setup(width=800, height=600)
pen = turtle.Turtle()
pen.penup()
home()

# Score
score_a = 0
score_b = 0


# Pen
pen.speed(1)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Arial", 24, "normal"))


# Keyboard binding
wn.listen()
wn.onkey(paddle_a_up, "w")
wn.onkey(paddle_a_down, "s")
wn.onkey(paddle_b_up, "Up")
wn.onkey(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()
    for ball in balls:
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound('wall.wav', winsound.SND_ASYNC)

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
            winsound.PlaySound('wall.wav', winsound.SND_ASYNC)

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(
                score_a, score_b), align="center", font=("Arial", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(
                score_a, score_b), align="center", font=("Arial", 24, "normal"))

        # Paddle and ball collisions
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

        if score_a == 10:
            pen.goto(0, 25)
            pen.color("red")
            pen.write("Player1 win !!", align="center",
                      font=("Arial", 30, "normal"))
            time.sleep(3)
            quit()
        elif score_b == 10:
            pen.goto(0, 25)
            pen.color("red")
            pen.write("Player2 win !!", align="center",
                      font=("Arial", 30, "normal"))
            time.sleep(3)
            quit()
