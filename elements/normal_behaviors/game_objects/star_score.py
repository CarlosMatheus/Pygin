from pygame.math import Vector2
from game_engine.time import Time
from game_engine.engine import Engine
from game_engine.normal_behavior import NormalBehavior
from game_engine.components.material import Material
from game_engine.color import Color
from elements.normal_behaviors.game_objects.circle import Circle


class StarScore(NormalBehavior):

    def start(self):
        self.fall_velocity = 250
        self.circle = Circle(Vector2(100, 100), 10, Material(Color.yellow))

    def update(self):
        self.fall(self.circle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                        + self.fall_velocity * Time.delta_time())