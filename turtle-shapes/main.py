from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)

def move_left():

    tim.left(10)
    tim.forward(10)

def move_right():
    tim.right(10)

def move_back():
    tim.back(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_back, "s")
screen.onkeypress(move_right, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()

