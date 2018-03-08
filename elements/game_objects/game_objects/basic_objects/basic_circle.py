from game_engine.components.circle_mash import CircleMash
from game_engine.game_object import GameObject
from game_engine.components.material import Material
from pygame.math import Vector2


class BasicCircle(GameObject):

    def __init__(self, position, radius, material, layer):
        """
        Add the circle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the circle
        :param position_y: initial position y of the circle
        :param radius: initial radius of the circle
        :param color: initial color of the circle
        """
        super(BasicCircle, self).__init__(position, 0, Vector2(1, 1), layer)
        self.material = Material(self, material.color)
        self.circle_mash = CircleMash(self, radius, self.material)

    def start(self):
        pass

    def update(self):
        pass
