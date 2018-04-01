import random

class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    yellow = (247, 251, 0)
    blue = (36, 127, 244)
    green = (86, 244, 85)
    silver = (192, 192, 192)
    gray = (112, 112, 112)
    orange = (253, 102, 0)

    @classmethod
    def random_color(cls):
        """
        :return: a random color
        """
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
