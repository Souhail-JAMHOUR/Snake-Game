import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("Blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.creat()

    def creat(self):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        self.goto(x, y)
