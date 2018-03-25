from game.scenes.main_scene import MainScene
from game.scenes.main_menu import MainMenu
from game.scenes.retry_scene import RetryScene


class ScenesControllerScript:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [MainMenu, MainScene, RetryScene]
