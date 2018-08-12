from Balance.game_objects.mesh_objects.particle import Particle
from pygin.components.particle_system import ParticleSystem
from pygin.components.physics import Physics
from pygin.game_object import GameObject
from pygin.time import Time
from pygame.math import Vector2


class DieEffect(GameObject):

    def __init__(self, position, material, radius, inst_vel):
        super().__init__(position, 0, Vector2(1, 1), 2)
        self.physics = Physics(self)
        self.inst_vel = inst_vel
        self.material = material
        self.radius = radius

    def start(self):
        """
        Will start a particle effect
        """
        self.physics.inst_velocity = self.inst_vel
        self.particle_system = ParticleSystem(self,
                                              Particle,
                                              quant=15,
                                              period=0.01,
                                              vel_min=30,
                                              vel_max=130,
                                              duration=0.9,
                                              gravity=130,
                                              layer=10,
                                              inherit_vel=True,
                                              inherit_vel_mult=0.5,
                                              unscaled=True,
                                              num_of_periods=1
                                              )
        self.particle_system.set_circ_gen(self.transform.position,
                                          radius=self.radius,
                                          mode="radial",
                                          direct_met=self.direct_met,
                                          ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met
                                          )
        self.particle_system.play()
        self.spawn_time = Time.now()

    def update(self):
        """
        Will be destroyed after a time
        """
        self.physics.inst_velocity = self.inst_vel
        if Time.now() - self.spawn_time > 0.01:
            self.destroy_me()

    def ini_angle_met(self):
        return 0

    def fin_angle_met(self):
        return 360

    def direct_met(self):
        return Vector2(0, -1)
