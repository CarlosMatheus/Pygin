import pygame
from .draw import Draw
from game_engine.components.constants import Constants
from game_engine.scene import Scene
from game_engine.time import Time

class Engine:

    screen_width = 360
    screen_height = 640
    game_display = 0

    @classmethod
    def start_game(cls, game_name, scenes):
        """
        Start the game coroutine with pygame
        :param game_name: name that will be displayed on the window
        :param scenes: list of scenes of the game
        """
        cls.game_name = game_name
        cls.scenes = scenes
        Time.start_coroutine(cls.game)
        Time.start_game()

    @classmethod
    async def game(cls):
        """
        Async method that will be the coroutine where the game will run in
        """
        pygame.init()
        cls.game_display = pygame.display.set_mode((Constants.screen_width, Constants.screen_height))
        pygame.display.set_caption(cls.game_name)
        Scene.scenes_list = cls.scenes
        Draw.set_game_display(Engine.game_display)
        Scene.start_first_scene()

    @classmethod
    def end_game(cls):
        """
        Quits the game
        """
        pygame.quit()
        quit()
