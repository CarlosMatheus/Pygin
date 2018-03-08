from game_engine.components.rectangle_mash import RectangleMash
from game_engine.game_object import GameObject
from pygame.math import Vector2


class BasicRectangle(GameObject):

    def __init__(self, position, dimension, material):
        """
        Add the rectangle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the rectangle
        :param position_y: initial position y of the rectangle
        :param width: initial width of the rectangle
        :param height: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        self.rectangle_mash = RectangleMash(dimension, material)
        super(BasicRectangle, self).__init__(position, 0, Vector2(1, 1))
