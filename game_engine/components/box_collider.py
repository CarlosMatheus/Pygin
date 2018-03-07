from game_engine.collider import Collider
from pygame.math import Vector2


class BoxCollider(Collider):

    def __init__(self, position, dimension):
        Collider.add_collider(self)
        self.left = position.x
        self.right = position.x + dimension.x
        self.up = position.y
        self.down = position.y + dimension.y
        self.vertexes = (Vector2(self.left, self.up), Vector2(self.left, self.down),
                         Vector2(self.right, self.down), Vector2(self.right, self.up))

    def is_point_inside(self, point):
        return point.x >= self.left and point.x <= self.right and point.y >= self.down and point.y <= self.up
