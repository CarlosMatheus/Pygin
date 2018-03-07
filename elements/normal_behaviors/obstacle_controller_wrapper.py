from game_engine.time import Time
from random import randint as rand
from game_engine.normal_behavior import NormalBehavior

#Controllers
from elements.normal_behaviors.obstacles.simple_obstacle_controller import SimpleObstacleController
from elements.normal_behaviors.obstacles.middle_rect_obstacle_controller import MiddleRectObstacleController
from elements.normal_behaviors.obstacles.two_in_one_simple_obstacle_controller import TwoInOneSimpleObstacleController
from elements.normal_behaviors.obstacles.star_score_controller import StarScoreController


class ObstacleControllerWrapper(NormalBehavior):

    def start(self):
        self.obstacle_generators = [
            SimpleObstacleController(),
            MiddleRectObstacleController(),
            TwoInOneSimpleObstacleController()
        ]

        self.power_up_generators = [StarScoreController()]

        self.last_generation_time = 1000 * Time.now()
        self.last_power_up_time = 1000 * Time.now()
        self.game_object_list = []

        for obstacle_generator in self.obstacle_generators:
            obstacle_generator.start()
        for power_up_generator in self.power_up_generators:
            power_up_generator.start()

    def update(self):
        self.game_object_list = []

        if 1000 * Time.now() - self.last_generation_time > 1500:
            self.generate_random_obstacle()

        for obstacle_generator in self.obstacle_generators:
            obstacle_generator.update()
            self.game_object_list.extend(obstacle_generator.game_object_list)

        if 1000 * Time.now() - self.last_power_up_time > 5000:
            self.generate_random_power_up()

        for power_up_generator in self.power_up_generators:
            power_up_generator.update()
            self.game_object_list.extend(power_up_generator.game_object_list)

    def generate_random_obstacle(self):
        self.last_generation_time = 1000 * Time.now()

        random_ind = rand(0, len(self.obstacle_generators))%len(self.obstacle_generators)
        random_obstacle_generator = self.obstacle_generators[random_ind]
        random_obstacle_generator.generate_obstacle()

    def generate_random_power_up(self):
        self.last_power_up_time = 1000 * Time.now()

        random_ind = rand(0, len(self.power_up_generators))%len(self.power_up_generators)
        random_obstacle_generator = self.power_up_generators[random_ind]
        random_obstacle_generator.generate_obstacle()
