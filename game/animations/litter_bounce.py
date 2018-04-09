from game_engine.components.animation import Animation
from game_engine.key_frame import KeyFrame
from pygame.math import Vector2
import random


class LitterBounce(Animation):

    def __init__(self, game_object):
        """
        :param game_object:
        """
        inter = "in_out_quint"
        gap =5
        key_frames = list()
        key_frames.append(KeyFrame(0.0, position=Vector2(0, 0), interpolation=inter))
        key_frames.append(KeyFrame(0.5, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(1, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(1.5, position=Vector2(self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(2, position=Vector2(-self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(2.5, position=Vector2(-self.rand()*gap, self.rand()*gap), interpolation=inter))
        key_frames.append(KeyFrame(3, position=Vector2(0, 0), interpolation=inter))
        super().__init__(game_object, key_frames)

    def rand(self):
        return random.randint(-2, 8)
