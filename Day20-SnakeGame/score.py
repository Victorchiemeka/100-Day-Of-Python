from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()  # You need to use penup() before setting the position
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()  # Call the method to write the initial score

    def update_scoreboard(self):
        self.clear()  # Clear previous text before writing new score
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
