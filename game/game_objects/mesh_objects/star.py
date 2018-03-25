from game_engine.components.polygon_mesh import PolygonMesh
from game_engine.components.circle_mesh import CircleMesh
from game_engine.components.circle_collider import CircleCollider
from game_engine.game_object import GameObject
from pygame.math import Vector2
from game_engine.geometry import Geometry
import math


class Star(GameObject):

    def __init__(self, center_position, size, material):
        """
        Add the polygon mesh component
        Call the superclass constructor passing basic game_object parameters
        """
        super(Star, self).__init__(center_position, 0, Vector2(1, 1), 2)
        self.circle_collider = CircleCollider(self)
        self.circle_mesh = CircleMesh(self, size, material)
        self.polygon_mesh = PolygonMesh(self, self.get_points(), material)

    def get_points(self):
        point_list = []
        angle = math.pi / 2 + math.pi
        for i in range(5):
            point_list.append(Vector2(self.transform.position.x + self.circle_collider.get_radius() * math.cos(angle),
                                      self.transform.position.y + self.circle_collider.get_radius() * math.sin(angle)))
            angle = angle + 36 * math.pi / 180
            point_list.append(Vector2(self.transform.position.x + self.circle_collider.get_radius()/2 * math.cos(angle),
                                      self.transform.position.y + self.circle_collider.get_radius()/2 * math.sin(angle)))
            angle = angle + 36 * math.pi / 180

        for i in range(5):
            point = point_list[i]
            point_list[i] = Geometry.rotate_point(Vector2(self.transform.position.x, self.transform.position.y),
                                                  point, self.transform.rotation)

        return point_list

    def fall(self, distance, angular_distance):
        self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + distance))
        self.transform.rotate(angular_distance)
        self.polygon_mesh.update_point_list(self.get_points())
