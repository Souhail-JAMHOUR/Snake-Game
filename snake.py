from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.creat_segment()
        self.head = self.segments[0]

    def creat_segment(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def move(self):
        for num in range(len(self.segments)-1, 0, -1):
            self.segments[num].goto(self.segments[num - 1].xcor(), self.segments[num - 1].ycor())
        self.segments[0].fd(15)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self, position):
        new_seg = Turtle()
        new_seg.penup()
        new_seg.color("white")
        new_seg.shape("square")
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend_segment(self):
        self.add_segment(self.segments[-1].position())

