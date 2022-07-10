import time
from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Gamow")
screen.tracer(0)
snake = Snake()
food = Food()
board = Scoreboard()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.creat()
        board.score += 1
        board.refresh()
        snake.extend_segment()

    # collision with wall

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        board.reset()
        snake.reset()

    # Detect collision with self

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            board.reset()
            snake.reset()

screen.exitonclick()
