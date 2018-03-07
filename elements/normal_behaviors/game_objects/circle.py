from game_engine.components.circle_mash import CircleMash
from game_engine.game_object import GameObject
from pygame.math import Vector2


class Circle(GameObject):

    def __init__(self, position, radius, material):
        self.circle_mash = CircleMash(radius, material)
        super(Circle, self).__init__(position, 0, Vector2(1, 1))
