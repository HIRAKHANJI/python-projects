import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT_TYPE = "Arial"
FONT_SIZE = 24
FONT_FORMAT = "normal"



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = (FONT_TYPE, FONT_SIZE, FONT_FORMAT))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = (FONT_TYPE, 40, FONT_FORMAT))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
