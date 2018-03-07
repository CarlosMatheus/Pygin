from game_engine.engine import Engine
from random import randint as rand
from game_engine.normal_behavior import NormalBehavior
from game_engine.game_object import GameObject
from elements.normal_behaviors.game_objects.main_menu_rectangle import Rectangle
from game_engine.game_object import GameObject
from game_engine.input import Input
from game_engine.color import Color
from game_engine.time import Time
from elements.normal_behaviors.game_objects.text import Text
from game_engine.components.material import Material
from pygame.math import Vector2


class MainMenuController(NormalBehavior):

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.time = Time.now()
        self.period = 1

        font_path = "assets/fonts/neuropolxrg.ttf"

        message_x = 10
        message_y = 270
        message_size = 14

        title_x = 37
        title_y = 200
        title_size = 50

        self.game_object_list = [
            Text(Vector2(message_x, message_y), "Press arrows keys to start playing", Color.white, message_size, font_path),
            Text(Vector2(title_x, title_y), "Balance", Color.white, title_size, font_path)
        ]
        GameObject.instantiate(self.game_object_list)

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        if self.should_spawn():
            self.spawn_block()
        if self.pressed_button():
            Engine.change_scene(1)

    def spawn_block(self):
        """
        Spawn a random block
        """
        parameters = self.generate_random_parameters()
        GameObject.instantiate(Rectangle(Vector2(parameters[0], parameters[1]),
                                         Vector2(parameters[2], parameters[3]), Material(parameters[4])))

    def generate_random_parameters(self):
        """
        Generate a random parameter to create a random block
        :return: a Tuple with the parameters
        """
        width = rand(20, 100)
        height = rand(10, 90)
        color = Color.random_color()
        position_x = rand(10, Engine.screen_width - width - 10)
        position_y = -height
        return position_x, position_y, width, height, color

    def pressed_button(self):
        """
        :return: if it should change scene
        """
        return Input.is_pressing_right or Input.is_pressing_left

    def should_spawn(self):
        """
        :return: if it should spawn
        """
        if Time.now() - self.time > self.period:
            self.time = Time.now()
            return True
        else:
            return False
