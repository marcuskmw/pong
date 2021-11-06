from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.penup()
        self.hideturtle()
        self.color("white")


        # self.print_score()
        self.refresh()


    def add_point_left(self):
        self.score_left+=1
        self.refresh()

    def add_point_right(self):
        self.score_right+=1
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def print_final_result(self):
        self.refresh()
        if self.score_right>self.score_left:
            self.goto(100, 0)
            self.write("Winner >>>>", align="center", font=("Courier", 60, "normal"))
        else:
            self.goto(-100, 0)
            self.write("<<<< Winner", align="center", font=("Courier", 60, "normal"))
