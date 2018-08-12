from game_engine.scene import Scene
from Balance.game_objects.controllers.main_menu_controller import MainMenuController


class MainMenu(Scene):

    def __init__(self):
        """
        Create the list of mesh_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_controllers_reference_list = [MainMenuController]
        super(MainMenu, self).__init__(self.init_game_objects_controllers_reference_list)
