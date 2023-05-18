from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.up, 'Up')
screen.onkey(right_paddle.down, 'Down')
screen.onkey(left_paddle.up, 'w')
screen.onkey(left_paddle.down, 's')

game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    ball.move()
    screen.update()

    # Detect collision of the ball with the top and bottom wall and bounce the ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle and bounce the ball
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.increase_speed()

    # Detect when right paddle misses the ball
    if ball.xcor() > 370:
        ball.reset_location()
        score.increase_l_score()  # Increase score for one paddle when the other misses the ball

    # Detect if left paddle misses the ball
    if ball.xcor() < -370:
        ball.reset_location()
        score.increase_r_score()

screen.exitonclick()
