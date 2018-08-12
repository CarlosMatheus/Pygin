from random import randint as rand
from pygin.game_object import GameObject
from Balance.game_objects.mesh_objects.main_menu_rectangle import Rectangle
from pygin.color import Color
from pygin.time import Time
from pygame.math import Vector2
from pygin.material import Material


class TestRectGenerator(GameObject):

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.time = Time.now()
        self.period = 1

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        if self.should_spawn():
            self.spawn_block()

    def spawn_block(self):
        """
        Spawn a random block
        """
        parameters = self.generate_random_parameters()
        Rectangle(Vector2(parameters[0], parameters[1]),
                                         Vector2(parameters[2], parameters[3]), Material(parameters[4]))

    def generate_random_parameters(self):
        """
        Generate a random parameter to create a random block
        :return: a Tuple with the parameters
        """
        width = rand(20, 100)
        height = rand(10, 90)
        color = Color.random_color()
        position_x = rand(10, Constants.screen_width - width - 10)
        position_y = -height
        return position_x, position_y, width, height, color

    def should_spawn(self):
        """
        :return: if it should spawn
        """
        if Time.now() - self.time > self.period:
            self.time = Time.now()
            return True
        else:
            return False
