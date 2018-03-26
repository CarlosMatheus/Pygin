from pygame.math import Vector2
from game_engine.time import Time
from random import randint
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.constants import Constants
from game.scripts.material import Material
from game.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation
from game_engine.components.animator import Animator
import math

class HalfMoonSpinningRectObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 300
        self.obstacle_width = 1.3 * Constants.screen_width
        self.obstacle_height = 0.06 * Constants.screen_height
        self.angular_speed = (self.fall_velocity/(1.2* Constants.screen_height+self.obstacle_height)) * \
                             0.9 * math.pi / 2
        self.game_object_list = []

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > 1.2 * Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())
        obstacle.transform.rotate(self.angular_speed * Time.delta_time() * obstacle.side)

    def generate_obstacle(self):
        side = randint(0, 1)

        rect = Rectangle(Vector2(-self.obstacle_width/2 + Constants.screen_width*side,
                                 - self.obstacle_height),
                         Vector2(self.obstacle_width, self.obstacle_height),
                         Material((255, 255, 255)))
        rect.animation = ObstaclePulsingAnimation(rect)
        rect.animator = Animator(rect, [rect.animation])
        rect.animator.play()

        if side == 1:
            rect.side = -1
        else:
            rect.side = 1

        self.game_object_list.append(rect)
