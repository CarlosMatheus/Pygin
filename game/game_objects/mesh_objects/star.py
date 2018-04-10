from game_engine.components.polygon_mesh import PolygonMesh
from game_engine.components.circle_mesh import CircleMesh
from game_engine.components.circle_collider import CircleCollider
from game_engine.components.particle_system import ParticleSystem
from game.game_objects.mesh_objects.player_particle import PlayerParticle
from game.animations.power_up_fade_out import PowerUpFadeOut
from game_engine.components.animator import Animator
from game.animations.litter_bounce import LitterBounce
from game_engine.collider import Collider
from game_engine.game_object import GameObject
from game_engine.time import Time
from game_engine.geometry import Geometry
from pygame.math import Vector2
import math


class Star(GameObject):

    def __init__(self, center_position, radius, material):
        """
        Add the polygon mesh component
        Call the superclass constructor passing basic game_object parameters
        """
        super(Star, self).__init__(center_position, 0, Vector2(1, 1), 2)
        self.material = material
        self.circle_collider = CircleCollider(self)
        self.circle_mesh = CircleMesh(self, radius)
        self.polygon_mesh = PolygonMesh(self)
        self.should_die = False

    def _get_points(self):
        point_list = list()
        angle = math.pi / 2 + math.pi
        for i in range(5):
            point_list.append(Vector2(self.transform.position.x + self.circle_mesh.get_radius() * math.cos(angle),
                                      self.transform.position.y + self.circle_mesh.get_radius() * math.sin(angle)))
            angle = angle + 36 * math.pi / 180
            point_list.append(Vector2(self.transform.position.x + self.circle_mesh.get_radius()/2 * math.cos(angle),
                                      self.transform.position.y + self.circle_mesh.get_radius()/2 * math.sin(angle)))
            angle = angle + 36 * math.pi / 180

        for i in range(5):
            point = point_list[i]
            point_list[i] = Geometry.rotate_point(Vector2(self.transform.position.x, self.transform.position.y),
                                                  point, self.transform.rotation)
        return point_list

    def fall(self, distance, angular_distance):
        self.transform.translate(Vector2(self.transform.position.x, self.transform.position.y + distance))
        self.transform.rotate(angular_distance)

    def die(self):

        # TODO: change how collider works: dont use the collider list

        Collider.remove(self)
        self.circle_collider = None
        self.circle_collider = None
        self.animator.play_next_animation()
        self.should_die = True
        self.die_time=Time.now()

    def start(self):
        self.particle_system = ParticleSystem(self, PlayerParticle, quant=1, period=0.15, vel_min=30, vel_max=60,
                                              duration=0.8, gravity=98, inherit_vel=True)
        self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="radial",
                                          direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met)
        self.particle_system.play()
        self.animation = LitterBounce(self)
        self.animator = Animator(self, [self.animation, PowerUpFadeOut(self)])
        self.animator.play()

    def update(self):
        if self.should_die:
            if Time.now() - self.die_time > 0.4:
                self.destroy_me()

    def ini_angle_met(self):
        return 150

    def fin_angle_met(self):
        return 390

    def direct_met(self):
        return Vector2(0, -1)
