from elements.normal_behaviors.test_rect_generator import TestRectGenerator
from game_engine.scene import Scene
from elements.normal_behaviors.player_controller import PlayerController
from elements.normal_behaviors.obstacles_controller import ObstaclesController
from elements.normal_behaviors.game_objects.rectangle import Rectangle
from elements.normal_behaviors.game_objects.circle import Circle


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.normal_behaviors_list = [PlayerController(), ObstaclesController()]
        super(MainScene, self).__init__(self.normal_behaviors_list)
