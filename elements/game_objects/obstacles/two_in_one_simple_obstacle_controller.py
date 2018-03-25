from pygame.math import Vector2
from game_engine.time import Time
from random import randint as rand
from elements.game_objects.game_objects.rectangle import Rectangle
from game_engine.game_object import GameObject
from elements.game_objects.material import Material
from elements.game_objects.constants import Constants

class TwoInOneSimpleObstacleController(GameObject):

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
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x,
                                                          obstacle_pair[1].transform.position.y
                                                  + 4 * self.fall_velocity * Time.delta_time())
        else:
            obstacle_pair[1].transform.position = Vector2(obstacle_pair[1].transform.position.x,
                                                          obstacle_pair[1].transform.position.y
                                        + self.fall_velocity * Time.delta_time())

        obstacle_pair[0].transform.position = Vector2(obstacle_pair[0].transform.position.x,
                                                      obstacle_pair[0].transform.position.y
                                                      + self.fall_velocity * Time.delta_time())

        obstacle_pair[0].polygon_mesh.update_point_list(obstacle_pair[0].get_points())
        obstacle_pair[1].polygon_mesh.update_point_list(obstacle_pair[1].get_points())

    def generate_obstacle(self):
        direction = rand(0, 1) < 0.5
        obstacle_width = 0.5 * Constants.screen_width
        obstacle_height = 0.06 * Constants.screen_height

        rect1 = Rectangle(Vector2(direction * 0.5 * Constants.screen_width, - obstacle_height),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        rect2 = Rectangle(Vector2(rect1.transform.position.x, rect1.transform.position.y),
                          Vector2(obstacle_width, obstacle_height),
                          Material((255, 255, 255)))

        self.game_object_list.append([rect1, rect2])

