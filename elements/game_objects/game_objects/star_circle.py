from elements.game_objects.game_objects.basic_objects.basic_circle import BasicCircle
from game_engine.components.circle_collider import CircleCollider


class StarCircle(BasicCircle):

    def __init__(self, position, radius, material):
        self.circle_collider = CircleCollider(self)
        layer = -1
        super(StarCircle, self).__init__(position, radius, material, layer)

    def start(self):
        pass

    def update(self):
        pass
