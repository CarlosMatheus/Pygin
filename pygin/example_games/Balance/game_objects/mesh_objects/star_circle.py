from pygin.basic_objects.basic_circle import BasicCircle
from pygin.components.circle_collider import CircleCollider


class StarCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(StarCircle, self).__init__(position, radius, material, layer = -1)
        self.circle_collider = CircleCollider(self)

    def start(self):
        pass

    def update(self):
        pass
