from game_engine.components.animation import Animation
from game_engine.key_frame import KeyFrame
from game.scripts.constants import Constants
from pygame.math import Vector2


class ObstaclePulsingAnimation(Animation):

    def __init__(self, game_obj):
        key_frame_list = list()
        key_frame_list.append(
            KeyFrame(0.0, scale=Vector2(1.0, 1.0), interpolation="out_cubic"))
        key_frame_list.append(
            KeyFrame(0.5, scale=Vector2(2.0, 2.0), interpolation="out_cubic"))
        key_frame_list.append(
            KeyFrame(1.0, scale=Vector2(1.0, 1.0)))
        super().__init__(game_obj, key_frame_list, should_loop=True)
