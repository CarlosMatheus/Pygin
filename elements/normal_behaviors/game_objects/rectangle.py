from game_engine.components.rectangle_mash import RectangleMash
from game_engine.game_object import GameObject
from game_engine.components.box_collider import BoxCollider
from pygame.math import Vector2


class Rectangle(GameObject):

    def __init__(self, position, dimension, material):

        self.rectangle_mash = RectangleMash(dimension, material)
        self.box_collider = BoxCollider(self)
        super(Rectangle, self).__init__(position, 0, Vector2(1, 1))
