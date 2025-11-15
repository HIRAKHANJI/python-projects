# import colorgram
import turtle as turtle_module
import random
from operator import index

from PIL.ImageChops import screen

# rgb_color = []
# colors = colorgram.extract('download.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
#
# print(rgb_color)

tim = turtle_module.Turtle()
tim.color("green")
tim.shape("turtle")
turtle_module.colormode(255)

extracted_colors = [(249, 248, 243), (250, 244, 248), (243, 250, 246), (242, 246, 250),
                    (234, 225, 83), (195, 8, 69), (231, 53, 131), (194, 164, 15), (113, 177, 212),
                    (198, 77, 16), (216, 162, 100), (29, 104, 166), (34, 187, 113), (14, 23, 63), (20, 29, 168),
                    (211, 136, 175), (230, 224, 8), (196, 35, 130), (15, 182, 211), (230, 167, 198), (127, 190, 164),
                    (10, 48, 29), (41, 131, 75), (142, 218, 203), (61, 13, 26), (64, 23, 10), (109, 91, 210), (235, 64, 34),
                    (131, 217, 230), (183, 18, 9)]


x_axis = tim.xcor()
y_axis = 0

def color_picker():
    extracted_colors_rand = random.randrange(0, 29)
    r_temp = extracted_colors[extracted_colors_rand][0]
    b_temp = extracted_colors[extracted_colors_rand][1]
    g_temp = extracted_colors[extracted_colors_rand][2]
    return r_temp, b_temp, g_temp

def dot_plotter():
       for j in range(10):
        global y_axis
        for i in range(10):
            tim.dot(10, color_picker())
            tim.penup()
            tim.forward(20)
            tim.pendown()
        tim.penup()
        tim.setx(x_axis)
        y_axis += 20
        tim.sety(y_axis)




dot_plotter()




display = turtle_module.Screen()
display.exitonclick()