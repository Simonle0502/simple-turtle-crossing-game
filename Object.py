from turtle import Turtle
import random
OBJECT_WIDTH = 20
OBJECT_FLOW_RANGE = int(240/OBJECT_WIDTH)
DEFAULT_WIDE = 20
DEFAULT_HEIGHT = 20
class Object(Turtle):
    def __init__(self):
        super().__init__()
        self.object_setup()

        
    
    def object_setup(self):
        self.shape("square")
        self.shape_stretch = random.randint(2,5)
        self.shape_length = self.shape_stretch * DEFAULT_WIDE
        self.shapesize(stretch_len=self.shape_stretch)
        self.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.penup()
        self.setpos(random.randint(-OBJECT_FLOW_RANGE*5,-OBJECT_FLOW_RANGE)*20,random.randint(-OBJECT_FLOW_RANGE,OBJECT_FLOW_RANGE)*20)
        self.hideturtle()
    def delete_object(self):
        self.hideturtle()
    
    def draw_object(self):
        self.showturtle()