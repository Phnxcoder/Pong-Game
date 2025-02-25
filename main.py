import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title('Pong')
screen.bgcolor('black')
screen.tracer(0)

# Create Game Objects
r_paddle = Paddle(350, 0)  # Right paddle
l_paddle = Paddle(-350, 0)  # Left paddle
ball = Ball()
score = Scoreboard()

# Controls
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Game Loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.01)  # Keep frame updates consistent
    ball.move()

    # Bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Paddle collision
    if (ball.distance(r_paddle.paddle) < 50 and ball.xcor() > 330) or \
       (ball.distance(l_paddle.paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.move_speed *= 0.9  # Increase speed slightly when hit

    # Scoring logic
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
