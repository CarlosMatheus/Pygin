from game_engine.collider import Collider
from pygame.math import Vector2


class CircleCollider(Collider):

    def __init__(self, position, radius):
        Collider.add_collider(self)
        Collider.add_circle_collider()
        self.center = position
        self.radius = radius
        left = position.x - radius
        right = position.x + radius
        up = position.y + radius
        down = position.y - radius
        self.main_points = (Vector2(left, self.center.y), Vector2(self.center.x, down),
                            Vector2(right, self.center.y), Vector2(self.center.x, up))

    def is_vertex_inside(self, point):
        return point.distance_to(self.center) <= self.radius
