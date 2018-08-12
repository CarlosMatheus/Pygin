from game_engine.basic_objects.basic_circle import BasicCircle
from game_engine.basic_objects.basic_rectangle import BasicRectangle
from Balance.game_objects.mesh_objects.star import Star
from Balance.animations.circle_player_initial_animation import CirclePlayerInitialAnimation
from game_engine.components.particle_system import ParticleSystem
from Balance.game_objects.mesh_objects.particle import Particle
from game_engine.components.animator import Animator
from game_engine.game_object import GameObject
from game_engine.components.circle_collider import CircleCollider
from Balance.game_objects.mesh_objects.get_power_up_effect import GetPowerUpEffect
from Balance.game_objects.mesh_objects.die_effect import DieEffect
from game_engine.components.physics import Physics
from Balance.animations.player_bounce import PlayerBounce
from game_engine.color import Color
from pygame import mixer
from pygame.math import Vector2


class PlayerCircle(BasicCircle):

    def __init__(self, position, radius, material):
        super(PlayerCircle, self).__init__(position, radius, material, layer=-2)
        self.circle_collider = CircleCollider(self)
        self.is_invencible = False
        self.is_not_dying = True

    def start(self):
        self.physics = Physics(self)
        self.star_score_controller = GameObject.find_by_type("StarScoreController")[0]
        self.main_scene_controller = GameObject.find_by_type("MainSceneController")[0]
        self.invencible_power_up_controller = GameObject.find_by_type("InvenciblePowerUpController")[0]
        self.animation = CirclePlayerInitialAnimation(self)
        self.animator = Animator(self, [self.animation])
        self.death_sound = mixer.Sound('Balance/assets/soundtrack/ball_death_01.ogg')
        self.particle_system = ParticleSystem(self, Particle, quant=5, period=0.07,
                                              vel_min=30, vel_max=200, duration=0.5,
                                              inherit_vel=True, inherit_vel_mult=-0.7)
        self.particle_system.set_circ_gen(self.transform.position, self.circle_mesh.get_radius(), mode="directional",
                                          direct_met=self.direct_met, ini_angle_met=self.ini_angle_met,
                                          fin_angle_met=self.fin_angle_met)
        self.particle_system.play()


    def ini_angle_met(self):
        return 0 + Vector2(1, 0).angle_to(self.physics.inst_velocity)

    def fin_angle_met(self):
        return 180 + Vector2(1, 0).angle_to(self.physics.inst_velocity)

    def direct_met(self):
        return Vector2(0, 1)

    def update(self):
        self.check_collision()

    def check_collision(self):
        (collided, game_obj) = self.circle_collider.on_collision()
        if collided:
            if issubclass(type(game_obj), BasicRectangle) and not self.is_invencible and game_obj.collidable:
                self.main_scene_controller.game_over()
                self.die()
            elif issubclass(type(game_obj), Star):
                GetPowerUpEffect(position=game_obj.transform.position, material=game_obj.material)
                game_obj.die()
                self.star_score_controller.get_star()
            elif issubclass(type(game_obj), BasicCircle):
                GetPowerUpEffect(position=game_obj.transform.position, material=game_obj.material)
                game_obj.die()
                self.invencible_power_up_controller.get_power_up()

    def die(self):
        if self.is_not_dying:
            self.death_sound.play()
            self.is_not_dying = False
            self.particle_system.stop()
            inst_vel = self.physics.inst_velocity
            r = self.circle_mesh.get_radius()
            for i in range(7):
                DieEffect(self.transform.position, self.material, 1 + r*i/6, inst_vel=inst_vel)
            self.material.alpha = 0
