from elements.game_objects.constants import Constants
from elements.game_objects.game_objects.text import Text
from game_engine.game_object import GameObject
from game_engine.color import Color
from pygame.math import Vector2

class ScoreController(GameObject):

    def start(self):

        font_path = "assets/fonts/neuropolxrg.ttf"

        self.number_of_steps_to_update_score = 20
        self.score_per_step = 1  # Number of steps of the game required to update the score
        self.current_step = 0

        self.score = 0.0
        score_x = 10.0
        score_y = 5.0
        score_message = str(int(self.score))
        score_color = Color.white
        score_size = 15

        self.game_object_list = [
            Text(Vector2(score_x, score_y), score_message, score_color, score_size, font_path)
        ]
        self.game_object_list[0].text_mesh.message = str(int(self.score))

    def update(self):
        self.current_step += 1
        if(self.current_step == self.number_of_steps_to_update_score):
            self.score = self.score + self.score_per_step
            self.current_step = 0
            Constants.current_score = self.score
            self.game_object_list[0].text_mesh.message = str(int(self.score))

