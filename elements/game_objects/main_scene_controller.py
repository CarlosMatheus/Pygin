from game_engine.scene import Scene
from game_engine.game_object import GameObject
from game_engine.time import Time
from elements.game_objects.game_objects.screen_fader import ScreenFader
from elements.game_objects.player_controller import PlayerController
from elements.game_objects.score_controller import ScoreController
from elements.game_objects.obstacle_controller_wrapper import ObstacleControllerWrapper


class MainSceneController(GameObject):

    def start(self):
        """
        setup initial scene variables
        """
        self.setup_initializer()
        self.setup_fader()

    def setup_initializer(self):
        self.initial_time = Time.now()
        self.should_initialize = True

    def setup_fader(self):
        """
        Start fade in and set variables to fade out
        """
        ScreenFader(fade="in")
        self.should_timer = False
        self.should_change_scene = False
        self.can_press_button = True

    def update(self):
        """
        call the initialize scene
        """
        self.initialize_scene()

    def initialize_scene(self):
        """
        When is the correct time, initialize scene
        This will happen just once
        """
        if Time.now() - self.initial_time > 0.65 and self.should_initialize:
            self.should_initialize = False
            PlayerController()
            ObstacleControllerWrapper()
            ScoreController()
