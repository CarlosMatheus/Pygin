from game_engine.basic_objects.basic_circle import BasicCircle
from game_engine.components.circle_collider import CircleCollider


class InvencibleCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(InvencibleCircle, self).__init__(position, radius, material, layer=-2)
        self.circle_collider = CircleCollider(self)
