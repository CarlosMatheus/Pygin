from pygame.math import Vector2
from game.game_objects.mesh_objects.star import Star
from pygame import mixer
from game_engine.time import Time
from game.scripts.material import Material
from game_engine.game_object import GameObject
from game_engine.color import Color
from random import uniform as randfloat
from game.scripts.constants import Constants
from game.game_objects.mesh_objects.circle import Circle
from game_engine.basic_objects.basic_circle import BasicCircle


class InvenciblePowerUpController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.radius = Constants.screen_width * 0.03
        self.game_object_list = []
        self.frames_invencible = 100
        self.sound_collect = mixer.Sound('game/assets/soundtrack/star_collect.wav')


    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def get_power_up(self):
        self.sound_collect.play()
        print("Invencible!")

    def generate_obstacle(self):
        random_pos = int(randfloat(self.radius + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.radius + Constants.circCenter_x - Constants.circRadius)))

        circle = Circle(Vector2(random_pos, -2 * self.radius), self.radius,
                        Material(Color.blue))

        self.game_object_list.append(circle)
