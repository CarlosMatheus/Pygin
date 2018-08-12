from pygin.basic_objects.basic_circle import BasicCircle
from pygin.time import Time


class BasicParticleCirc(BasicCircle):

    def __init__(self, position, destroy_time=1.0):
        self.destroy_time = destroy_time
        self.creation_time = Time.now()
        self.creator_obj = None
        super().__init__(position=position, radius=1)

    def set_creator_object(self, creator_obj):
        """
        Set to this particle the game_object that has the particle system that create this particle
        :param creator_obj: the game_object reference
        """
        self.creator_obj = creator_obj

    def start(self):
        pass

    def update(self):
        if Time.now() - self.creation_time > self.destroy_time:
            self.destroy_me()
