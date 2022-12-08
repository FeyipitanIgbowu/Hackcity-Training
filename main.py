from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Fays Snake Game")

box_list = []
#creating the squares
snake_boxes = [(0, 0), (-20, 0), (-40, 0)]

for boxes in snake_boxes:
    new_box = Turtle(shape="square")
    new_box.color("Black")
    new_box.penup()
    new_box.goto(boxes)
    box_list.append(new_box)

#moving the snake
game_on = True
while game_on:
   screen.update()
   time.sleep(0.1)

   for box_num in range(len(box_list) -1, 0, -1):
       new_x = box_list[box_num - 1].xcor()
       new_y = box_list[box_num - 1].ycor()
       box_list[box_num].goto(new_x, new_y)
   box_list[0].forward(20)






#so the screen remains after running
screen.exitonclick()