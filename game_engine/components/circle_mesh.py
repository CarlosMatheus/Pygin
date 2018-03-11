from game_engine.mesh import Mesh


class CircleMesh(Mesh):

    def __init__(self, game_object, radius, material):
        super(CircleMesh, self).__init__(game_object)
        self.radius = radius
        self.material = material
