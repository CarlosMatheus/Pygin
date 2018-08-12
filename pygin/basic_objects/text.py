from pygin.components.text_mesh import TextMesh
from pygin.game_object import GameObject
from pygame.math import Vector2
import pygame


class Text(GameObject):

    def __init__(self, position, message, material, size, font_path, layer=10):
        super(Text, self).__init__(position, 0, Vector2(1, 1), layer=layer)
        self.material = material
        font = pygame.font.Font(font_path, size)
        self.text_mesh = TextMesh(self, message, size, font)
