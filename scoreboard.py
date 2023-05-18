from turtle import Turtle
FONT = ('Courier', 50, 'normal')
ALIGNMENT = 'center'
R_SCORE_POSITION = (100, 220)
L_SCORE_POSITION = (-100, 220)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.r_score = 0
        self.l_score = 0
        self.hideturtle()
        self.penup()
        self.print_score()

    def increase_r_score(self):
        self.r_score += 1
        self.print_score()

    def increase_l_score(self):
        self.l_score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.goto(L_SCORE_POSITION)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(R_SCORE_POSITION)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)