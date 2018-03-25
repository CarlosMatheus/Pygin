from pygame.math import Vector2
from game_engine.time import Time
from random import randint as rand
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.material import Material
from game.scripts.constants import Constants

class TwoSideBySideSimpleObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 300
        self.game_object_list = []

    def update(self):

        if len(self.game_object_list) > 0:

            for obstacle_pair in self.game_object_list:
                if obstacle_pair[0].transform.position.y > Constants.screen_height:
                    self.game_object_list.remove(obstacle_pair)
                    for obstacle in obstacle_pair:
                        obstacle.destroy(obstacle)
                        GameObject.destroy(obstacle)
                else:
                    self.fall(obstacle_pair)

    def fall(self, obstacle_pair):
        visible_condition = 0.1 * Constants.screen_height < obstacle_pair[1].transform.position.y < 0.45 * Constants.screen_height

        if visible_condition:
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x, obstacle_pair[1].transform.position.y
                                                  + 5.0 * self.fall_velocity * Time.delta_time())

        else:
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x, obstacle_pair[1].transform.position.y
                                        + self.fall_velocity * Time.delta_time())


        obstacle_pair[0].transform.position = Vector2(obstacle_pair[0].transform.position.x,
                                              obstacle_pair[0].transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):
        direction = rand(0, 1) < 0.5
        obstacle_width = 0.5 * Constants.screen_width
        obstacle_height = 0.06 * Constants.screen_height

        rect1 = Rectangle(Vector2(direction * 0.5 * Constants.screen_width, - obstacle_height),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        rect2_x = rect1.transform.position.x

        if rect2_x == 0:
            rect2_x = 0.5 * Constants.screen_width
        else:
            rect2_x = 0.0

        rect2 = Rectangle(Vector2(rect2_x, rect1.transform.position.y),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        self.game_object_list.append([rect1, rect2])
