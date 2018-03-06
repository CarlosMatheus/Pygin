from .normal_behavior import NormalBehavior
from .draw import Draw
from .components.transform import Transform
from .components.material import Material
from .engine import Engine


class GameObject(NormalBehavior):

    current_running_scene = 0

    def __init__(self, position_x, position_y, rotation, scale_x, scale_y, color):
        """
        set basics game_objects parameters
        :param position_x: game_object's x initial position
        :param position_y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale_x: game_object's x initial scale
        :param scale_y: game_object's y initial scale
        :param color: game_object's initial material color
        """
        self.transform = Transform(position_x, position_y, rotation, scale_x, scale_y)
        self.material = Material(color)

    def draw_game_object(self):
        """
        Draw the game_object on screen
        """
        Draw.rect(self.transform.translate[0], self.transform.translate[1], self.transform.scale[0],
                  self.transform.scale[1], self.material.color)

    @classmethod
    def instantiate(cls, game_object):
        Engine.current_running_scene.add_game_object(game_object)

    @classmethod
    def destroy(cls, game_object):
        Engine.current_running_scene.remove_game_object(game_object)
