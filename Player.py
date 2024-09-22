from turtle import Turtle
STARTING_POSITION =(0,-280)
SPEED = 5

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setup_player()

    def setup_player(self):
        self.shape("turtle")
        self.color("lime green")
        self.setheading(90)
        self.penup()
        self.setpos(STARTING_POSITION)


    def move(self):
        self.forward(SPEED)

    def is_collide(self,objects_list):
         
        for object in range(len(objects_list)):
            # NEED OPTIMISE LATER
            object_right_edge = objects_list[object].xcor() + (objects_list[object].shape_length / 2 )
            player_left_edge = self.xcor() - 10
            object_left_edge = objects_list[object].xcor() - (objects_list[object].shape_length / 2)
            player_top_edge = self.ycor() + 10
            player_bottom_edge = self.ycor() - 10
            object_top_edge = objects_list[object].ycor() + 10
            object_bottom_edge = objects_list[object].ycor() - 10
             

            if (((player_left_edge <=  object_right_edge) and (player_left_edge >= object_left_edge )) and (((player_top_edge <= object_top_edge) and (player_top_edge >= object_bottom_edge)) or ((player_bottom_edge <= object_top_edge) and (player_bottom_edge >= object_bottom_edge)))):
                return True
        return False



