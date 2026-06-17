from turtle import Turtle

STARTING_TEXT = "Score : "
POSITION = (0,270)
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(POSITION)
        self.color("white")
        self.hideturtle()
        self.update_score()

    #Display current score
    def update_score(self):
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    #Increase score after food collision
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    #Display game over message
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)
