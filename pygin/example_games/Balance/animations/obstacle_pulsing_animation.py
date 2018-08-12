from pygin.components.animation import Animation
from pygin.key_frame import KeyFrame
from pygame.math import Vector2
import random


class ObstaclePulsingAnimation(Animation):

    def __init__(self, game_obj):
        key_frame_list = list()
        key_frame_list.append(KeyFrame(0.00,
                                       scale=Vector2(1.0, 1.0),
                                       interpolation="out_cubic"))
        key_frame_list.append(KeyFrame(0.35,
                                       scale=Vector2(1.07, 1.07),
                                       interpolation="out_cubic"))
        key_frame_list.append(KeyFrame(0.70, scale=Vector2(1.0, 1.0)))

        super().__init__(game_obj, key_frame_list, should_loop=True)

    def rand(self):
        return random.randint(-2, 8)
