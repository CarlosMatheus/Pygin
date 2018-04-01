from game.scripts.constants import Constants
from game_engine.basic_objects.text import Text
from game_engine.game_object import GameObject
from game_engine.color import Color
from pygame.math import Vector2
from game_engine.material import Material
from game_engine.time import Time

class ScoreController(GameObject):

    def start(self):

        font_path = "game/assets/fonts/neuropolxrg.ttf"

        self.time_to_update_score = 0.095
        self.score_per_step = 1  # Number of steps of the game required to update the score
        self.last_update_time = Time.now()

        self.score = 0.0
        score_x = 10.0
        score_y = 5.0
        score_message = str(int(self.score))
        score_color = Color.white
        score_size = 15

        self.game_object_list = [
            Text(Vector2(score_x, score_y), score_message, Material(score_color), score_size, font_path)
        ]
        self.game_object_list[0].text_mesh.message = str(int(self.score))

    def update(self):
        if Time.now() - self.last_update_time >= self.time_to_update_score:
            self.score = self.score + self.score_per_step
            self.last_update_time = Time.now()
            Constants.current_score = self.score
            self.game_object_list[0].text_mesh.message = str(int(self.score))

