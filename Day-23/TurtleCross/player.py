from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.seth(90)
        self.goto(0, -280)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(0, -280)