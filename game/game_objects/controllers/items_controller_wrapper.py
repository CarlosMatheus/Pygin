from game_engine.time import Time
from random import randint as rand
from pygame.math import Vector2

#Controllers
from game.game_objects.controllers.items_controller.star_score_controller import StarScoreController
from game.game_objects.controllers.items_controller.invencible_power_up_controller import InvenciblePowerUpController
from game_engine.game_object import GameObject


class ItemsControllerWrapper(GameObject):

    def start(self):
        self.power_up_generators = [StarScoreController(Vector2(0, 0), 0, Vector2(0, 0), 0),
                                    InvenciblePowerUpController(Vector2(0, 0), 0, Vector2(0, 0), 0)]

        self.power_up_generation_delta = 7500
        self.last_power_up_time = 1000 * Time.now()
        self.generation_obstacle_difficult = 1

        for power_up_generator in self.power_up_generators:
            power_up_generator.start()

    def update(self):

        if 1000 * Time.now() - self.last_power_up_time > self.power_up_generation_delta * \
                self.generation_obstacle_difficult:
            self.generate_random_power_up()

    def generate_random_power_up(self):
        self.last_power_up_time = 1000 * Time.now()

        random_ind = rand(0, 10)
        if random_ind >= 5:
            random_ind = 1
        else:
            random_ind = 0
        random_obstacle_generator = self.power_up_generators[random_ind]
        random_obstacle_generator.generate_obstacle()
