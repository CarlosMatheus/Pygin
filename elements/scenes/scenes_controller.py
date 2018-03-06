from elements.scenes.scenes_list.main_scene import MainScene
from elements.scenes.scenes_list.main_menu import MainMenu


class ScenesController:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list
        """
        return [MainMenu(), MainScene()]
