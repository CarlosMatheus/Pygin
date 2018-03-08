from game_engine.mash import Mash


class PolygonMash(Mash):

    def __init__(self, game_object, point_list, material):
        super(PolygonMash, self).__init__(game_object)
        self.point_list = point_list
        self.material = material
