from elements.normal_behaviors.game_objects.basic_objects.basic_circle import BasicCircle
from elements.normal_behaviors.game_objects.basic_objects.basic_rectangle import BasicRectangle
from game_engine.game_object import GameObject
from game_engine.engine import Engine
from game_engine.components.circle_collider import CircleCollider


class PlayerCircle(BasicCircle):

    def __init__(self, position, radius, material):
        self.circle_collider = CircleCollider(self)
        super(PlayerCircle, self).__init__(position, radius, material)

    def start(self):
        pass

    def update(self):
        (collided, game_obj) = self.circle_collider.on_collision()
        if collided:
            if issubclass(type(game_obj), BasicRectangle):
                Engine.change_scene(1)
            elif issubclass(type(game_obj), BasicCircle):
                # print("--- POWERUP! ---")
                GameObject.destroy(game_obj)
