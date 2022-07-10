from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(x=0, y=280)
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score} Hight Score: {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.score} , HighScore : {self.high_score}", align="center", font=("Arial", 8, "normal"))

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.refresh()

