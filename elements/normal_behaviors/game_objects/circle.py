from game_engine.components.circle_mash import CircleMash
from game_engine.game_object import GameObject


class Circle(GameObject):

    def __init__(self, position_x, position_y, radius, color):

        self.circle_mash = CircleMash(position_x, position_y, radius, color)
        super(Circle, self).__init__(position_x, position_y, 0, 1, 1)
