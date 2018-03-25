from game_engine.scene import Scene
from balance.game_objects.retry_controller import RetryController


class RetryScene(Scene):

    def __init__(self):
        """
        Create the list of game_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [RetryController]
        super(RetryScene, self).__init__(self.init_game_objects_controllers_reference_list)
