from pygame.math import Vector2
from elements.game_objects.game_objects.star import Star
from game_engine.time import Time
from elements.game_objects.material import Material
from game_engine.game_object import GameObject
from game_engine.color import Color
from random import uniform as randfloat
from game_engine.components.constants import Constants

class StarScoreController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.game_object_list = []
        self.size = Constants.screen_width * 0.03

    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.fall(self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        random_pos = int(randfloat(self.size / 2 + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.size / 2 + Constants.circCenter_x - Constants.circRadius)))

        star = Star(Vector2(random_pos, -self.size), self.size,
                    Material(Color.yellow))
        self.game_object_list.append(star)
