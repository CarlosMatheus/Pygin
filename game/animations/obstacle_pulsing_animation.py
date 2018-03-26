from game_engine.components.animation import Animation
from game_engine.key_frame import KeyFrame
from game.scripts.constants import Constants
from pygame.math import Vector2


class ObstaclePulsingAnimation(Animation):

    def __init__(self, game_obj):
        key_frame_list = list()
        key_frame_list.append(
            KeyFrame(0.00, scale=Vector2(1.0, 1.0), interpolation="out_cubic"))
        key_frame_list.append(
            KeyFrame(0.25, scale=Vector2(1.1, 1.1), interpolation="out_cubic"))
        key_frame_list.append(
            KeyFrame(0.50, scale=Vector2(1.0, 1.0)))
        super().__init__(game_obj, key_frame_list, should_loop=True)
