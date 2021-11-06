from turtle import Turtle
PADDLE_MOVE_SPEED = 20

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def peddle_up(self):
        if self.ycor()< 240:
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVE_SPEED)

    def peddle_down(self):
        if self.ycor()>-240:
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE_SPEED)

