from game_engine.time import Time
from random import randint as rand
from pygame.math import Vector2
from game_engine.game_object import GameObject

#Controllers
from elements.game_objects.obstacles.simple_obstacle_controller import SimpleObstacleController
from elements.game_objects.obstacles.middle_rect_obstacle_controller import MiddleRectObstacleController
from elements.game_objects.obstacles.rect_translate_x_obstacle_cotroller import RectTranslateXObstacleController
from elements.game_objects.obstacles.two_in_one_simple_obstacle_controller import TwoInOneSimpleObstacleController
from elements.game_objects.obstacles.two_side_by_side_obstacle_controller import TwoSideBySideSimpleObstacleController
from elements.game_objects.obstacles.star_score_controller import StarScoreController
from elements.game_objects.obstacles.spinning_middle_rect_obstacle_controller import SpinningMiddleRectObstacleController
from elements.game_objects.obstacles.half_moon_spinning_rect_obstacle_controller import HalfMoonSpinningRectObstacleController
from game_engine.game_object import GameObject


class ObstacleControllerWrapper(GameObject):

    def awake(self):
        self.power_up_generators = [StarScoreController(Vector2(0, 0), 0, Vector2(0, 0), 0)]

    def start(self):
        self.obstacle_generators = [
            # SimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # MiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # TwoInOneSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # TwoSideBySideSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # RectTranslateXObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # SpinningMiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            HalfMoonSpinningRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        ]

        self.power_up_generation_delta = 5000
        self.obstacle_geneation_delta = 1500
        self.last_generation_time = 1000 * Time.now()
        self.last_power_up_time = 1000 * Time.now()
        self.game_object_list = []
        self.last_increases_dificculty_time = Time.now()
        self.game_difficuty = 1
        self.time_to_increase_difficult = 1
        self.generation_obstacle_difficult = 1
        self.max_difficult = 10

        for obstacle_generator in self.obstacle_generators:
            obstacle_generator.start()
        for power_up_generator in self.power_up_generators:
            power_up_generator.start()

    def update(self):
        if Time.now() - self.last_increases_dificculty_time > self.time_to_increase_difficult \
                and self.game_difficuty <= self.max_difficult:
            print("Difficulty Increase!")
            self.game_difficuty += 1
            self.last_increases_dificculty_time = Time.now()
            self.generation_obstacle_difficult = (1 - (self.game_difficuty - 1) * 0.2 / self.max_difficult)

        if 1000 * Time.now() - self.last_generation_time > self.obstacle_geneation_delta * \
                self.generation_obstacle_difficult:
            self.generate_random_obstacle()

        for obstacle_generator in self.obstacle_generators:
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

        if 1000 * Time.now() - self.last_power_up_time > self.power_up_generation_delta * \
                self.generation_obstacle_difficult:
            self.generate_random_power_up()

        for power_up_generator in self.power_up_generators:
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

    def generate_random_obstacle(self):
        self.last_generation_time = 1000 * Time.now()

        number_of_obstacles = min(self.game_difficuty, len(self.obstacle_generators))

        print(number_of_obstacles)

        random_ind = rand(0, number_of_obstacles)% number_of_obstacles
        random_obstacle_generator = self.obstacle_generators[random_ind]
        random_obstacle_generator.generate_obstacle()

    def generate_random_power_up(self):
        self.last_power_up_time = 1000 * Time.now()

        random_ind = rand(0, len(self.power_up_generators))%len(self.power_up_generators)
        random_obstacle_generator = self.power_up_generators[random_ind]
        random_obstacle_generator.generate_obstacle()
