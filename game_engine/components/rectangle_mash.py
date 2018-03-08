from game_engine.mash import Mash


class RectangleMash(Mash):

    def __init__(self, game_object, dimension, material):
        super(RectangleMash, self).__init__(game_object)
        self.dimension = dimension
        self.material = material
