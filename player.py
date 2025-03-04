from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

scoreboard = Scoreboard()
scoreboard.update_score()


class Player(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.setposition(STARTING_POSITION)
        self.curr_x = x_cor
        self.game_speed = 0.1

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.curr_x, new_y)
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.game_speed *= 0.5
            scoreboard.update_score()

    def game_over(self):
        self.game_speed = 2000


