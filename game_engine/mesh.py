from game_engine.component import Component


class Mesh(Component):

    def __init__(self, game_object):
        super(Mesh, self).__init__(game_object)
        self.check_material()

    def check_material(self):
        """
        check whether the game_object material was defined before create the mesh
        """
        if self.game_object.material is None:
            raise Exception("GameObject {0} must have a material defined in order to have a Mesh"
                            .format(type(self.game_object).name))

    def get_material(self):
        """
        get the material of this mesh
        :return: the game_object material
        """
        return self.game_object.material
