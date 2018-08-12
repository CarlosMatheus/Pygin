from pygin.basic_objects.basic_particle_circ import BasicParticleCirc
from Balance.animations.particle_fade_animation import ParticleFadeAnimation
from pygin.material import Material
from pygin.components.animator import Animator
from pygin.time import Time


class Particle(BasicParticleCirc):

    def __init__(self, position):
        self.change = True
        super().__init__(position)

    def start(self):
        self.animation = ParticleFadeAnimation(self, self.creator_obj.particle_system.duration)
        self.animator = Animator(self, [self.animation])
        self.animator.play()

    def update(self):
        if self.change:
            self.change = False
            self.material = Material(self.creator_obj.material.color)
        if Time.now() - self.creation_time > self.destroy_time:
            self.destroy_me()
