from game_engine.input import Input
from game_engine.time import Time
from elements.game_objects.game_objects.player_circle import PlayerCircle
from pygame.math import Vector2
from elements.game_objects.material import Material
from game_engine.game_object import GameObject
from elements.game_objects.constants import Constants
import math


class PlayerController(GameObject):

    def start(self):
        self.angle = 0.0
        self.angularSpeed = 5.0
        self.game_object_list = [
            PlayerCircle(Vector2(Constants.circCenter_x + Constants.circRadius, Constants.screen_height+15), 15, Material((253, 102, 0))),
            PlayerCircle(Vector2(Constants.circCenter_x - Constants.circRadius, Constants.screen_height+15), 15, Material((0, 120, 255)))
        ]
        self.in_initial_animation = True
        self.should_play = True
        self.initial_time = Time.now()

    def update(self):
        self.initial_animation()
        if not self.in_initial_animation:
            if Input.is_pressing_left:
                self.turn_left()
            if Input.is_pressing_right:
                self.turn_right()

    def initial_animation(self):
        if self.in_initial_animation:
            if self.should_play:
                self.should_play = False
                self.game_object_list[0].animator.play()
                self.game_object_list[1].animator.play()
        if Time.now() - self.initial_time > 1.0:
            self.in_initial_animation = False

    def turn_right(self):
        self.angle = (self.angle + self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def turn_left(self):
        self.angle = (self.angle - self.angularSpeed * Time.delta_time()) % (2 * math.pi)
        self.update_circles()

    def update_circles(self):
        self.game_object_list[0].transform.\
            translate(Vector2(Constants.circCenter_x + Constants.circRadius * math.cos(self.angle),
                              Constants.circCenter_y + Constants.circRadius * math.sin(self.angle)))

        self.game_object_list[1].transform.\
            translate(Vector2(Constants.circCenter_x + Constants.circRadius * math.cos(self.angle + math.pi),
                              Constants.circCenter_y + Constants.circRadius * math.sin(self.angle + math.pi)))
