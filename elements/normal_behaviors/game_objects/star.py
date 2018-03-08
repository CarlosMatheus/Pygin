from game_engine.components.polygon_mash import PolygonMash
from game_engine.game_object import GameObject
from pygame.math import Vector2
import math

class Star(GameObject):

    def __init__(self, center_position, size, material):
        """
        Add the polygon mash component
        Call the superclass constructor passing basic game_object parameters
        :param point_list:
        :param material:
        """
        self.center_position = center_position
        self.size = size
        self.material = material
        point_list = self.get_points()

        self.polygon_mash = PolygonMash(point_list, material)
        super(Star, self).__init__(Vector2(0, 0), 0, Vector2(1, 1), 2)

    def get_points(self):
        point_list = []
        angle = math.pi / 2 + math.pi

        for i in range(5):
            point_list.append(Vector2(self.center_position.x + self.size * math.cos(angle),
                                      self.center_position.y + self.size * math.sin(angle)))
            angle = angle + 36 * math.pi / 180

            point_list.append(Vector2(self.center_position.x + self.size/2 * math.cos(angle),
                                      self.center_position.y + self.size/2 * math.sin(angle)))
            angle = angle + 36 * math.pi / 180

        return point_list

    def fall(self, distance):
        self.center_position.y = self.center_position.y + distance

        point_list = self.get_points()

        self.polygon_mash = PolygonMash(point_list, self.material)
