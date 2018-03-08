from game_engine.scene import Scene
from elements.game_objects.player_controller import PlayerController
from elements.game_objects.score_controller import ScoreController
from elements.game_objects.obstacle_controller_wrapper import ObstacleControllerWrapper


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of game_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [PlayerController,
                                                             ObstacleControllerWrapper,
                                                             ScoreController
                                                             ]
        super(MainScene, self).__init__(self.init_game_objects_controllers_reference_list)
