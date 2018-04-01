from game_engine.mesh import Mesh
from pygame.math import Vector2


class PolygonMesh(Mesh):

    def __init__(self, game_object):
        super(PolygonMesh, self).__init__(game_object)
        self.__point_list = None
        self.__set_points_up()
        self.__geometric_center = None
        self.__update_geometric_center()
        self.__scaled_point_list = None
        self.__update_scaled_point_list()

    def get_points(self):
        """
        Get the list of points that defines the polygon
        :return: the points list (it is a list of Vector2)
        """
        return self.__scaled_point_list

    def get_unscaled_points(self):
        """
        Get the unscaled points list
        :return: the unscaled point_list
        """
        return self.__point_list

    def __set_points_up(self):
        """
        Set the point list with the game_object's _point_list parameter
        If it is not defined it will rise an exception,
        because it is a requisite to the polygon mesh to have defined the _get_points
        """
        if self.game_object._get_points() is not None:
            self.__point_list = self.game_object._get_points()
        else:
            raise Exception("GameObject {0} has a polygon_mesh, but has not a _get_points method!"
                            .format(type(self.game_object).__name__))

    def __start(self):
        """
        Start the mesh parameters
        """
        self.__point_list = self.game_object._get_points()
        self.__update_geometric_center()
        self.__update_scaled_point_list()

    def __update(self):
        """
        Update the mesh parameters
        """
        self.__point_list = self.game_object._get_points()
        self.__update_geometric_center()
        self.__update_scaled_point_list()

    def __update_geometric_center(self):
        """
        Update the geometric center based on new pointers position
        """
        self.__geometric_center = Vector2(0, 0)
        for point in self.__point_list:
            self.__geometric_center += point
        self.__geometric_center /= len(self.__point_list)

    def __update_scaled_point_list(self):
        """
        Update the scaled points list with the new position and new scale
        """
        self.__scaled_point_list = list()
        for point in self.__point_list:
            point_x = ((point.x - self.__geometric_center.x) * self.transform.scale.x) + self.__geometric_center.x
            point_y = ((point.y - self.__geometric_center.y) * self.transform.scale.y) + self.__geometric_center.y
            self.__scaled_point_list.append(Vector2(point_x, point_y))
