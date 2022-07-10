from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score} Hight Score: {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} , HighScore : {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.refresh()

