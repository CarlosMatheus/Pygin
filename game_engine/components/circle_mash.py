from game_engine.mash import Mash


class CircleMash(Mash):

    def __init__(self, game_object, radius, material):
        super(CircleMash, self).__init__(game_object)
        self.radius = radius
        self.material = material
