from pygame.math import Vector2
from game_engine.time import Time
from game_engine.game_object import GameObject
from Balance.game_objects.mesh_objects.rectangle import Rectangle
from Balance.scripts.constants import Constants
from game_engine.color import Color
from game_engine.material import Material
from random import randint as rand

class BackgroundParticlesController(GameObject):

    def start(self):
        self.first_layer_velocity = 200
        self.second_layer_velocity = 100
        self.first_layer = []
        self.second_layer = []
        self.generate_particles()

    def update(self):

        for obstacle in self.first_layer:
            if obstacle.transform.position.y > Constants.screen_height:
                obstacle.transform.position = Vector2(rand(0, Constants.screen_width), 0)
            else:
                self.fall(obstacle, self.first_layer_velocity)

        for obstacle in self.second_layer:
            if obstacle.transform.position.y > Constants.screen_height:
                obstacle.transform.position = Vector2(rand(0, Constants.screen_width), 0)
            else:
                self.fall(obstacle, self.second_layer_velocity)

    def fall(self, obstacle, fall_velocity):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + fall_velocity * Time.delta_time())

    def generate_particles(self):
        for i in range(5):
            rect = Rectangle(Vector2(rand(0, Constants.screen_width), rand(0, Constants.screen_height)),
                             Vector2(0.007 * Constants.screen_width, 0.007 * Constants.screen_width),
                             Material(Color.silver), -3)
            rect.polygon_collider = []
            rect.collidable = False
            self.first_layer.append(rect)

        for i in range(5):
            rect = Rectangle(Vector2(rand(0, Constants.screen_width), rand(0, Constants.screen_height)),
                             Vector2(0.007 * Constants.screen_width, 0.007 * Constants.screen_width),
                             Material(Color.gray), -3)
            rect.polygon_collider = []
            rect.collidable = False
            self.second_layer.append(rect)