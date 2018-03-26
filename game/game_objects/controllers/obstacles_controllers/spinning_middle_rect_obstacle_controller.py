from pygame.math import Vector2
from game_engine.time import Time
from random import randint as rand
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.constants import Constants
from game.scripts.material import Material
from game.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation
from game_engine.components.animator import Animator


class SpinningMiddleRectObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 280
        self.angular_speed = 5
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
        obstacle.transform.rotate(self.angular_speed * Time.delta_time() * obstacle.direction)

    def generate_obstacle(self):
        self.obstacle_width = 0.45 * Constants.screen_width
        self.obstacle_height = 0.06 * Constants.screen_height
        rect = Rectangle(Vector2(0.5 * Constants.screen_width - 0.5 * self.obstacle_width, - self.obstacle_height),
                         Vector2(self.obstacle_width, self.obstacle_height),
                         Material((255, 255, 255)))
        direction = rand(0, 1) < 0.5
        if direction == 0:
            direction = -1
        rect.direction = direction
        rect.transform.rotate(0)
        rect.animation = ObstaclePulsingAnimation(rect)
        rect.animator = Animator(rect, [rect.animation])
        rect.animator.play()
        self.game_object_list.append(rect)
