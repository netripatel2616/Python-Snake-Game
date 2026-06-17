from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#Create Game Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

#Keyboard Contols
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Main Game Loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Collision with Wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.game_over()
        game_on = False

    #Collision with itself
    body = snake.segments[1:]
    for segment in body:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()