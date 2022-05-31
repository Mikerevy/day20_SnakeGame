from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super(Score, self).__init__()
        self.count_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.count_score}, High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.count_score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.count_score > self.high_score:
            self.high_score = self.count_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.count_score = 0
        self.update_score()





    #
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))