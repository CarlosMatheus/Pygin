from game_engine.key_frames import KeyFrame
from game_engine.component import Component
from game_engine.time import Time
from pygame.math import Vector2


class Animation(Component):

    def __init__(self, game_object, key_frames, should_loop=True, num_of_loops="inf"):
        """
        :param game_object:
        """
        self.animator = None
        self.is_playing = False
        self.key_frames = key_frames
        self.interpolation = 0
        self.current_animation_time = 0.0
        self.current_kf_idx = 0
        self.current_loop = 0
        self.new_frame = True
        self.loop = should_loop
        self.num_of_loops = num_of_loops
        super().__init__(game_object)

    def set_animator(self, animator_obj):
        self.animator = animator_obj

    def reset(self):
        self.current_animation_time = 0.0
        self.current_kf_idx = 0
        self.current_loop = 0
        self.new_frame = True

    def __play(self):
        if self.key_frames[self.current_kf_idx].position is not None:
            if self.new_frame:
                self.max_distance_x = self.key_frames[self.current_kf_idx+1].position.x-\
                                        self.key_frames[self.current_kf_idx].position.x
                self.max_distance_y = self.key_frames[self.current_kf_idx + 1].position.y-\
                                      self.key_frames[self.current_kf_idx].position.y
                self.total_distance_x = 0.0
                self.total_distance_y = 0.0

            space_x = self.interpolation(self.key_frames[self.current_kf_idx].position.x,
                                            self.key_frames[self.current_kf_idx+1].position.x)
            distance_x = space_x - self.total_distance_x

            space_y = self.interpolation(self.key_frames[self.current_kf_idx].position.y,
                                            self.key_frames[self.current_kf_idx + 1].position.y)
            distance_y = space_y - self.total_distance_y

            if abs(self.total_distance_x + distance_x) > abs(self.max_distance_x):
                distance_x = self.max_distance_x - self.total_distance_x
                self.total_distance_x = self.total_distance_x
            else:
                self.total_distance_x += distance_x
            # if abs(self.total_distance_y + distance_y) > abs(self.max_distance_y):
            #     distance_y = self.max_distance_y - self.total_distance_y
            #     self.total_distance_y = self.max_distance_y
            # else:
            #     self.total_distance_y += distance_y
            if abs(self.current_animation_time - self.key_frames[self.current_kf_idx+1].time) < Time.delta_time()*(3/2):
                distance_y = self.max_distance_y - self.total_distance_y
                self.total_distance_y = self.max_distance_y
            else:
                self.total_distance_y += distance_y

            self.transform.translate(Vector2(self.transform.position.x + distance_x,
                                             self.transform.position.y + distance_y))
        if self.key_frames[self.current_kf_idx].rotation is not None:
            self.transform.rotate(self.key_frames[self.current_kf_idx].rotation)
        if self.key_frames[self.current_kf_idx].scale is not None:
            self.transform.scale = Vector2(self.key_frames[self.current_kf_idx].scale.x,
                                           self.key_frames[self.current_kf_idx].scale.y)
        if self.new_frame:
            self.new_frame = False

    def update(self):
        self.current_animation_time += Time.delta_time()
        if self.key_frames[self.current_kf_idx].time <= self.current_animation_time < self.key_frames[self.current_kf_idx+1].time:
            self.__set_interpolation(self.key_frames[self.current_kf_idx].interpolation)
            self.__play()
        else:
            print(self.current_animation_time)
            self.new_frame = True
            self.__next_key()
            self.__play()

    def __next_key(self):
        self.current_kf_idx += 1
        if self.current_kf_idx >= len(self.key_frames)-1:
            if self.__should_loop():
                print(self.transform.position.y)
                self.current_loop += 1
                self.current_kf_idx = 0
                self.current_animation_time = 0.0
            else:
                self.__end_animation()
        self.__set_interpolation(self.key_frames[self.current_kf_idx].interpolation)

    def __should_loop(self):
        if self.num_of_loops == "inf":
            return True
        else:
            return self.current_loop >= self.num_of_loops

    def __end_animation(self):
        self.animator.play_next_animation()

    def __set_interpolation(self, kind):
        """
        linear
        ease funcions
        :param kind:
        :return:
        """
        if kind == "linear":
            self.interpolation = self.__linear
        elif kind == "in_cubic":
            self.interpolation = self.__in_cubic
        elif kind == "out_cubic":
            self.interpolation = self.__out_cubic
        elif kind == "in_out_quint":
            self.interpolation = self.__in_out_quint
        elif kind == "in_back":
            self.interpolation = self.__in_back
        elif kind == "out_back":
            self.interpolation = self.__out_back
        elif kind == "in_out_back":
            self.interpolation = self.__in_out_back

    def __linear(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = tn
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __in_cubic(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = (tn**3)
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __out_cubic(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = (tn**(1/3))
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __in_out_quint(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2:
            tn = (t - t1) / (t2 - t1)
            vn = 3 * tn * tn
            v = (value2 - value1) * vn
            distance = v*Time.delta_time()
        else:
            distance = 0.0
        return distance

    def __in_back(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2:
            tn = (t - t1) / (t2 - t1)
            vn = 3 * tn * tn
            v = (value2 - value1) * vn
            distance = v*Time.delta_time()
        else:
            distance = 0.0
        return distance

    def __out_back(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2:
            tn = (t - t1) / (t2 - t1)
            vn = 3 * tn * tn
            v = (value2 - value1) * vn
            distance = v*Time.delta_time()
        else:
            distance = 0.0
        return distance

    def __in_out_back(self, value1, value2):
        t1 = self.key_frames[self.current_kf_idx].time
        t2 = self.key_frames[self.current_kf_idx + 1].time
        t = self.current_animation_time
        if t1 != t2:
            tn = (t - t1) / (t2 - t1)
            vn = 3 * tn * tn
            v = (value2 - value1) * vn
            distance = v*Time.delta_time()
        else:
            distance = 0.0
        return distance
