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
        point_list = []
        angle = math.pi/2 + math.pi

        for i in range(5):
            point_list.append(Vector2(center_position.x + size*math.cos(angle),
                                      center_position.y + size*math.sin(angle)))
            angle = angle + 144*math.pi/180

        print(point_list)

        self.polygon_mash = PolygonMash(point_list, material)
        super(Star, self).__init__(Vector2(0, 0), 0, Vector2(1, 1))
