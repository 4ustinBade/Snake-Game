from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GO_FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle) : 

    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white") 
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score = {self.score}", False, align = ALIGNMENT, font = FONT)
    
    def refresh(self) :
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, align = ALIGNMENT, font = FONT)

    def game_over(self) : 
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", False, align = ALIGNMENT, font = GO_FONT)
        self.goto(0, 0)