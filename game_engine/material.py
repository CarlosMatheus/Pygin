from game_engine.color import Color


class Material:

    def __init__(self, color=Color.white, alpha=None):
        """
        set initial parameters
        :param color: material color
        """
        self.color = color
        self.alpha = alpha
