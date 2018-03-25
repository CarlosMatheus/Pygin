from game_engine.mesh import Mesh


class TextMesh(Mesh):

    def __init__(self, game_object, message, color, size, font):
        super(TextMesh, self).__init__(game_object)
        self.message = message
        self.color = color
        self.size = size
        self.font = font
        self.label = font.render(self.message, 1, self.color)
