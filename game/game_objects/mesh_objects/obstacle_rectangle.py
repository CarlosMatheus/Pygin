from game_engine.basic_objects.basic_rectangle import BasicRectangle
from game_engine.components.polygon_collider import PolygonCollider
from game_engine.components.particle_system import ParticleSystem
from game.game_objects.mesh_objects.player_particle import PlayerParticle


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material, layer=0):
        super(Rectangle, self).__init__(position, dimension, material, layer=layer)
        self.dimension = dimension
        self.polygon_collider = PolygonCollider(self)
        self.particle_system = ParticleSystem(self, PlayerParticle,
                                              quant=0.01, quant_proport_to_len=True,
                                              period=0.03,
                                              vel_min=0, vel_max=100, duration=0.5,
                                              spawn_prob="parab", vel_prob="parab",
                                              inherit_vel=True, inherit_vel_mult=1)
        self.particle_system.set_line_gen(self.fin_point_met, self.ini_point_met)
        self.particle_system.play()

    def ini_point_met(self):
        return self.polygon_mesh.get_points()[0]

    def fin_point_met(self):
        return self.polygon_mesh.get_points()[3]


    # Todo: make line directional on particle system:
    # def direct_met(self):
    #     return Vector2(0, -1)
