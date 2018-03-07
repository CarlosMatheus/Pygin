from game_engine.scene import Scene
from elements.normal_behaviors.main_menu_controller import MainMenuController


class MainMenu(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.init_normal_behaviors_list = [MainMenuController()]
        super(MainMenu, self).__init__(self.init_normal_behaviors_list)
