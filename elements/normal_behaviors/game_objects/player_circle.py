from game_engine.components.circle_mash import CircleMash
from game_engine.engine import Engine
from game_engine.game_object import GameObject
from game_engine.components.circle_collider import CircleCollider
from pygame.math import Vector2


class Circle(GameObject):

    def __init__(self, position, radius, material):
        self.circle_mash = CircleMash(radius, material)
        self.circle_collider = CircleCollider(self)
        super(Circle, self).__init__(position, 0, Vector2(1, 1))

    def update(self):
        if self.circle_collider.on_collision():
            Engine.change_scene(1)