from game_engine.components.rectangle_mash import RectangleMash
from game_engine.game_object import GameObject


class Rectangle(GameObject):

    def __init__(self, position_x, position_y, width, height, color):

        self.rectangle_mash = RectangleMash(position_x, position_y, width, height, color)
        super(Rectangle, self).__init__(position_x, position_y, 0, 1, 1)
