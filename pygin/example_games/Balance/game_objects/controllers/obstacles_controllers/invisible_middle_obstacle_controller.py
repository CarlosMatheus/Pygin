from pygame.math import Vector2
from pygin.time import Time
from pygin.game_object import GameObject
from Balance.game_objects.mesh_objects.obstacle_rectangle import Rectangle
from Balance.scripts.constants import Constants
from pygin.material import Material
from Balance.animations.obstacle_pulsing_animation import ObstaclePulsingAnimation
from Balance.animations.power_up_fade_out import PowerUpFadeOut
from pygin.components.animator import Animator


class InvisibleMiddleObstacleController(GameObject):

    def start(self):
        self.fall_velocity = 400
        self.game_object_list = []

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)

            if obstacle.visible and obstacle.transform.position.y > 0.15 * Constants.screen_height:
                self.turn_invisible(obstacle)
                obstacle.visible = False

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())

    def turn_invisible(self, game_obj):
        game_obj.animation = PowerUpFadeOut(game_obj)
        game_obj.animator = Animator(game_obj, [game_obj.animation])
        game_obj.animator.play()

    def generate_obstacle(self):
        self.obstacle_width = 0.3 * Constants.screen_width
        self.obstacle_height = 0.06 * Constants.screen_height
        rect = Rectangle(Vector2(0.5 * Constants.screen_width - 0.5 * self.obstacle_width, - 3*self.obstacle_height),
                         Vector2(self.obstacle_width, self.obstacle_height),
                         Material((255, 255, 255)))
        rect.animation = ObstaclePulsingAnimation(rect)
        rect.animator = Animator(rect, [rect.animation])
        rect.animator.play()
        rect.visible = True
        self.game_object_list.append(rect)
