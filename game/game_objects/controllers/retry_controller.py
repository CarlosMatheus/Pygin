from random import randint as rand
from game.game_objects.mesh_objects.main_menu_rectangle import Rectangle
from game_engine.scene import Scene
from game_engine.game_object import GameObject
from game_engine.input import Input
from game_engine.color import Color
from game_engine.time import Time
from game.game_objects.mesh_objects.text import Text
from game.scripts.material import Material
from pygame.math import Vector2
from game.scripts.constants import Constants
from game.game_objects.mesh_objects.screen_fader import ScreenFader
from game.game_objects.controllers.background_particles_controller import BackgroundParticlesController


class RetryController(GameObject):

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.time = Time.now()
        self.period = 1.5

        font_path = "game/assets/fonts/neuropolxrg.ttf"

        message_x = 15
        message_y = 300
        message_size = 14

        score = str(int(Constants.current_score))
        score_size = 28
        score_x = 30
        score_y = 240

        title_x = 20
        title_y = 180
        title_size = 50

        self.game_object_list = [
            Text(Vector2(title_x, title_y), "You died", Color.red, title_size, font_path),
            Text(Vector2(score_x, score_y), "Score: " + score, Color.white, score_size, font_path),
            Text(Vector2(message_x, message_y), "Press arrows keys to try again", Color.white, message_size, font_path)
        ]
        self.setup_fader()
        BackgroundParticlesController()

    def setup_fader(self):
        """
        Start fade in and set variables to fade out
        """
        ScreenFader(fade="in")
        self.should_timer = False
        self.should_change_scene = False
        self.can_press_button = True

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        if self.should_spawn():
            self.spawn_block()
        if self.pressed_button() and self.can_press_button:
            self.should_timer = True
            self.can_press_button = False
        if self.should_timer:
            ScreenFader(fade="out")
            self.timer = Time.now()
            self.should_timer = False
            self.should_change_scene = True
        if self.should_change_scene:
            if Time.now() - self.timer > 0.68:
                Scene.change_scene(1)

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
