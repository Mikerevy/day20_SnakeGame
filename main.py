from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My SnakeGame")
screen.tracer(0)
screen.listen()

# Create a new objects
snake = Snake()
food = Food()
score = Score()

# Control our Snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# While the game is on
game_is_on = True

while game_is_on:
    # Set up the screen flow
    screen.update()
    time.sleep(0.1)
    # Call object snake and method move
    snake.move()

    # Detect snake collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect the wall collision
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect colision with tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()