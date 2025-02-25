from turtle import Turtle

class Paddle:
    def __init__(self, x_pos, y_pos):
        self.paddle = Turtle("square")
        self.paddle.speed(0)
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(x_pos, y_pos)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        if new_y < 250:  # Prevent moving out of bounds
            self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        if new_y > -240:  # Prevent moving out of bounds
            self.paddle.goto(self.paddle.xcor(), new_y)
