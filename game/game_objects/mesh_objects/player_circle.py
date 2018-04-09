from game_engine.basic_objects.basic_circle import BasicCircle
from game_engine.basic_objects.basic_rectangle import BasicRectangle
from game.game_objects.mesh_objects.star import Star
from game.animations.circle_player_initial_animation import CirclePlayerInitialAnimation
from game_engine.components.particle_system import ParticleSystem
from game.game_objects.mesh_objects.player_particle import PlayerParticle
from game_engine.components.animator import Animator
from game_engine.game_object import GameObject
from game_engine.components.circle_collider import CircleCollider
from game_engine.color import Color
from pygame import mixer
from pygame.math import Vector2


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
        self.particle_system = ParticleSystem(self, PlayerParticle, quant=5, period=0.05, vel_min=20, vel_max=180, duration=0.6)
        self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="directional",
                                          direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met)
        self.particle_system.play()

    def ini_angle_met(self):
        return 0

    def fin_angle_met(self):
        return 180

    def direct_met(self):
        return Vector2(0, 1)

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
