from pygame.math import Vector2
from game_engine.time import Time
from game_engine.game_object import GameObject
from game.game_objects.mesh_objects.rectangle import Rectangle
from game.scripts.constants import Constants
from game.scripts.material import Material

class BackgroundParticlesController(GameObject):

    def start(self):
        self.fall_velocity = 60
        self.game_object_list = []
        self.rect_position = [Vector2(0.20 * Constants.screen_width, 0.00 * Constants.screen_height),
                              Vector2(0.35 * Constants.screen_width, 0.15 * Constants.screen_height),
                              Vector2(0.43 * Constants.screen_width, 0.45 * Constants.screen_height),
                              Vector2(0.69 * Constants.screen_width, 0.75 * Constants.screen_height),
                              Vector2(0.88 * Constants.screen_width, 0.90 * Constants.screen_height)]
        self.current_rect = 0

        self.generate_particles()

    def update(self):

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                obstacle.transform.position = self.rect_position[self.current_rect]
                self.current_rect += 1
            else:
                self.fall(obstacle)

    def fall(self, obstacle):
        obstacle.transform.position = Vector2(obstacle.transform.position.x, obstacle.transform.position.y
                                              + self.fall_velocity * Time.delta_time())
        obstacle.polygon_mesh.update_point_list(obstacle.get_points())

    def generate_particles(self):
        for i in range(5):
            self.obstacle_x, self.obstacle_y = self.rect_position[i].x, self.rect_position[i].y
            rect = Rectangle(Vector2(self.obstacle_x, self.obstacle_y),
                             Vector2(0.05 * Constants.screen_width, 0.05 * Constants.screen_height),
                             Material((255, 255, 255)))
            rect.polygon_collider = []
            self.game_object_list.append(rect)
