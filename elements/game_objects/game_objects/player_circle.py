from elements.game_objects.game_objects.basic_objects.basic_circle import BasicCircle
from elements.game_objects.game_objects.basic_objects.basic_rectangle import BasicRectangle
from elements.game_objects.game_objects.star import Star
from game_engine.game_object import GameObject
from game_engine.scene import Scene
from game_engine.components.circle_collider import CircleCollider


class PlayerCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(PlayerCircle, self).__init__(position, radius, material, layer = -2)
        self.circle_collider = CircleCollider(self)

    def start(self):
        pass

    def update(self):
        (collided, game_obj) = self.circle_collider.on_collision()
        if collided:
            if issubclass(type(game_obj), BasicRectangle):
                Scene.change_scene(2)
            elif issubclass(type(game_obj), Star):
                GameObject.destroy(game_obj)
