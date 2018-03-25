from game_engine.collider import Collider
from game_engine.geometry import Geometry


class PolygonCollider(Collider):

    def __init__(self, game_object):
        """
        initiate collider
        :param game_object: The reference to the object that contains the collider
        """
        super(PolygonCollider, self).__init__(game_object)
        Collider.add_collider(self)

    def is_vertex_inside(self, point):
        """
        Verify if a point is inside of the polygon
        :param point: the point to verify
        :return: True if it is inside
        """
        return Geometry.polygon_point_intersection(self.get_point_list(), point)

    def get_point_list(self):
        """
        :return: Get the point list of a polygon
        """
        return self.game_object.polygon_mesh.get_points()

    def on_collision(self):
        """
        Check if the have occurred a collision between two colliders

        print("testing ", p1, "-", p2, " with point ", point)    loop on the collider list to check if this collider have collided with other
        :return: True if collided
        """

    def __circle_collision(self, circle):
        """
        Check a collision between this collider and a circle_collider
        :param circle: the circle collider reference
        :return: True if collided
        """
        raise Exception('--- This methods have not been implemented yet! Use circle_collider instead ---')

    def __polygon_collision(self, polygon):
        """
        Check a collision between this collider and a polygon_collider
        :param circle: the circle collider reference
        :return: True if collided
        """
        raise Exception('--- This methods have not been implemented yet! Use circle_collider instead ---')