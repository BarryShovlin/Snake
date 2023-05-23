from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.show_score()

    def show_score(self):
        self.write(f"Score: {self.score}", False, align="center", font=("ariel", 20, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=("goudy_oldstyle", 80, "bold"))

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.show_score()