import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player(x_cor=0, y_cor=0)
screen.listen()
screen.onkey(player.move, 'Up')
game_is_on = True

while game_is_on:
    cars = CarManager()
    cars.car_moves()
    all_cars = cars.give_list()
    for car in all_cars:
        if car.distance(player) < 30:
            game_is_on = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.write("game over")
    time.sleep(player.game_speed)
    screen.update()

screen.exitonclick()
