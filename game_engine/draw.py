import pygame
from pygame import gfxdraw
from .color import Color


class Draw:
    game_display = 0
    screen_width = 0
    screen_height = 0

    @classmethod
    def set_game_display(cls, screen, screen_width, screen_height):
        """
        set the screen reference
        :param screen: the pygame's screen object
        :param screen_width:
        :param screen_height:
        """
        cls.game_display = screen
        cls.screen_width = screen_width
        cls.screen_height = screen_height

    @classmethod
    def update_background(cls):
        """
        fill all screen with black at the begging of each frame
        """
        cls.game_display.fill(Color.black)

    @classmethod
    def circle(cls, position, radius, color, alpha=None):
        """
        Draw a circle
        :param position: circle's position
        :param radius: circle's radius
        :param color: circle's color
        """
        pygame.gfxdraw.filled_circle(cls.game_display, int(position.x), int(position.y), int(radius), color)

    @classmethod
    def polygon(cls, color, point_list, alpha=None):
        """
        Draw a polygon
        :param color:
        :param point_list:
        """
        if alpha is not None:
            s = pygame.Surface((cls.screen_width, cls.screen_height))
            s.set_alpha(alpha)
            pygame.draw.polygon(s, color, point_list)
            cls.game_display.blit(s, (0, 0))
        else:
            pygame.gfxdraw.filled_polygon(cls.game_display, point_list, color)

    @classmethod
    def text(cls, position_x, position_y, label, alpha=None):
        """
        Draws text
        :param position_x: text's x position
        :param position_y: text's y position
        :param label: its the pygame label necessary to draw the text
        """
        if alpha is not None:
            s = pygame.Surface((cls.screen_width, cls.screen_height))
            s.set_alpha(alpha)
            s.blit(label, (position_x, position_y))
            cls.game_display.blit(s, (0, 0))
        else:
            cls.game_display.blit(label, (position_x, position_y))
