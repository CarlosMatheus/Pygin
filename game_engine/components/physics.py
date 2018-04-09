from game_engine.component import Component
from game_engine.time import Time
from pygame.math import Vector2


class Physics(Component):

    def __init__(self, game_object, mass=None, gravity=0, velocity=Vector2(0, 0), acceleration=Vector2(0, 0),
                 angular_velocity=0, angular_acceleration=0):
        super(Physics, self).__init__(game_object)
        gravity *= 10
        self.mass = mass
        self.velocity = velocity
        self.acceleration = acceleration
        self.angular_velocity = angular_velocity
        self.angular_acceleration = angular_acceleration
        self.gravity = gravity
        self.inst_velocity = velocity
        p = self.transform.position
        t = Time.delta_time()
        self.position_vect = [Vector2(p.x, p.y), Vector2(p.x, p.y), Vector2(p.x, p.y)]
        self.time_vect = [t, t, t]

    def get_inst_velocity(self):
        return self.inst_velocity

    def __update(self):
        self.__update_velocity()
        self.__update_position()
        self.__update_angular_velocity()
        self.__update_rotation()
        self.__update_inst_velocity()

    def __update_inst_velocity(self):
        del self.time_vect[0]
        self.time_vect.append(Time.delta_time())
        del self.position_vect[0]
        self.position_vect.append(Vector2(self.transform.position.x, self.transform.position.y))
        dir = self.position_vect[2] - self.position_vect[0]
        t = self.time_vect[0] + self.time_vect[1] + self.time_vect[2]
        if t == 0:
            self.inst_velocity = Vector2(0, 0)
        else:
            self.inst_velocity = dir / t

    def __update_position(self):
        new_position = Vector2(self.transform.position.x + (self.velocity.x * Time.delta_time()),
                               self.transform.position.y + (self.velocity.y * Time.delta_time()))
        self.transform.translate(new_position)

    def __update_velocity(self):
        self.velocity.x = self.velocity.x + (self.acceleration.x * Time.delta_time())
        self.velocity.y = self.velocity.y + ((self.acceleration.y + self.gravity) * Time.delta_time())

    def __update_angular_velocity(self):
        self.angular_velocity = self.angular_velocity + (self.angular_acceleration * Time.delta_time())

    def __update_rotation(self):
        self.transform.rotate(self.angular_velocity * Time.delta_time())
