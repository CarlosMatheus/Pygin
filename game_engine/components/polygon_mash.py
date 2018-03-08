from game_engine.component import Component


class PolygonMash(Component):

    def __init__(self, game_object, point_list, material):
        super(PolygonMash, self).__init__(game_object)
        self.point_list = point_list
        self.material = material
