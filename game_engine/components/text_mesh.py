from game_engine.mesh import Mesh


class TextMesh(Mesh):

    def __init__(self, game_object, message, material, size, font):
        super(TextMesh, self).__init__(game_object)
        self.message = message
        self.material = material
        self.size = size
        self.font = font
        self.label = self.font.render(self.message, 1, self.material.color)


    def __update(self):
        """
        update label with new message or color
        """
        self.label = self.font.render(self.message, 1, self.material.color)