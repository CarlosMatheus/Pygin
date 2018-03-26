from game_engine.basic_objects.basic_circle import BasicCircle
from game_engine.basic_objects.basic_rectangle import BasicRectangle
from game.game_objects.mesh_objects.star import Star
from game.animations.circle_player_initial_animation import CirclePlayerInitialAnimation
from game_engine.components.animator import Animator
from game_engine.game_object import GameObject
from game_engine.components.circle_collider import CircleCollider
from game_engine.color import Color
from pygame import mixer


class PlayerCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(PlayerCircle, self).__init__(position, radius, material, layer=-2)
        self.circle_collider = CircleCollider(self)
        self.is_invencible = False

    def start(self):
        self.star_score_controller = GameObject.find_by_type("StarScoreController")[0]
        self.main_scene_controller = GameObject.find_by_type("MainSceneController")[0]
        self.invencible_power_up_controller = GameObject.find_by_type("InvenciblePowerUpController")[0]
        self.animation = CirclePlayerInitialAnimation(self)
        self.animator = Animator(self, [self.animation])
        self.death_sound = mixer.Sound('game/assets/soundtrack/ball_death.wav')

    def update(self):
        (collided, game_obj) = self.circle_collider.on_collision()
        if collided:
            if issubclass(type(game_obj), BasicRectangle) and not self.is_invencible and game_obj.collidable:
                self.main_scene_controller.game_over()
                self.death_sound.play()
            elif issubclass(type(game_obj), Star):
                GameObject.destroy(game_obj)
                self.star_score_controller.get_star()
            elif issubclass(type(game_obj), BasicCircle):
                GameObject.destroy(game_obj)
                self.invencible_power_up_controller.get_power_up()
