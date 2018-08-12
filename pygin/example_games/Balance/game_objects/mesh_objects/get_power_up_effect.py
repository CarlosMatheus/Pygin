from Balance.game_objects.mesh_objects.particle import Particle
from pygin.components.particle_system import ParticleSystem
from pygin.game_object import GameObject
from pygin.time import Time
from pygame.math import Vector2


class GetPowerUpEffect(GameObject):

    def __init__(self, position, material):
        """
        Add the polygon mesh component
        Call the superclass constructor passing basic game_object parameters
        """
        super().__init__(position, 0, Vector2(1, 1), 2)
        self.material = material

    def start(self):
        self.particle_system = ParticleSystem(self,
                                              Particle,
                                              quant=30,
                                              period=0.02,
                                              vel_min=40,
                                              vel_max=80,
                                              duration=2,
                                              gravity=98,
                                              layer=10
                                              )
        self.particle_system.set_circ_gen(self.transform.position,
                                          1, mode="radial",
                                          direct_met=self.direct_met,
                                          ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met
                                          )
        self.particle_system.play()
        self.spawn_time = Time.now()

    def update(self):
        if Time.now() - self.spawn_time > 0.03:
            self.destroy_me()

    def ini_angle_met(self):
        return 0

    def fin_angle_met(self):
        return 360

    def direct_met(self):
        return Vector2(0, -1)
