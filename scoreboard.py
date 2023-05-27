from turtle import Turtle, Screen


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pencolor("white")
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align="center", font=("ariel", 20, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, align="center", font=("goudy_oldstyle", 80, "bold"))

    def refresh_score(self):
        self.score += 1
        self.show_score()