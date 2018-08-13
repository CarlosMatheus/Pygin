from ..scenes.main_scene import MainScene


class ScenesScript:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list with the references to the scenes classes
        """
        return [MainScene]
