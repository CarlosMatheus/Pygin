from game_engine.time import Time
from random import randint as rand
from pygame.math import Vector2

#Controllers
from game.game_objects.controllers.obstacles_controllers.simple_obstacle_controller import SimpleObstacleController
from game.game_objects.controllers.obstacles_controllers.middle_rect_obstacle_controller import MiddleRectObstacleController
from game.game_objects.controllers.obstacles_controllers.random_x_final_obstacle_controller import RandomXFinalObstacleController
from game.game_objects.controllers.obstacles_controllers.rect_translate_x_obstacle_cotroller import RectTranslateXObstacleController
from game.game_objects.controllers.obstacles_controllers.two_in_one_simple_obstacle_controller import TwoInOneSimpleObstacleController
from game.game_objects.controllers.obstacles_controllers.two_side_by_side_obstacle_controller import TwoSideBySideSimpleObstacleController
from game.game_objects.controllers.items_controller.star_score_controller import StarScoreController
from game.game_objects.controllers.items_controller.invencible_power_up_controller import InvenciblePowerUpController
from game.game_objects.controllers.obstacles_controllers.spinning_middle_rect_obstacle_controller import SpinningMiddleRectObstacleController
from game.game_objects.controllers.obstacles_controllers.half_moon_spinning_rect_obstacle_controller import HalfMoonSpinningRectObstacleController
from game_engine.game_object import GameObject


class ObstacleControllerWrapper(GameObject):

    def start(self):
        self.obstacle_generators = [
            SimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            MiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            TwoInOneSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            TwoSideBySideSimpleObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            HalfMoonSpinningRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            RectTranslateXObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0),
            SpinningMiddleRectObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        ]
        self.rect_x_controller = RandomXFinalObstacleController(Vector2(0, 0), 0, Vector2(0, 0), 0)
        self.obstacle_geneation_delta = 1500
        self.last_generation_time = 1000 * Time.now()
        self.game_object_list = []
        self.last_increases_dificculty_time = Time.now()
        self.game_difficuty = 1
        self.time_to_increase_difficult = 6
        self.generation_obstacle_difficult = 1
        self.max_difficult = 10

        for obstacle_generator in self.obstacle_generators:
            obstacle_generator.start()

    def update(self):
        self.increase_difficult()
        if 1000 * Time.now() - self.last_generation_time > self.obstacle_geneation_delta * \
                self.generation_obstacle_difficult:
            self.generate_random_obstacle()

        for obstacle_generator in self.obstacle_generators:
            game_objs = obstacle_generator.game_object_list
            self.game_object_list.extend(game_objs)

    def increase_difficult(self):
        if Time.now() - self.last_increases_dificculty_time > self.time_to_increase_difficult \
                and self.game_difficuty < self.max_difficult:

            title_x = 20
            title_y = 180
            title_size = 50
            font_path = "game/assets/fonts/neuropolxrg.ttf"
            # Text(Vector2(title_x, title_y), "Difficulty Increased!", Color.white, title_size, font_path)

            self.game_difficuty += 1
            self.last_increases_dificculty_time = Time.now()
            self.time_to_increase_difficult *= 1.02
            self.generation_obstacle_difficult = (1 - (self.game_difficuty - 1) * 0.2 / self.max_difficult)

            if(self.game_difficuty == 7 and len(self.obstacle_generators) > 3):
                self.delete_object_with_specific_type(SimpleObstacleController)
                self.delete_object_with_specific_type(TwoInOneSimpleObstacleController)

            if(self.game_difficuty == 10):
                print("Max difficult!")
                self.delete_object_with_specific_type(TwoSideBySideSimpleObstacleController)
                self.delete_object_with_specific_type(HalfMoonSpinningRectObstacleController)
            else:
                print("Difficulty Increases to " + str(self.game_difficuty))

    def generate_random_obstacle(self):
        self.last_generation_time = 1000 * Time.now()

        number_of_obstacles = int(min(self.game_difficuty, len(self.obstacle_generators)))
        random_ind = rand(0, number_of_obstacles-1)
        random_obstacle_generator = self.obstacle_generators[random_ind]
        if type(random_obstacle_generator) == RectTranslateXObstacleController:
            self.last_generation_time -= 300

        if self.game_difficuty == self.max_difficult:
            self.rect_x_controller.generate_obstacle()
        random_obstacle_generator.generate_obstacle()

    def delete_object_with_specific_type(self, obstacle_type):
        for i in range(len(self.obstacle_generators)):
            if type(self.obstacle_generators[i]) == obstacle_type:
                self.obstacle_generators.pop(i)
                break
