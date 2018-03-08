import pygame
from .collider import Collider
from pygame.math import Vector2
from .time import Time
from .input import Input
from .draw import Draw


class Scene:

    current_running_scene_index = 0
    current_running_scene = 0
    scenes_list = []

    def __init__(self, init_game_objects_controllers_reference_list):
        """
        Set object's variables to start a new scene
        :param init_game_objects_controllers_reference_list: list of all game_objects of the scene
        """
        init_game_objects_list = []
        self.init_game_objects_list = init_game_objects_list
        self.game_objects = []
        self.frame_events = []
        if Scene.current_running_scene == 0:
            Scene.current_running_scene = self
        for reference in init_game_objects_controllers_reference_list:
            init_game_objects_list.append(reference(Vector2(0, 0), 0, Vector2(0, 0)))
        self.should_end_scene = False

    def start(self):
        """
        Run methods to set the scene up
        """
        self.should_end_scene = False
        self.game_objects = self.init_game_objects_list
        self.run_events()
        Draw.update_background()
        self.run_all_starts()
        pygame.display.flip()
        Time.end_of_start()

    def run_all_starts(self):
        """
        Run the start method of each game_object
        """
        for game_object in self.game_objects:
            game_object.start()

    def run_all_updates(self):
        """
        Runs the update of each game_object of the scene
        """
        for game_object in self.game_objects:
            game_object.update()

    def draw_all_game_objects(self):
        """
        Run draw method of each game_object of the scene
        """
        for game_object in self.game_objects:
            game_object.draw_game_object()

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
        Add a new game object to the scene's game_objects list
        :param game_object: new game_object to add to scene
        """
        self.game_objects.append(game_object)
        game_object.start()

    def remove_game_object(self, game_object):
        """
        Remove a game_object if it is on game_object list
        :param game_object: the game_object to be removed
        """
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
            Collider.remove(game_object)

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
        """
        for event in self.frame_events:
            print(event)

    def debug_fps(self):
        """
        DEBUG print the game fps each frame
        """
        print(Time.clock.get_fps())

    def debug_objs(self):
        """
        DEBUG print the number of game_object each frame
        """
        print(len(self.game_objects))

    def end_scene(self):
        """
        Set the variable to stop scene loop
        """
        self.should_end_scene = True

    def exit_scene(self):
        """
        empty the game_objects and the collider list and start next scene
        """
        self.game_objects = []
        Collider.collider_list = []
        Scene.start_next_scene()

    @classmethod
    def start_first_scene(cls):
        """
        Start the first scene
        """
        cls.current_running_scene = cls.scenes_list[0]()
        cls.current_running_scene_index = 0
        cls.current_running_scene.start()
        cls.current_running_scene.scene_loop()

    @classmethod
    def change_scene(cls, scene_index):
        """
        End the current scene to start the next scene
        :param scene_index: the index on scene_list of the next scene
        """
        cls.current_running_scene.end_scene()
        cls.current_running_scene_index = scene_index
        cls.current_running_scene = cls.scenes_list[scene_index]()

    @classmethod
    def start_next_scene(cls):
        """
        Start next scene
        """
        cls.current_running_scene.start()
        cls.current_running_scene.scene_loop()
