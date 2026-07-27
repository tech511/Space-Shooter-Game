import turtle

from settings import WIDTH, HEIGHT, WHITE


class Score:

    def __init__(self):

        self.score = 0

        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.speed(0)
        self.pen.color(WHITE)

        self.pen.goto(-WIDTH//2 + 20, HEIGHT//2 - 40)

        self.draw()

    def draw(self):

        self.pen.clear()

        self.pen.write(
            f"Score : {self.score}",
            align="left",
            font=("Arial", 18, "bold")
        )

    def add(self, points):

        self.score += points

        self.draw()

    def reset(self):

        self.score = 0

        self.draw()
