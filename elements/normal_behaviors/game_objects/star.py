from game_engine.components.polygon_mash import PolygonMash
from game_engine.game_object import GameObject
from pygame.math import Vector2


class Star(GameObject):

    def __init__(self, point_list, color):
        """
        Add the polygon mash component
        Call the superclass constructor passing basic game_object parameters
        :param point_list:
        :param color:
        """
        super(Star, self).__init__(Vector2(0, 0), 0, Vector2(1, 1))
        self.polygon_mash = PolygonMash(point_list, color)
