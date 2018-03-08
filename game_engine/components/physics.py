from game_engine.component import Component


class Physics(Component):

    def __init__(self, game_object, mass, initial_velocity):
        super(Physics, self).__init__(game_object)
        self.mass = mass
        self.velocity = initial_velocity
