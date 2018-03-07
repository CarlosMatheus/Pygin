from game_engine.input import Input
from game_engine.time import Time
from random import randint as rand
from game_engine.engine import Engine
from game_engine.normal_behavior import NormalBehavior
from elements.normal_behaviors.game_objects.rectangle import Rectangle

import math

class ObstaclesController(NormalBehavior):

    def start(self):
        self.fall_velocity = 250
        self.game_object_list = []
        self.last_generation_time = 0

    def update(self):

        if 1000 * Time.now() - self.last_generation_time > 1500:
            self.generate_simple_obstacle()

        for obstacle in self.game_object_list:
            if (obstacle.rectangle_mash.position_y > Engine.screen_height):
                obstacle.destroy()
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.translate = (obstacle.transform.translate[0], obstacle.transform.translate[1]
                                        + self.fall_velocity * Time.delta_time())

    def generate_simple_obstacle(self):
        self.last_generation_time = 1000 * Time.now()

        direction = rand(0,1) < 0.5
        rect = Rectangle(direction * 0.6 * Engine.screen_width, - 0.1 * Engine.screen_height, 0.4 * Engine.screen_width,
                         0.1 * Engine.screen_height, (255, 255, 255))
        self.game_object_list.append(rect)
