import pygame
from .game_object import GameObject
from .engine import Engine
from .time import Time
from .input import Input
from .draw import Draw


class Scene:

    def __init__(self, _normal_behaviors):
        """
        Set object's variables to start a new scene
        :param _normal_behaviors: list of all _normal_behaviors of the scene
        """
        self.normal_behaviors = _normal_behaviors
        self.frame_events = []
        self.should_end_scene = False

    def start(self):
        """
        Run methods to set the scene up
        """
        self.run_events()
        Draw.update_background()
        self.run_all_starts()
        pygame.display.flip()
        Time.end_of_start()

    def run_all_starts(self):
        """
        Run the start method of each normal_behavior
        """
        for normal_behavior in self.normal_behaviors:
            normal_behavior.start()

    def run_all_updates(self):
        """
        Runs the update of each normal_behavior of the scene
        """
        for normal_behavior in self.normal_behaviors:
            normal_behavior.update()

    def draw_all_game_objects(self):
        """
        Run draw method of each game_object of the scene
        """
        for normal_behavior in self.normal_behaviors:
            if isinstance(normal_behavior, GameObject):
                normal_behavior.draw_game_object()

    def scene_loop(self):
        """
        Defines the main loop of the scene
        The scene occurs while in the loop
        """
        while not self.should_end_scene:
            self.run_events()
            Draw.update_background()
            self.run_all_updates()
            self.draw_all_game_objects()
            pygame.display.flip()
            Time.end_of_loop()
        self.exit_scene()

    def add_game_object(self, game_object):
        """
        Add a new game object to the scene's normal_behaviors list
        :param game_object: new game_object to add to scene
        """
        self.normal_behaviors.append(game_object)
        game_object.start()

    def remove_game_object(self, game_object):
        if game_object in self.normal_behaviors:
            self.normal_behaviors.remove(game_object)

    def run_events(self):
        """
        get the events in pygame queue
        and run the methods related to them
        """
        self.frame_events = pygame.event.get()
        Input.update_input(self.frame_events)

    def debug_event(self):
        """
        DEBUG print all the events of each frame
        :return:
        """
        for event in self.frame_events:
            print(event)

    def end_scene(self):
        self.should_end_scene = True

    def exit_scene(self):
        self.normal_behaviors = []
        Engine.start_next_scene()
