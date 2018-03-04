import pygame
from .draw import Draw


class Engine:

    screen_width = 360
    screen_height = 640
    game_display = 0
    scenes_list = []

    @classmethod
    def start_game(cls, game_name, scenes):
        """
        Start the game with pygame
        :param game_name: name that will be displayed on the window
        :param scenes: list of scenes of the game
        """
        pygame.init()
        cls.game_display = pygame.display.set_mode((cls.screen_width, cls.screen_height))
        pygame.display.set_caption(game_name)
        cls.scenes_list = scenes
        Draw.set_game_display(Engine.game_display)
        cls.start_first_scene()

    @classmethod
    def start_first_scene(cls):
        """
        Start the first scene
        """
        Engine.scenes_list[0].start()
        Engine.scenes_list[0].scene_loop()

    @classmethod
    def end_game(cls):
        """
        Quits the game
        """
        pygame.quit()
        quit()
