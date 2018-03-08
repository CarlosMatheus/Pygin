from game_engine.components.circle_mash import CircleMash
from game_engine.game_object import GameObject
from pygame.math import Vector2


class BasicCircle(GameObject):

    def __init__(self, position, radius, material):
        """
        Add the circle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the circle
        :param position_y: initial position y of the circle
        :param radius: initial radius of the circle
        :param color: initial color of the circle
        """
        self.circle_mash = CircleMash(radius, material)
        super(BasicCircle, self).__init__(position, 0, Vector2(1, 1))

    def start(self):
        pass

    def update(self):
        pass
