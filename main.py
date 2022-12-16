import turtle
from turtle import Turtle, Screen

from paddle import Paddle
screen = Screen()
screen.bgcolor("Pink")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)

#Creating a paddle
paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("Black")
paddle.penup()
paddle.goto(350,0)


def move_up():
    new_y = paddle.ycor() + 20
    paddle.goto(self.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

right_paddle = Paddle((-350 , 0))
left_paddle = Paddle((350 , 0))


#turning the animation back on so the paddle can go directly from the center to the position
game_is_on = True
while game_is_on:
    screen.update()



screen.exitonclick()
