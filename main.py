import math
import time

from paddle import Paddle
from turtle import Screen, Turtle
from ball import Ball
from scoreboard import ScoreBoard

#
screen = Screen()

# def setup_screen():
BALL_SPEED = 1
EDGE_WIDTH = 30
SCREEN_WIDTH = 800.0
SCREEN_HEIGHT = 600.0

screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)  # turn off animation

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball(SCREEN_HEIGHT, SCREEN_WIDTH)
scoreboard = ScoreBoard()
# ball.speed = BALL_SPEED
# ball.left(math.degrees(math.atan2(SCREEN_HEIGHT, SCREEN_WIDTH)))

#
# setup_paddle(350, 0)
screen.listen()
screen.onkey(key="Up", fun=right_paddle.peddle_up)
screen.onkey(key="Down", fun=right_paddle.peddle_down)
screen.onkey(key="w", fun=left_paddle.peddle_up)
screen.onkey(key="d", fun=left_paddle.peddle_down)


# create a ball
# ball = Turtle()
# ball.shape("circle")
# ball.penup()
# ball.color("white")
# # ball.left(45)
# # ball.left(math.atan2(SCREEN_HEIGHT,SCREEN_WIDTH))
# ball.forward(100)

game_is_on = True
while game_is_on:
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    if ball.ycor() > ball.window_height / 2 - EDGE_WIDTH:
        ball.bounce_y()
    elif ball.ycor() < -ball.window_height / 2 + EDGE_WIDTH:
        ball.bounce_y()

    # detection of paddle
    if ball.distance(
            right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(
            left_paddle) < 50 and ball.xcor() < - 320:  # + left_paddle.width():
        ball.bounce_x()

    # check if the paddle miss the ball
    if ball.xcor() > SCREEN_WIDTH / 2:
        ball.reset()
        scoreboard.add_point_left()

    if ball.xcor() < - SCREEN_WIDTH / 2:
        ball.reset()
        scoreboard.add_point_right()

    if max(scoreboard.score_left,scoreboard.score_right)>=3:
        game_is_on = False
        scoreboard.print_final_result()


screen.exitonclick()
