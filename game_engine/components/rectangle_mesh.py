from game_engine.mesh import Mesh


class RectangleMesh(Mesh):

    def __init__(self, game_object, dimension, material):
        super(RectangleMesh, self).__init__(game_object)
        self.dimension = dimension
        self.material = material
