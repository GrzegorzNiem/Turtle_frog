from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 300
cars = []


class CarManager(Turtle):
    def __init__(self):
        coinflip = random.randint(0, 5)
        if coinflip == 0:
            super().__init__()
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.shape('square')
            self.penup()
            self.color(random.choice(COLORS))
            random_y = random.randint(-200, 200)
            self.setposition(300, random_y)
            self.setheading(180)
            cars.append(self)

    def car_moves(self):
        for car in cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def give_list(self):
        return cars
