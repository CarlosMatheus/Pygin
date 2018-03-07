from game_engine.scene import Scene
from elements.normal_behaviors.player_controller import PlayerController
from elements.normal_behaviors.test_rect_generator import TestRectGenerator


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.normal_behaviors_list = [PlayerController(), TestRectGenerator()]

        super(MainScene, self).__init__(self.normal_behaviors_list)
