import turtle as t
import random
import colorgram


timmy = t.Turtle()
timmy.shape("arrow")
timmy.color("red")

# colours = ["DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# width = 0.1
timmy.speed("fastest")
t.colormode(255)
#
def random_colour():
     r = random.randint(0, 255)
     g = random.randint(0, 255)
     b = random.randint(0, 255)
     return r, g, b
#
# for _ in range(200):
#     timmy.width(width)
#     timmy.pencolor(random_colour())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     width += 0.3

# def draw_shape(num_sides):
#     angle = 360/ num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side_n in range(3, 11):
#     draw_shape(shape_side_n)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        timmy.pencolor(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()