from pygin.basic_objects.basic_rectangle import BasicRectangle
from pygin.components.polygon_collider import PolygonCollider


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material, layer=0):
        super(Rectangle, self).__init__(position, dimension, material, layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)
