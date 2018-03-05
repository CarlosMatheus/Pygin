from elements.scenes.scenes_list.main_scene import MainScene


class ScenesController:

    @classmethod
    def get_scenes(cls):
        """
        :return: the scene list
        """
        return [MainScene()]
