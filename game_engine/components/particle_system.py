from game_engine.component import Component


class ParticleSystem(Component):

    def __init__(self, game_object):
        super(ParticleSystem, self).__init__(game_object)
