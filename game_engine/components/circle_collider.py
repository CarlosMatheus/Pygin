from game_engine.collider import Collider
from game_engine.components.box_collider import BoxCollider
from pygame.math import Vector2


class CircleCollider(Collider):

    def __init__(self, circle_obj_ref):
        """
        initiate collider
        :param circle_obj_ref: The reference to the object that contains the collider
        """
        Collider.add_collider(self)
        self.circle = circle_obj_ref

    def is_vertex_inside(self, point):
        """
        Verify if a point is inside of the circle
        :param point: the point to verify
        :return: True if it is inside
        """
        return point.distance_to(self.get_center()) <= self.get_radius()

    def get_center(self):
        """
        :return: Get the center point of the circle
        """
        return self.circle.transform.position

    def get_radius(self):
        """
        :return: Get the radius of the circle
        """
        return self.circle.circle_mash.radius

    def get_main_points(self):
        """
        The main points are the up, down, left and right extremities borders of the circle
        :return: An array that contains each of the four points
        """
        return [Vector2(self.circle.transform.position.x - self.get_radius(), self.get_center().y),
                Vector2(self.get_center().x, self.circle.transform.position.y + self.get_radius()),
                Vector2(self.circle.transform.position.x + self.get_radius(), self.get_center().y),
                Vector2(self.get_center().x, self.circle.transform.position.y - self.get_radius())]

    def on_collision(self):
        """
        Check if the have occurred a collision between two colliders
        loop on the collider list to check if this collider have collided with other
        :return: True if collided
        """
        for collider in Collider.collider_list:
            if isinstance(collider, BoxCollider):
                collided = self.__box_collision(collider)
            elif isinstance(collider, CircleCollider):
                collided = self.__circle_collision(collider)
            if collided:
                return True
        return False

    def __box_collision(self, box):
        """
        Check a collision between this collider and a box_collider
        :param box: the box collider reference
        :return: True if collided
        """
        for vertex in box.get_vertexes():
            if self.is_vertex_inside(vertex):
                return True
        for point in self.get_main_points():
            if box.is_point_inside(point):
                return True
        return False

    def __circle_collision(self, circle):
        """
        Check a collision between this collider and a circle_collider
        :param circle: the circle collider reference
        :return: True if collided
        """
        if circle == self:
            return False
        elif circle.get_center().distance_to(self.get_center()) > circle.get_radius() + self.get_radius():
            return False
        else:
            return True
