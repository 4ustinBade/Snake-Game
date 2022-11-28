from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
GO_FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle) : 

    def __init__(self) :
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("white") 
        self.goto(0, 260)
        self.write(f"Score : {self.score} Highscore : {self.high_score}", False, align = ALIGNMENT, font = FONT)
    
    def refresh(self) :
        self.clear()
        self.write(f"Score : {self.score}  Highscore : {self.high_score}", False, align = ALIGNMENT, font = FONT)

    def reset(self) :
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
            self.refresh()
            

    def increase_score(self) :
        self.score += 1
        self.refresh()

    
"""
   def game_over(self) : 
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write(f"GAME OVER!!!", False, align = ALIGNMENT, font = GO_FONT)
        self.goto(0, 0)
"""""