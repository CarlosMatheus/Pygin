from game_engine.input import Input
from game_engine.time import Time
from game_engine.normal_behavior import NormalBehavior
from elements.normal_behaviors.game_objects.circle import Circle
from pygame.math import Vector2
from game_engine.components.material import Material
from elements.normal_behaviors.game_objects.text import Text
from game_engine.engine import Engine

import math


class PlayerController(NormalBehavior):

    def start(self):

        self.angle = 0.0
        self.angularSpeed = 5.0

        self.game_object_list = [
            Circle(Vector2(Engine.circCenter_x + Engine.circRadius, Engine.circCenter_y), 15, Material((253, 102, 0))),
            Circle(Vector2(Engine.circCenter_x - Engine.circRadius, Engine.circCenter_y), 15, Material((0, 120, 255)))
        ]

    def update(self):
        if Input.is_pressing_left:
            self.turn_left()
        if Input.is_pressing_right:
            self.turn_right()

        for game_object in self.game_object_list:
            game_object.update()

    def turn_right(self):
        self.angle = (self.angle + self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def turn_left(self):
        self.angle = (self.angle - self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def update_circles(self):
        self.game_object_list[0].transform.\
            translate(Vector2(Engine.circCenter_x + Engine.circRadius * math.cos(self.angle),
                              Engine.circCenter_y + Engine.circRadius * math.sin(self.angle)))

        self.game_object_list[1].transform.\
            translate(Vector2(Engine.circCenter_x + Engine.circRadius * math.cos(self.angle + math.pi),
                              Engine.circCenter_y + Engine.circRadius * math.sin(self.angle + math.pi)))
