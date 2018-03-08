from game_engine.components.text_mash import TextMash
from game_engine.game_object import GameObject
from pygame.math import Vector2
import pygame


class Text(GameObject):

    def __init__(self, position, message, color, size, font):
        pygame.font.init()
        self.text_mash = TextMash(message, color, size, font)
        super(Text, self).__init__(position, 0, Vector2(1, 1))
