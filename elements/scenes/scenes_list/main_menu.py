from game_engine.scene import Scene
from elements.game_objects.main_menu_controller import MainMenuController


class MainMenu(Scene):

    def __init__(self):
        """
        Create the list of game_objects and call the superclass constructor passing the list
        """
        self.init_game_objects_list = [MainMenuController()]
        super(MainMenu, self).__init__(self.init_game_objects_list)
