from game_engine.collider import Collider
from pygame.math import Vector2


class BoxCollider(Collider):

    def __init__(self, game_object):
        """
        initiate collider
        :param rectangle_obj_ref: The reference to the object that contains the collider
        """
        super(BoxCollider, self).__init__(game_object)
        Collider.add_collider(self)

    def is_point_inside(self, point):
        """
        Verify if a point is inside of the rectangle
        :param point: the point to verify
        :return: True if it is inside
        """
        return point.x >= self.get_left_side() and point.x <= self.get_right_side() \
               and point.y <= self.get_down_side() and point.y >= self.get_up_side()

    def get_left_side(self):
        """
        :return: left side position x
        """
        return self.transform.position.x

    def get_right_side(self):
        """
        :return: right side position x
        """
        return self.transform.position.x + self.game_object.rectangle_mesh.dimension.x

    def get_up_side(self):
        """
        :return: up side position y
        """
        return self.transform.position.y

    def get_down_side(self):
        """
        :return: down side position y
        """
        return self.transform.position.y + self.game_object.rectangle_mesh.dimension.y

    def get_vertexes(self):
        """
        :return: The rectangle vertexes in an array
        """
        return [Vector2(self.get_left_side(), self.get_up_side()),
                Vector2(self.get_left_side(), self.get_down_side()),
                Vector2(self.get_right_side(), self.get_down_side()),
                Vector2(self.get_right_side(), self.get_up_side())
                ]

    def on_collision(self):
        """
        Check if the have occurred a collision between two colliders
        loop on the collider list to check if this collider have collided with other
        :return: True if collided
        TODO: other kinds of collisions -- for this game you can only call this function inside a circle_collide
        """
        raise Exception('--- This methods have not been implemented yet! Use circle_collider instead ---')

    def __box_collision(self, box):
        """
        Check a collision between this collider and a box_collider
        :param box: the box collider reference
        :return: True if collided
        TODO: other kinds of collisions -- for this game you can only call this function inside a circle_collide
        """
        raise Exception('--- This methods have not been implemented yet! Use circle_collider instead ---')

    def __circle_collision(self, circle):
        """
        Check a collision between this collider and a circle_collider
        :param circle: the circle collider reference
        :return: True if collided
        TODO: other kinds of collisions -- for this game you can only call this function inside a circle_collide
        """
        raise Exception('--- This methods have not been implemented yet! Use circle_collider instead ---')
