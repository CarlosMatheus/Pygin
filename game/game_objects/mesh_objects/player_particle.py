from game_engine.basic_objects.basic_particle_circ import BasicParticleCirc
from game.animations.particle_fade_animation import ParticleFadeAnimation
from game_engine.material import Material
from game_engine.components.animator import Animator


class PlayerParticle(BasicParticleCirc):

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
