from game_engine.component import Component


class RectangleMash(Component):

    def __init__(self, game_object, dimension, material):
        super(RectangleMash, self).__init__(game_object)
        self.dimension = dimension
        self.material = material
