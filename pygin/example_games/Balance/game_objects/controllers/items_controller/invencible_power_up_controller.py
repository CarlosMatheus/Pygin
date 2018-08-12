from pygame.math import Vector2
from pygame import mixer
from game_engine.time import Time
from game_engine.game_object import GameObject
from random import uniform as randfloat
from Balance.game_objects.mesh_objects.invencible_circle import InvencibleCircle
from game_engine.material import Material
from game_engine.basic_objects.text import Text
from game_engine.color import Color
from Balance.scripts.constants import Constants
from Balance.animations.text_up_fade_out_animation import TextUpFadeOutAnimation
from game_engine.components.animator import Animator


class InvenciblePowerUpController(GameObject):

    def start(self):
        self.fall_velocity = 150
        self.radius = Constants.screen_width * 0.025
        self.game_object_list = []
        self.sound_collect = mixer.Sound('Balance/assets/soundtrack/powerup_collect_01.ogg')
        self.time_of_last_invencibily = -1000
        self.invecible_time = 3.5
        self.current_color = "normal"
        self.animation_ticks_times = [0.4, 0.5, 0.6, 0.7, 0.75, 0.80, 0.85, 0.90, 0.95, 1.00, 1.10]
        self.current_animation_tick_index = 0
        self.should_delete_power_up_text = False
        self.power_up_text_gen_time = 0.0

    def awake(self):
        self.player_controller = GameObject.find_by_type("PlayerController")[0]

    def update(self):

        if Time.time_scale == 0.0:
            #Paused Balance. Adjust timers
            self.time_of_last_invencibily += Time.delta_time(True)

        difference_time = Time.now() - self.time_of_last_invencibily
        if difference_time > self.invecible_time:
            for i in range(2):
                self.player_controller.game_object_list[i].is_invencible = False
            self.get_back_to_original_colors()
            self.current_animation_tick_index = 0
        else:
            value = min(difference_time / self.invecible_time, 1)  # Just to convert between 0 and 1
            diff = abs(value - self.animation_ticks_times[self.current_animation_tick_index])
            if(diff < 0.01):
                self.current_animation_tick_index += 1
                self.tick_colors()

        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)
        self.delete_power_up_text()

    def fall(self, obstacle):
        obstacle.transform.position.y = obstacle.transform.position.y + (self.fall_velocity * Time.delta_time())

    def get_power_up(self):
        self.sound_collect.play()
        power_up = self.game_object_list[0]
        #Power up text effect
        font_path = "Balance/assets/fonts/neuropolxrg.ttf"
        text_size = 15
        power_up_text = Text(power_up.transform.position, "INVENCIBLE!", Material(Color.purple, alpha=255), text_size, font_path)
        power_up_text.transform.position.x -= power_up_text.text_mesh.size
        power_up_text.animation = TextUpFadeOutAnimation(power_up_text)
        power_up_text.animator = Animator(power_up_text, [power_up_text.animation])
        power_up_text.animator.play()

        for i in range(2):
            self.player_controller.game_object_list[i].is_invencible = True
        self.change_colors_to_green()
        self.time_of_last_invencibily = Time.now()
        self.power_up_text = power_up_text
        self.should_delete_power_up_text = True

    def delete_power_up_text(self):
        if self.should_delete_power_up_text:
            if Time.now() - self.time_of_last_invencibily > 1.0:
                self.should_delete_power_up_text = False
                self.power_up_text.destroy_me()

    def generate_obstacle(self):
        random_pos = int(randfloat(self.radius + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.radius + Constants.circCenter_x - Constants.circRadius)))

        circle = InvencibleCircle(Vector2(random_pos, -2 * self.radius), self.radius,
                                  Material(Color.purple))

        self.game_object_list.append(circle)

    def tick_colors(self):
        if(self.current_color == "normal"):
            self.current_color = "green"
            self.change_colors_to_green()
        else:
            self.current_color = "normal"
            self.get_back_to_original_colors()

    def get_back_to_original_colors(self):
        self.player_controller.game_object_list[0].change_color(Color.orange)
        self.player_controller.game_object_list[1].change_color(Color.blue)

    def change_colors_to_green(self):
        for i in range(2):
            self.player_controller.game_object_list[i].change_color(Color.purple)
