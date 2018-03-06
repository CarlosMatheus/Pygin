from .normal_behavior import NormalBehavior
from .draw import Draw
from .components.transform import Transform


class GameObject(NormalBehavior):

    def __init__(self, position_x, position_y, rotation, scale_x, scale_y):
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
        self.transform = Transform(position_x, position_y, rotation, scale_x, scale_y)

    def draw_game_object(self):
        """
        Draw the game_object on screen
        """
        if hasattr(self, 'rectangle_mash'):
            Draw.rect(self.transform.translate[0], self.transform.translate[1], self.transform.scale[0] * self.rectangle_mash.width,
                      self.transform.scale[1] * self.rectangle_mash.height, self.rectangle_mash.color)

        elif hasattr(self, 'circle_mash'):
            Draw.circle(self.circle_mash.position_x, self.circle_mash.position_y, self.circle_mash.radius, self.circle_mash.color)
