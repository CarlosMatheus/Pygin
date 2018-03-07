from .draw import Draw
from .components.transform import Transform
from .scene import Scene
from pygame.math import Vector2


class GameObject:

    current_running_scene = 0

    def __init__(self, position, rotation, scale, layer):
        """
        set basics game_objects parameters
        :param position.x: game_object's x initial position
        :param position.y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale.x: game_object's x initial scale
        :param scale.y: game_object's y initial scale
        :param layer: the layer in the order of screen
        """
        self.transform = Transform(position, rotation, scale, layer)
        self.__instantiate(self)

    def start(self):
        """
        Will be called just once when the GameObject is instantiate on scene
        """
        pass

    def update(self):
        """
        Will be call every frame
        """
        pass

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

        elif hasattr(self, 'polygon_mash'):
            Draw.polygon(self.polygon_mash.material.color, self.polygon_mash.point_list)

        elif hasattr(self, 'text_mash'):
            Draw.text(self.transform.position.x, self.transform.position.y, self.text_mash.message,
                      self.text_mash.color, self.text_mash.size, self.text_mash.font)
        else:
            pass

    @classmethod
    def __instantiate(cls, game_object):
        """
        Instantiate a new game_object on scene
        :param game_object: game_object to be instantiated
        """
        Scene.current_running_scene.add_game_object(game_object)

    @classmethod
    def destroy(cls, game_object):
        """
        Destroy the game_object, remove it from scene
        :param game_object: the game_object to be removed (Can be a list)
        """
        if isinstance(game_object, list) or isinstance(game_object, tuple):
            for game_obj in game_object:
                Scene.current_running_scene.remove_game_object(game_obj)
        else:
            Scene.current_running_scene.remove_game_object(game_object)
