import turtle
from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("Pink")
screen.setup(width=800, height=600)
screen.title("My Pong Game")

#Creating a paddle
paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("Black")
paddle.penup()
paddle.goto(350,0)




screen.exitonclick()