from pygame.math import Vector2
from game_engine.time import Time
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.constants import Constants
from game_engine.material import Material
from random import uniform as randfloat
from random import randint

class RectTranslateXObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 400
        self.translate_velocity = 600
        self.game_object_list = []
        self.obstacle_size = 0.05 * Constants.screen_height

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        new_x = obstacle.transform.position.x + self.translate_velocity \
                * Time.delta_time() * obstacle.vel

        if new_x > Constants.screen_width - self.obstacle_size/2 \
                or new_x < -self.obstacle_size/2:
            obstacle.vel *= -1
        obstacle.transform.position = Vector2(new_x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def generate_obstacle(self):


        random_pos = int(randfloat(Constants.screen_width - self.obstacle_size / 2-1,
                                   -self.obstacle_size / 2+1))

        rect = Rectangle(Vector2(random_pos, -self.obstacle_size),
                         Vector2(self.obstacle_size, self.obstacle_size),
                         Material((255, 255, 255)))

        direction = randint(0, 1)
        if direction == 0:
            direction = -1
        rect.vel = direction  # Checks if going left or right. Can be 1 for right or -1 for left
        self.game_object_list.append(rect)
