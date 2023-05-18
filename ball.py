from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9 # Increasing ball speed everytime the ball hits the paddle

    def reset_location(self):
        self.goto(0, 0)
        self.ball_speed = 0.1 # Resetting ball to original value since the game restarts
        self.bounce_x()

    def increase_speed(self):
        self.speed()
