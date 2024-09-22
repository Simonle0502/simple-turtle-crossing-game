from turtle import Turtle, Screen
from Player import Player
from Object_handling import Objects
from Level_handle import Level
import time
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
TEXT_TYPE =("Arial",10,"bold")

class Gameplay():
    def __init__(self):
        self.screen = Screen()
        self.game_on = True
        self.time = time
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("navajo white")
        self.screen.title("Turtle Crossing game")
        self.screen.colormode(255)
        self.screen.tracer(0)
        # Close the window when the close button is clicked
        self.screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.stop_game)
        self.object_setup()

    def object_setup(self):
        self.player = Player()
        self.level = Level()
        self.object = Objects(self.level.level_speed)


    def game_update(self):
        self.level.update_level()
        self.object.update_speed(self.level.level_speed)
        self.player.setup_player()

    def key_control(self):
        self.screen.listen()
        self.screen.onkey(self.stop_game, "q")  # Press 'q' to stop the game
        self.screen.onkeypress(self.player.move,"Up")

    def stop_game(self):
        self.game_on = False

    def game_end_screen(self):
        self.screen.clear()
        self.screen.bgcolor("navajo white")
        result = Turtle()
        result.color("black")
        result.hideturtle()
        self.screen.update()
        result.write(f"\tGAME OVER \n YOUR HIGHEST LEVEL IS: {self.level.current_level}",align="center",font=TEXT_TYPE)
    def play(self):
        while self.game_on:
            self.object.draw_objects()
            self.object.move_objects()
            self.object.update_objects()
            if self.player.is_collide(self.object.objects_list):
                self.stop_game()
            if self.level.is_pass(self.player):
                self.game_update()
            self.key_control()
            self.screen.update()
            self.time.sleep(0.02)

        self.game_end_screen()
        self.screen.exitonclick()

test = Gameplay()
test.play()

    
