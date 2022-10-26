import turtle
import time


def home():
    pen = turtle.Turtle()
    penText = pen.clone()
    pen.penup()
    penText.penup()
    pen.color("red")
    penText.color("red")
    penText.goto(0, 100)
    penText.write("Ping-Pong", align="center", font=("Arial", 30, "normal"))
    penText.goto(0, -60)
    penText.write("Player 1(left): Use W,S to move.",
                  align="center", font=("Arial", 15, "normal"))
    penText.goto(0, -90)
    penText.write("Player 2(right): Use UP, DOWN to move.",
                  align="center", font=("Arial", 15, "normal"))
    penText.goto(0, -120)
    penText.write("We play to 10 :)",
                  align="center", font=("Arial", 15, "normal"))

    delay = 5
    for i in range(5):
        pen.goto(0, -30)
        pen.write(f"Game starts in:{delay}.", align="center",
                  font=("Arial", 15, "normal"))
        delay -= 1
        time.sleep(1)
        pen.clear()
    penText.clear()
    penText.goto(900, 900)
    pen.goto(900, 900)
