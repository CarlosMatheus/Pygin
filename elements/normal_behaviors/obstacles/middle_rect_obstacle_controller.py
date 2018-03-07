from pygame.math import Vector2
from game_engine.time import Time
from game_engine.engine import Engine
from game_engine.normal_behavior import NormalBehavior
from elements.normal_behaviors.game_objects.rectangle import Rectangle
from game_engine.game_object import GameObject
from game_engine.components.material import Material

class MiddleRectObstacleController(NormalBehavior):

    def start(self):
        self.fall_velocity = 350
        self.game_object_list = []

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Engine.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        obstacle_width = 0.3 * Engine.screen_width
        obstacle_height = 0.06 * Engine.screen_height
        rect = Rectangle(Vector2(0.5 * Engine.screen_width - 0.5 * obstacle_width, - obstacle_height),
                         Vector2(obstacle_width, obstacle_height),
                         Material((255, 255, 255)))
        self.game_object_list.append(rect)
        GameObject.instantiate(rect)
