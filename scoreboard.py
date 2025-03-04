from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.score = -1

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", font=FONT)

    def game_over(self):
        pass

