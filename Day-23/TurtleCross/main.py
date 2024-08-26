from turtle import Turtle,Screen
import time
from CarManager import CarManager
from player import Player
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Cross")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = ScoreBoard()


screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 30:
            game_is_on = False
            score.game_over()

    # detect if turtle reached other end
    if player.ycor() > 250:
        player.reset_position()
        car_manager.increase_speed()
        score.update_score()

    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()