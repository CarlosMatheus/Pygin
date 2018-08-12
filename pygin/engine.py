import pygame
from .draw import Draw
from pygin.scene import Scene
from pygin.time import Time
from pygin.input import Input


class Engine:

    screen_width = 240
    screen_height = 426
    game_name = "Untitled"
    game_display = None
    scenes = None

    @classmethod
    def start_game(cls, game_settings):
        """
        Start the Balance coroutine with pygame
        :param game_settings: settings of the Balance
        """
        cls.set_game_settings(game_settings)
        Time.start_coroutine(cls.game)
        Time.start_game()

    @classmethod
    def set_game_settings(cls, game_settings):
        """
        set up some Balance settings on engine
        :param game_settings: settings of the Balance
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
        Async method that will be the coroutine where the Balance will run in
        """
        pygame.mixer.pre_init(44100, -16, 1, 512)
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
        Quits the Balance
        """
        pygame.quit()
        quit()
