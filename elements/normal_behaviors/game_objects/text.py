from game_engine.components.text_mash import TextMash
from game_engine.game_object import GameObject
import pygame


class Text(GameObject):

    def __init__(self, position_x, position_y, message, color, size, font):
        pygame.font.init()
        self.text_mash = TextMash(position_x, position_y, message, color, size, font)
        super(Text, self).__init__(position_x, position_y, 0, 1, 1)
