from game_engine.scene import Scene
from Balance.game_objects.controllers.main_scene_controller import MainSceneController


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [MainSceneController]
        super(MainScene, self).__init__(self.init_game_objects_controllers_reference_list)
