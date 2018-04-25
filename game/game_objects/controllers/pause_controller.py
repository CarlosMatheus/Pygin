from random import randint as rand
from game.game_objects.mesh_objects.main_menu_rectangle import Rectangle
from game_engine.scene import Scene
from game_engine.game_object import GameObject
from game_engine.input import Input
from game_engine.color import Color
from game_engine.time import Time
from game_engine.basic_objects.text import Text
from game_engine.material import Material
from pygame.math import Vector2
from game.scripts.constants import Constants
from game.game_objects.mesh_objects.screen_fader import ScreenFader
from game.game_objects.controllers.background_particles_controller import BackgroundParticlesController

class PauseController(GameObject):

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

        title_x = 20
        title_y = 180
        title_size = 50

        self.game_object_list = [
            Text(Vector2(title_x, title_y), "PAUSED", Material(Color.red), title_size, font_path),
            Text(Vector2(message_x, message_y), "Press space to keep playing", Material(Color.white), message_size, font_path),
            Rectangle(Vector2(0, 0), Vector2(Constants.screen_width, Constants.screen_height), Material(Color.mask))
        ]

        self.game_object_list[2].collidable = False

    def destroy_all_text(self):
        for text in self.game_object_list:
            text.destroy_me()