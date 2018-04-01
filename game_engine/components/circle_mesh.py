from game_engine.mesh import Mesh


class CircleMesh(Mesh):

    def __init__(self, game_object, radius):
        super(CircleMesh, self).__init__(game_object)
        self.__radius = radius

    def get_radius(self):
        return self.__radius * max(self.transform.scale.x, self.transform.scale.y)
    
    def get_unscaled_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius
