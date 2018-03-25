import pygame
from .draw import Draw
from game_engine.scene import Scene
from game_engine.time import Time
from game_engine.input import Input


class Engine:

    screen_width = 240
    screen_height = 426
    game_name = "Untitled"
    game_display = None
    scenes = None

    @classmethod
    def start_game(cls, game_settings):
        """
        Start the game coroutine with pygame
        :param game_settings: settings of the game
        """
        cls.set_game_settings(game_settings)
        Time.start_coroutine(cls.game)
        Time.start_game()

    @classmethod
    def set_game_settings(cls, game_settings):
        """
        set up some game settings on engine
        :param game_settings: settings of the game
        """
        if hasattr(game_settings, "scenes_list"):
            cls.scenes = game_settings.scenes_list
        else:
            raise Exception("No scenes_list in game_settings file!")
        if hasattr(game_settings, "game_name"):
            cls.game_name = game_settings.game_name
        if hasattr(game_settings, "screen_width"):
            cls.screen_width = game_settings.screen_width
        if hasattr(game_settings, "screen_height"):
            cls.screen_height = game_settings.screen_height

    @classmethod
    async def game(cls):
        """
        Async method that will be the coroutine where the game will run in
        """
        pygame.init()
        cls.game_display = pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption(cls.game_name)
        Scene.scenes_list = cls.scenes
        Draw.set_game_display(cls.game_display, cls.screen_width, cls.screen_height)
        Input.set_engine_reference(cls)
        Scene.start_first_scene()

    @classmethod
    def end_game(cls):
        """
        Quits the game
        """
        pygame.quit()
        quit()
