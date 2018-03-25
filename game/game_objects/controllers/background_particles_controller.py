from pygame.math import Vector2
from game_engine.time import Time
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.constants import Constants
from game_engine.color import Color
from game.scripts.material import Material
from random import randint as rand

class BackgroundParticlesController(GameObject):

    def start(self):
        self.fall_velocity = 60
        self.game_object_list = []
        self.generate_particles()

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                obstacle.transform.position = Vector2(rand(0, Constants.screen_width), 0)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())
        obstacle.polygon_mesh.update_point_list(obstacle.get_points())

    def generate_particles(self):
        for i in range(5):
            rect = Rectangle(Vector2(rand(0, Constants.screen_width), rand(0, Constants.screen_height)),
                             Vector2(0.007 * Constants.screen_width, 0.007 * Constants.screen_width),
                             Material(Color.silver), -3)
            rect.polygon_collider = []
            rect.collidable = False
            self.game_object_list.append(rect)

        for i in range(5):
            rect = Rectangle(Vector2(rand(0, Constants.screen_width), rand(0, Constants.screen_height)),
                             Vector2(0.007 * Constants.screen_width, 0.007 * Constants.screen_width),
                             Material(Color.gray), -3)
            rect.polygon_collider = []
            rect.collidable = False
            self.game_object_list.append(rect)