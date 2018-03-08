from pygame.math import Vector2
from game_engine.time import Time
from random import randint as rand
from game_engine.engine import Engine
from game_engine.game_object import GameObject
from elements.game_objects.game_objects.rectangle import Rectangle
from game_engine.components.material import Material

class TwoSideBySideSimpleObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 300
        self.game_object_list = []

    def update(self):

        if len(self.game_object_list) > 0:
            for index, obstacle in enumerate(self.game_object_list):
                if obstacle.transform.position.y > 2 * Engine.screen_height:
                    self.game_object_list.remove(obstacle)
                    obstacle.destroy(obstacle)
                    GameObject.destroy(obstacle)
                else:
                    self.fall(obstacle, index)

    def fall(self, obstacle, ind):
        visible_condition = 0.1*Engine.screen_height<obstacle.transform.position.y and obstacle.transform.position.y<0.35*Engine.screen_height and ind%2 == 1
        invisible_condition = 1.0*Engine.screen_height<obstacle.transform.position.y and ind%2 == 0

        if visible_condition:
            obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                                  + 4 * self.fall_velocity * Time.delta_time())
        elif invisible_condition and ind < len(self.game_object_list)-1:
            obstacle.transform.position.x = self.game_object_list[ind+1].transform.position.x
            obstacle.transform.position.y = self.game_object_list[ind+1].transform.position.y
        else:
            obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                        + self.fall_velocity * Time.delta_time())

    def trap_condition(self, obstacle):
        trap = True
        if obstacle.transform.position.y < 0.2 * Engine.screen_height or obstacle.transform.position.y > 0.6 * Engine.screen_height:
            trap = False

        return trap

    def generate_obstacle(self):
        direction = rand(0, 1) < 0.5
        obstacle_width = 0.5 * Engine.screen_width
        obstacle_height = 0.06 * Engine.screen_height

        rect1 = Rectangle(Vector2(direction * 0.5 * Engine.screen_width, - obstacle_height),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        rect2 = Rectangle(Vector2(rect1.transform.position.x, rect1.transform.position.y),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        if rect2.transform.position.x == 0:
            rect2.transform.position.x = 0.5 * Engine.screen_width
        else:
            rect2.transform.position.x = 0.0

        self.game_object_list.extend([rect1, rect2])
