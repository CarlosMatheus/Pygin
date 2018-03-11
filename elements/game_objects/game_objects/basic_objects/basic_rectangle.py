from game_engine.components.rectangle_mesh import RectangleMesh
from game_engine.components.material import Material
from game_engine.game_object import GameObject
from pygame.math import Vector2


class BasicRectangle(GameObject):

    def __init__(self, position, dimension, material, layer):
        """
        Add the rectangle mesh component
        Call the superclass constructor passing basic game_object parameters
        :param position.x: initial position x of the rectangle
        :param position.y: initial position y of the rectangle
        :param dimension.x: initial width of the rectangle
        :param dimension.y: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        super(BasicRectangle, self).__init__(position, 0, Vector2(1, 1), layer)
        self.material = Material(self, material.color)
        self.rectangle_mesh = RectangleMesh(self, dimension, self.material)
