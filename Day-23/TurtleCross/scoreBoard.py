from turtle import Turtle

class ScoreBoard(Turtle):


    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.penup()
        self.hideturtle()
        self.goto(x=-260, y=260)
        self.write(f"Level: {self.player_score}", font=("courier", 20, "normal"))

    def update_score(self):
        self.player_score += 1
        self.clear()
        self.write(f"Level: {self.player_score}", font=("courier", 20, "normal"))

    def game_over(self):
        self.goto(x=-180, y=0)
        self.clear()
        self.write(f"Game Over.Final Score is {self.player_score}", font=("courier", 20, "normal"))
        