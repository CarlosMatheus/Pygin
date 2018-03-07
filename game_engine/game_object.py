from .normal_behavior import NormalBehavior
from .draw import Draw
from .components.transform import Transform
from .engine import Engine
from pygame.math import Vector2


class GameObject(NormalBehavior):

    current_running_scene = 0

    def __init__(self, position, rotation, scale):
        """
        set basics game_objects parameters
        :param position_x: game_object's x initial position
        :param position_y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale_x: game_object's x initial scale
        :param scale_y: game_object's y initial scale
        :param color: game_object's initial material color
        :param type: string representing the object type (Circle or Rectangle)
        """
        self.transform = Transform(position, rotation, scale)

    def draw_game_object(self):
        """
        Draw the game_object on screen
        """
        if hasattr(self, 'rectangle_mash'):
            Draw.rect(Vector2(self.transform.position.x, self.transform.position.y),
                      Vector2(self.transform.scale.x * self.rectangle_mash.dimension.x,
                              self.transform.scale.y * self.rectangle_mash.dimension.y),
                      self.rectangle_mash.material.color)

        elif hasattr(self, 'circle_mash'):
            Draw.circle(self.transform.position, self.circle_mash.radius, self.circle_mash.material.color)

    @classmethod
    def instantiate(cls, game_object):
        """
        Instantiate a new game_object on scene
        :param game_object: game_object to be instantiated
        """
        Engine.current_running_scene.add_game_object(game_object)

    @classmethod
    def destroy(cls, game_object):
        """
        Destroy the game_object, remove it from scene
        :param game_object: the game_object to be removed
        """
        Engine.current_running_scene.remove_game_object(game_object)

