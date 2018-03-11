from game_engine.mesh import Mesh


class PolygonMesh(Mesh):

    def __init__(self, game_object, point_list, material):
        super(PolygonMesh, self).__init__(game_object)
        self.point_list = point_list
        self.material = material

    def update_point_list(self, point_list):
        self.point_list = point_list
