from game_engine.components.box_collider import BoxCollider
from game_engine.components.circle_collider import CircleCollider


class Collider():

    collider_list = []

    @classmethod
    def add_collider(cls, collider):
        cls.collider_list.append(collider)

    def on_collision(self):
        for collider in Collider.collider_list:
            if isinstance(collider, BoxCollider):
                return self.__box_collision()
            elif isinstance(collider, CircleCollider):
                return self.__circle_collision()

    # TODO: other kinds of collisions -- for this game you can only call this function inside a circle_collide

    def __box_collision(self, box):
        for vertex in box.vextexes:
            if self.is_vertex_inside(vertex):
                return True
        for point in self.main_points:
            if box.is_point_inside(point):
                return True
        return False

    def __circle_collision(self, circle):
        if circle == self:
            return False
        elif circle.center.distance_to(self.center) > circle.radius + self.radius:
            return False
        else:
            return True
