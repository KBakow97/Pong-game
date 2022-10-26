import turtle
import random
ball1 = turtle.Turtle()
random_list1 = [0.3, 0.4]
random_list2 = [-0.4, -0.3]
random_list3 = [-0.4, -0.3, 0.3, 0.4]
ball1.speed(10)
ball1.shape("circle")
ball1.color("green")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = random.choice(random_list1)
ball1.dy = random.choice(random_list3)
ball2 = ball1.clone()
ball2.color("blue")
ball1.dx = random.choice(random_list2)
ball1.dy = random.choice(random_list3)
balls = [ball1, ball2]
