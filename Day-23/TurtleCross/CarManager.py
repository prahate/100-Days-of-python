import random
from turtle import Turtle
MOVE_CAR_DISTANCE = 5

colors = ["red", "yellow", "green", "blue", "pink", "grey"]

class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_CAR_DISTANCE)

    def increase_speed(self):
        global MOVE_CAR_DISTANCE
        MOVE_CAR_DISTANCE += 5