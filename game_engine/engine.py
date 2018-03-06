import pygame
from .draw import Draw


class Engine:
    current_running_scene_index = 0
    current_running_scene = 0
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
        cls.current_running_scene = cls.scenes_list[0]
        cls.current_running_scene_index = 0
        cls.scenes_list[0].start()
        cls.scenes_list[0].scene_loop()

    @classmethod
    def change_scene(cls, scene_index):
        cls.current_running_scene.end_scene()
        cls.current_running_scene_index = scene_index
        cls.current_running_scene = cls.scenes_list[scene_index]

    @classmethod
    def start_next_scene(cls):
        cls.current_running_scene.start()
        cls.current_running_scene.scene_loop()

    @classmethod
    def end_game(cls):
        """
        Quits the game
        """
        pygame.quit()
        quit()

