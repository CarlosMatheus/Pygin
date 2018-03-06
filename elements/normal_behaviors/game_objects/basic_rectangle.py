from game_engine.components.rectangle_mash import RectangleMash
from game_engine.game_object import GameObject


class Rectangle(GameObject):

    def __init__(self, position_x, position_y, width, height, color):
        """
        Add the rectangle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the rectangle
        :param position_y: initial position y of the rectangle
        :param width: initial width of the rectangle
        :param height: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        self.rectangle_mash = RectangleMash(position_x, position_y, width, height, color)
        super(Rectangle, self).__init__(position_x, position_y, 0, 1, 1)
