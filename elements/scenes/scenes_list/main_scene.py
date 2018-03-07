from game_engine.scene import Scene
from elements.normal_behaviors.player_controller import PlayerController
from elements.normal_behaviors.score_controller import ScoreController
from elements.normal_behaviors.obstacle_controller_wrapper import ObstacleControllerWrapper

class MainScene(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.init_normal_behaviors_list = [PlayerController(),
                                           ObstacleControllerWrapper(),
                                           ScoreController()
                                           ]
        super(MainScene, self).__init__(self.init_normal_behaviors_list)
