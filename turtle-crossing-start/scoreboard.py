from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()

        self.goto(-295, 265)

        self.write(f"Level: {self.level}", align = "left", font = FONT)


    def update_level(self):
        self.clear()
        self.level_up()
        self.write(f"Level: {self.level}", align = "left", font = FONT)


    def level_up(self):
        self.level += 1

    def game_over(self):

        self.goto(0, 0)
        self.write("GAME OVER!", align = "center", font = ("Courier", 40, "normal"))