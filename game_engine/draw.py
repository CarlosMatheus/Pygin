import pygame
from .color import Color


class Draw:
    game_display = 0

    @classmethod
    def set_game_display(cls, screen):
        """
        set the screen reference
        :param screen: the pygame's screen object
        """
        cls.game_display = screen

    @classmethod
    def update_background(cls):
        """
        fill all screen with black at the begging of each frame
        """
        cls.game_display.fill(Color.black)

    @classmethod
    def rect(cls, position_x, position_y, scale_x, scale_y, color):
        """
        Draw a rectangle
        :param position_x: rect's x position
        :param position_y: rect's y position
        :param scale_x: rect's x scale
        :param scale_y: rect's y scale
        :param color: rect's color
        """
        pygame.draw.rect(cls.game_display, color, [position_x, position_y, scale_x, scale_y])

    @classmethod
    def circle(cls, position_x, position_y, radius, color):
        """
        Draw a circle
        :param position_x: circle's x position
        :param position_y: circle's y position
        :param radius: circle's radius
        :param color: circle's color
        """
        pygame.draw.circle(cls.game_display, color, [position_x, position_y], radius)

    @classmethod
    def text(cls, position_x, position_y, message, color, size, font_path):
        """
        Draws text
        :param position_x: text's x position
        :param position_y: text's y position
        :param message: the text's content. The message attached to it
        :param color: text's color
        :param size: text's size
        :param font_path: the path for a .ttf file representing the desired font. Can be none
        :return:
        """
        font = pygame.font.Font(font_path, size)
        # render text
        label = font.render(message, 1, color)
        cls.game_display.blit(label, (position_x, position_y))