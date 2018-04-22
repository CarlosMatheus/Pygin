from game_engine.components.physics import Physics
from game_engine.component import Component
from game_engine.time import Time
from pygame.math import Vector2
import random
import math


class ParticleSystem(Component):

    def __init__(self,
                 game_object,
                 spawn_game_obj_class,
                 layer=0,
                 quant=1,
                 quant_proport_to_len=False,
                 period=0.05,
                 vel_min=80,
                 vel_max=160,
                 duration=1.0,
                 gravity=0,
                 inherit_vel=False,
                 inherit_vel_mult=1,
                 spawn_prob="lin",
                 vel_prob="lin",
                 unscaled=False
                 ):
        super().__init__(game_object)
        self.duration = duration
        self.gravity = gravity
        self.vel_min = vel_min
        self.layer = layer
        self.vel_max = vel_max
        self.inherit_vel = inherit_vel
        self.quant_proport_to_len = quant_proport_to_len
        self.inherit_vel_mult = inherit_vel_mult
        self.quant = quant
        self.turned_on = False
        self.period = period
        self.spawn_game_obj_class = spawn_game_obj_class
        self.last_time = Time.now()
        self.ini_point_method = None
        self.fin_point_method = None
        self.generation_mode = None
        self.obj_list = list()
        self.spawn_prob = None
        self.vel_prob = None
        self.define_vel_prob(vel_prob)
        self.define_spawn_prob(spawn_prob)
        self.unscaled = unscaled
        if self.inherit_vel:
            if self.game_object.physics is None:
                self.game_object.physics = Physics(self.game_object)

    def set_line_gen(self, ini_point_method, fin_point_method):
        self.ini_point_method = ini_point_method
        self.fin_point_method = fin_point_method
        self.generation_mode = self.set_line_gen

    def set_circ_gen(self, center_point, radius, mode="radial", ini_angle_met=None, fin_angle_met=None, direct_met=None):
        if ini_angle_met is None:
            self.ini_angle_met = self.default_ini_ang_met
        else:
            self.ini_angle_met = ini_angle_met
        if fin_angle_met is None:
            self.fin_angle_met = self.default_fin_ang_met
        else:
            self.fin_angle_met = fin_angle_met
        self.direct_met = direct_met
        self.center_point = center_point
        self.radius = radius
        self.mode = mode
        self.generation_mode = self.set_circ_gen

    def default_ini_ang_met(self):
        return 0

    def default_fin_ang_met(self):
        return 360

    def play(self):
        self.turned_on = True
        self.destroy_timer = Time.now()
        self.last_time = Time.now()

    def stop(self):
        self.turned_on = False

    def define_spawn_prob(self, spawn_prob):
        if spawn_prob == "lin":
            self.spawn_prob = self.__linear_prob_func
        elif spawn_prob == "parab":
            self.spawn_prob = self.__parabolic_spawn_prob_func

    def define_vel_prob(self, vel_prob):
        if vel_prob == "lin":
            self.vel_prob = self.__lin_vel_prob_func
        elif vel_prob == "parab":
            self.vel_prob = self.__parabolic_vel_prob_func

    def __update(self):
        if self.turned_on:
            if self.should_spawn():
                if self.quant_proport_to_len:
                    quant = math.ceil(self.fin_point_method().distance_to(self.ini_point_method()) * self.quant)
                else:
                    quant = int(self.quant)
                for i in range(quant):
                    spawn_location = None
                    obj_velocity_vect = None
                    spawn_prob = self.spawn_prob()
                    vel_prob = self.vel_prob(spawn_prob)
                    if self.generation_mode == self.set_line_gen:
                        spawn_location = (self.fin_point_method() - self.ini_point_method()) * spawn_prob + self.ini_point_method()
                        velocity = random.randint(int(self.vel_min*1000), int(self.vel_max*1000))/1000
                        obj_velocity_vect = (self.fin_point_method() - self.ini_point_method()).normalize().rotate(90)*velocity
                    elif self.generation_mode == self.set_circ_gen:
                        normal = Vector2(1, 0).rotate((self.fin_angle_met() - self.ini_angle_met()) * spawn_prob + self.ini_angle_met())
                        spawn_location = self.center_point + normal * self.radius

                        velocity = random.randint(int(self.vel_min * 1000), int(self.vel_max * 1000)) / 1000

                        if self.mode == "radial":
                            obj_velocity_vect = normal * velocity * vel_prob
                        elif self.mode == "directional":
                            obj_velocity_vect = self.direct_met() * velocity * vel_prob
                        else:
                            raise Exception("Unknown mode {0}".format(str(self.mode)))


                    obj = self.spawn_game_obj_class(spawn_location)
                    if self.inherit_vel:
                        obj.physics = Physics(obj, velocity=(obj_velocity_vect + self.game_object.physics.inst_velocity*self.inherit_vel_mult))
                    else:
                        obj.physics = Physics(obj, velocity=(obj_velocity_vect))

                    obj.physics.gravity = self.gravity

                    obj.transform.layer = self.layer

                    obj.set_creator_object(self.game_object)

                    obj.destroy_time = self.duration

                    if self.unscaled == True:
                        if obj.animator is not None:
                            for animation in obj.animator.animation_list:
                                animation.unscaled = self.unscaled
                        if obj.physics is not None:
                            obj.physics.unscaled = self.unscaled

                    self.obj_list.append(obj)
                    self.destroy_first()

    def destroy_first(self):
        if Time.now() - self.destroy_timer > self.duration:
            self.obj_list[0].destroy_me()
            del self.obj_list[0]

    def __circular_prob_func(self):
        # line going from 0 to 1
        angle = random.randint(0, 180)

        rad = angle * math.pi / 180
        if angle < 90:
            return (1 - math.cos(rad)) / 2
        else:
            return (1 - math.cos(rad)) / 2

    def __parabolic_spawn_prob_func(self):
        x = random.randint(0, 100)
        odd = random.randint(0, 100)
        if odd < 50:
            return ((-1)*math.sqrt(x/100)+1)/2
        else:
            return (math.sqrt(x/100)+1)/2

    def __gauss_prob_func(self):
        return max(min(random.gauss(0.5, 0.25), 1.0), 0.0)

    def __lin_vel_prob_func(self, x):
        return 1

    def __parabolic_vel_prob_func(self, x):
        return 4 * (x - 0.5) * (x - 0.5)

    def __linear_prob_func(self):
        return random.randint(0, 1000)/1000.0

    def should_spawn(self):
        if (Time.now() - self.last_time) > self.period:
            self.last_time = Time.now()
            return True
        else:
            return False
