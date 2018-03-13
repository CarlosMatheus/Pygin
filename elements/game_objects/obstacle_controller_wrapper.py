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
from game_engine.game_object import GameObject


class ObstacleControllerWrapper(GameObject):

    def start(self):
        self.obstacle_generators = [
            # SimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # MiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # TwoInOneSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            # TwoSideBySideSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            RectTranslateXObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        ]

        self.power_up_generators = [StarScoreController(Vector2(0, 0), 0, Vector2(0, 0), 0)]

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
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

        if 1000 * Time.now() - self.last_power_up_time > 4000:
            self.generate_random_power_up()

        for power_up_generator in self.power_up_generators:
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

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
