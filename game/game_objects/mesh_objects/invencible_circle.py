from game_engine.basic_objects.basic_circle import BasicCircle
from game_engine.components.circle_collider import CircleCollider
from game_engine.components.particle_system import ParticleSystem
from game.game_objects.mesh_objects.player_particle import PlayerParticle
from game.animations.power_up_fade_out import PowerUpFadeOut
from game_engine.components.animator import Animator
from game.animations.litter_bounce import LitterBounce
from game_engine.collider import Collider
from game_engine.time import Time
from pygame.math import Vector2


class InvencibleCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(InvencibleCircle, self).__init__(position, radius, material, layer=-2)
        self.circle_collider = CircleCollider(self)
        self.should_die = False

    # Todo: create a power_up class that is superclass of invencible circle and star

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

    def die(self):

        # TODO: change how collider works: dont use the collider list

        Collider.remove(self)
        self.circle_collider = None
        self.animator.play_next_animation()
        self.should_die = True
        self.die_time=Time.now()

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
