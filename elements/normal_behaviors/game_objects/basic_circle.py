from game_engine.components.circle_mash import CircleMash
from game_engine.game_object import GameObject


class Circle(GameObject):

    def __init__(self, position_x, position_y, radius, color):
        """
        Add the circle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the circle
        :param position_y: initial position y of the circle
        :param radius: initial radius of the circle
        :param color: initial color of the circle
        """
        self.circle_mash = CircleMash(position_x, position_y, radius, color)
        super(Circle, self).__init__(position_x, position_y, 0, 1, 1)
