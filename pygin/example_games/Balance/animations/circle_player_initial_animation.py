from pygin.components.animation import Animation
from pygin.key_frame import KeyFrame
from Balance.scripts.constants import Constants
from pygame.math import Vector2


class CirclePlayerInitialAnimation(Animation):

    def __init__(self, game_obj):
        dist = abs(Constants.circCenter_y-(Constants.screen_height+15))*0.1
        key_frame_list = list()
        key_frame_list.append(
            KeyFrame(0.0, position=Vector2(game_obj.transform.position.x, Constants.screen_height+15), interpolation="out_cubic"))
        key_frame_list.append(
            KeyFrame(0.5, position=Vector2(game_obj.transform.position.x, Constants.circCenter_y-(dist)), interpolation="in_out_quint"))
        key_frame_list.append(
            KeyFrame(0.7, position=Vector2(game_obj.transform.position.x, Constants.circCenter_y)))
        super().__init__(game_obj, key_frame_list, should_loop=False)
