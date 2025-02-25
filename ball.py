from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1  # Initial move speed

    def move(self):
        if self.dx == 0 and self.dy == 0:  # Prevent ball from stopping
            self.dx, self.dy = 10, 10  
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1  # Reverse direction

    def bounce_x(self):
        self.dx *= -1  # Reverse direction

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1  # Reset speed after scoring
        self.bounce_x()
