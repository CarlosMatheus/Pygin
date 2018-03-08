from game_engine.component import Component


class Material(Component):

    def __init__(self, game_object, color):
        """
        set initial parameters
        :param color: material color
        """
        super(Material, self).__init__(game_object)
        self.color = color
