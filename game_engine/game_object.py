from .draw import Draw
from .components.transform import Transform
from .scene import Scene
from pygame.math import Vector2


class GameObject:

    current_running_scene = 0

    def __init__(self, position=Vector2(0, 0), rotation=0, scale=Vector2(1, 1), layer=0):
        """
        set basics mesh_objects parameters
        :param position.x: game_object's x initial position
        :param position.y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale.x: game_object's x initial scale
        :param scale.y: game_object's y initial scale
        :param layer: the layer in the order of screen
        """
        self.transform = 0
        self.transform = Transform(self, position, rotation, scale, layer)
        self.transform.transform = self.transform
        self.tag = None
        self.animator = None
        self.animation = None
        self.material = None
        self.physics = None
        self.polygon_mesh = None
        self.particle_system = None
        self.circle_mesh = None
        self.text_mesh = None
        self.collidable = True
        self.__instantiate(self)

    def awake(self):
        """
        Will be called just once when the GameObject is instantiate on scene and will be called before start
        """
        pass

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

    def protected_start(self):
        if self.polygon_mesh is not None:
            self.polygon_mesh._PolygonMesh__start()

    def protected_update(self):
        """
        This method will run every frame, but it is not intended to be implemented inside a game_object
        """
        if self.animator is not None:
            self.animator._Animator__update()
        if self.physics is not None:
            self.physics._Physics__update()
        if self.polygon_mesh is not None:
            self.polygon_mesh._PolygonMesh__update()
        if self.text_mesh is not None:
            self.text_mesh._TextMesh__update()
        if self.particle_system is not None:
            self.particle_system._ParticleSystem__update()

    def draw_game_object(self):
        """
        Draw the game_object on screen
        """
        if self.polygon_mesh is not None:
            Draw.polygon(self.material.color, self.polygon_mesh.get_points(), self.material.alpha)
        elif self.circle_mesh is not None:
            Draw.circle(self.transform.position, self.circle_mesh.get_radius(), self.material.color, self.material.alpha)
        elif self.text_mesh is not None:
            Draw.text(self.transform.position.x, self.transform.position.y, self.text_mesh.label, self.material.alpha)

    def _get_points(self):
        return None

    def destroy_me(self):
        GameObject.destroy(self)

    @classmethod
    def find_by_type(cls, game_object_type_string):
        """
        Find all the mesh_objects of that type in the current running scene
        :param game_object_type_string: a string with the game_object type(Class)
        :return: a list with all the mesh_objects of that type
        """
        return Scene.current_running_scene.find_game_object_by_type(game_object_type_string)

    @classmethod
    def find_by_tag(cls, game_object_tag_string):
        """
        Find all the mesh_objects with that tag in the current running scene
        :param game_object_tag_string: the tag name
        :return: a list with all game_object in the scene with that tag
        """
        return Scene.current_running_scene.find_game_object_by_tag(game_object_tag_string)

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
