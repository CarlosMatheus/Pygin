from elements.game_objects.game_objects.basic_objects.basic_rectangle import BasicRectangle
from game_engine.components.box_collider import BoxCollider
from pygame.math import Vector2


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material):
        super(Rectangle, self).__init__(position, dimension, material, layer = 0)
        self.box_collider = BoxCollider(self)
