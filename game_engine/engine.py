import pygame
from .draw import Draw
from game_engine.components.constants import Constants
from game_engine.scene import Scene


class Engine:

    screen_width = 360
    screen_height = 640
    game_display = 0

    @classmethod
    def start_game(cls, game_name, scenes):
        """
        Start the game with pygame
        :param game_name: name that will be displayed on the window
        :param scenes: list of scenes of the game
        """
        pygame.init()
        cls.game_display = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        pygame.display.set_caption(game_name)
        Scene.scenes_list = scenes
        Draw.set_game_display(Engine.game_display)
        Scene.start_first_scene()

    @classmethod
    def end_game(cls):
        """
        Quits the game
        """
        pygame.quit()
        quit()
