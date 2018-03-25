from balance.scenes.scenes_list.main_scene import MainScene
from balance.scenes.scenes_list.main_menu import MainMenu
from balance.scenes.scenes_list.retry_scene import RetryScene


class ScenesController:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [MainMenu, MainScene, RetryScene]
