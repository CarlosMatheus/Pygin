from game_engine.component import Component


class CircleMash(Component):

    def __init__(self, game_object, radius, material):
        super(CircleMash, self).__init__(game_object)
        self.radius = radius
        self.material = material
