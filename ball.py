from turtle import Turtle
import math
import random


class Ball(Turtle):


    def increase_speed(self):
        self.speed*=0.9
        print(self.speed)

    def __init__(self, window_height, window_width):
        super().__init__()
        self.speed =0.1
        self.shape("circle")
        self.penup()
        self.color("white")
        self.window_height = window_height
        self.window_width = window_width
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.last_bounce_x_at = 0

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if abs(self.last_bounce_x_at - self.xcor()) > 20:
            self.x_move *= -1
            self.last_bounce_x_at = self.xcor()
            self.increase_speed()

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move * self.speed
        # new_x = self.xcor() + self.x_move * self.speed
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)
        self.x_move *= random.choice((-1, 1))
        self.y_move *= random.choice((-1, 1))
        self.speed=0.1
