from turtle import Turtle
LEVEL_COLOR = "black"
LAST_LEVEL = 10
DEFAULT_LEVEL_SPEED = 6
class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color(LEVEL_COLOR)
        self.current_level = 1
        self.level_type = ("Arial",15,"bold")
        self.level_position = (-240,260) 
        self.initialise_level()



    
    def update_level(self):
        self.current_level += 1
        self.initialise_level()
    
    def is_last_level(self):
        if self.current_level == LAST_LEVEL:
            return True
        return False
    def is_pass(self,player):
        if player.ycor() >= 280:
            return True
        return False

    def initialise_level(self):
        self.level_speed = self.current_level/4 * DEFAULT_LEVEL_SPEED
        self.clear()
        self.hideturtle()
        self.penup()
        self.setpos(self.level_position)
        self.write(f"LEVEL: {self.current_level}",align= "center",font= self.level_type)
    
    