from pygame.math import Vector2
from game.game_objects.mesh_objects.star import Star
from pygame import mixer
from game_engine.time import Time
from game_engine.game_object import GameObject
from random import uniform as randfloat
from game_engine.basic_objects.text import Text
from game_engine.material import Material
from game_engine.color import Color
from game.scripts.constants import Constants
from game.animations.text_up_fade_out_animation import TextUpFadeOutAnimation
from game_engine.components.animator import Animator


class StarScoreController(GameObject):

    def start(self):
        self.fall_velocity = 250
        self.angular_speed = 0
        self.game_object_list = []
        self.size = Constants.screen_width * 0.03
        self.points_per_star = 50
        self.sound_collect = mixer.Sound('game/assets/soundtrack/star_collect.wav')
        self.should_delete_plus_score_text = False
        self.plus_score_text_gen_time = 0.0

    def awake(self):
        self.score_controller = GameObject.find_by_type("ScoreController")[0]

    def update(self):
        for obstacle in self.game_object_list:
            if obstacle.transform.position.y > Constants.screen_height:
                self.game_object_list.remove(obstacle)
                obstacle.destroy(obstacle)
                GameObject.destroy(obstacle)
            else:
                self.fall(obstacle)
        self.delete_plus_score_text()

    def fall(self, obstacle):
        obstacle.fall(self.fall_velocity * Time.delta_time(), self.angular_speed * Time.delta_time())

    def get_star(self):
        self.sound_collect.play()
        obstacle = self.game_object_list[0]

        #plus score effect
        font_path = "game/assets/fonts/neuropolxrg.ttf"
        plus_score = Text(obstacle.transform.position, "+50", Material(Color.white, alpha=255), 15, font_path)
        plus_score.transform.position.x -= plus_score.text_mesh.size
        plus_score.animation = TextUpFadeOutAnimation(plus_score)
        plus_score.animator = Animator(plus_score, [plus_score.animation])
        plus_score.animator.play()
        self.time_of_last_plus_score = Time.now()
        self.plus_score = plus_score
        self.should_delete_plus_score_text = True

        self.score_controller.score += self.points_per_star

    def delete_plus_score_text(self):
        if self.should_delete_plus_score_text:
            if Time.now() - self.time_of_last_plus_score > 1.0:
                self.should_delete_plus_score_text = False
                self.plus_score.destroy_me()

    def generate_obstacle(self):
        random_pos = int(randfloat(self.size / 2 + Constants.circCenter_x - Constants.circRadius,
                                   Constants.screen_width -
                                   (self.size / 2 + Constants.circCenter_x - Constants.circRadius)))

        star = Star(Vector2(random_pos, -self.size), self.size,
                    Material(Color.yellow))
        self.game_object_list.append(star)
