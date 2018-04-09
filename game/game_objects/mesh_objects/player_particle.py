from game_engine.basic_objects.basic_particle_circ import BasicParticleCirc


class PlayerParticle(BasicParticleCirc):

    def __init__(self, position):
        super().__init__(position)

    def start(self):
        self.change = True

    def update(self):
        if self.change:
            self.change = False
            self.material = self.creator_obj.material
