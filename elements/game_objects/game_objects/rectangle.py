from elements.game_objects.game_objects.basic_objects.basic_rectangle import BasicRectangle
from game_engine.components.box_collider import BoxCollider
from game_engine.components.polygon_mesh import PolygonMesh
from pygame.math import Vector2


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material):
        super(Rectangle, self).__init__(position, dimension, material, layer = 0)
        self.dimension = dimension
        self.box_collider = BoxCollider(self)
        self.polygon_mesh = PolygonMesh(self, self.get_points(), material)

    def get_points(self):
        point_list = []
        point_list.append(Vector2(self.transform.position.x, self.transform.position.y))
        point_list.append(Vector2(self.transform.position.x, self.transform.position.y + self.dimension.y))
        point_list.append(Vector2(self.transform.position.x + self.dimension.x, self.transform.position.y + self.dimension.y))
        point_list.append(Vector2(self.transform.position.x + self.dimension.x, self.transform.position.y))
        return point_list