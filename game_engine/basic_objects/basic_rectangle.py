from game_engine.components.polygon_mesh import PolygonMesh
from game_engine.components.material import Material
from game_engine.game_object import GameObject
from game_engine.geometry import Geometry
from pygame.math import Vector2


class BasicRectangle(GameObject):

    def __init__(self, position, dimension, material, layer):
        """
        Add the rectangle mesh component
        Call the superclass constructor passing basic game_object parameters
        :param position.x: initial position x of the rectangle
        :param position.y: initial position y of the rectangle
        :param dimension.x: initial width of the rectangle
        :param dimension.y: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        super(BasicRectangle, self).__init__(position, 0, Vector2(1, 1), layer)
        self.material = Material(self, material.color, material.alpha)
        self.dimension = dimension
        self.polygon_mesh = PolygonMesh(self, self.material)

    def _get_points(self):
        point_list = [Vector2(self.transform.position.x, self.transform.position.y),
                      Vector2(self.transform.position.x, self.transform.position.y + self.dimension.y),
                      Vector2(self.transform.position.x + self.dimension.x,
                              self.transform.position.y + self.dimension.y),
                      Vector2(self.transform.position.x + self.dimension.x, self.transform.position.y)]

        for i in range(len(point_list)):
            point = point_list[i]
            point_list[i] = Geometry.rotate_point(Vector2(self.transform.position.x + self.dimension.x/2, self.transform.position.y + self.dimension.y/2),
                                                  point, self.transform.rotation)
        return point_list
