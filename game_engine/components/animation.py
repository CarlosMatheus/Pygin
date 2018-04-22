from game_engine.component import Component
from game_engine.time import Time
from pygame.math import Vector2


class Animation(Component):

    def __init__(self, game_object, key_frames, should_loop=True, num_of_loops="inf", unscaled=False):
        """
        Set every thing up for the animation
        :param game_object: the game object the called this
        :param key_frames: a list of keyframes that defines the animation
        :param should_loop: if it should loop
        :param num_of_loops: the number of times it should loop
        :param unscaled: if the time of this animation is unscaled
        """
        self.animator = None
        self.unscaled = unscaled
        self.is_playing = False
        self.key_frames = key_frames
        self.interpolation = None
        self.current_animation_time = 0.0
        self.total_parameter = dict()
        self.max_parameter = dict()
        self.current_kf_idx = 0
        self.current_loop = 0
        self.new_frame = True
        self.loop = should_loop
        self.num_of_loops = num_of_loops
        super().__init__(game_object)

    def update(self):
        """
        Method that will run every frame while this animation is running
        """
        self.current_animation_time += Time.delta_time(self.unscaled, self.game_object.time_scale)
        if self.should_change_key_frame():

            # todo remove this set interpolation

            self.__set_interpolation(self.key_frames[self.current_kf_idx].interpolation)
            self.__play_on_each_parameter()
        else:
            self.__next_key()
            self.new_frame = True
            self.__set_interpolation(self.key_frames[self.current_kf_idx].interpolation)
            self.__play_on_each_parameter()

    def should_change_key_frame(self):
        return (self.key_frames[self.current_kf_idx].time <= self.current_animation_time < self.key_frames[
            self.current_kf_idx + 1].time) and (self.current_kf_idx + 1 < len(self.key_frames))

    def not_out_of_key_frame(self):
        return self.current_kf_idx + 1 < len(self.key_frames)

    def set_animator(self, animator_obj):
        """
        set the reference of the animator
        :param animator_obj: The animator's reference
        """
        self.animator = animator_obj

    def reset(self):
        """
        reset the animation
        """
        self.current_animation_time = 0.0
        self.current_kf_idx = 0
        self.current_loop = 0
        self.new_frame = True

    def __play_on_each_parameter(self):
        """
        Do the modifications of that frame on each parameter
        If it is defined a change in a keyframe,
        the parameter will not be None and will occur a change
        """
        if self.animator.current_playing_animation is not None and self.not_out_of_key_frame():
            if self.key_frames[self.current_kf_idx].position is not None:
                max_x = self.key_frames[self.current_kf_idx + 1].position.x
                min_x = self.key_frames[self.current_kf_idx].position.x
                max_y = self.key_frames[self.current_kf_idx + 1].position.y
                min_y = self.key_frames[self.current_kf_idx].position.y
                distance_x = self.__play(min_x, max_x, "position_x")
                distance_y = self.__play(min_y, max_y, "position_y")
                self.transform.translate(Vector2(self.transform.position.x + distance_x,
                                                 self.transform.position.y + distance_y))

            if self.key_frames[self.current_kf_idx].rotation is not None:
                max_rotation = self.key_frames[self.current_kf_idx + 1].rotation
                min_rotation = self.key_frames[self.current_kf_idx].rotation
                dist_rotation = self.__play(min_rotation, max_rotation, "rotation")
                self.transform.rotation += dist_rotation

            if self.key_frames[self.current_kf_idx].scale is not None:
                max_x = self.key_frames[self.current_kf_idx + 1].scale.x
                min_x = self.key_frames[self.current_kf_idx].scale.x
                max_y = self.key_frames[self.current_kf_idx + 1].scale.y
                min_y = self.key_frames[self.current_kf_idx].scale.y
                dist_scale_x = self.__play(min_x, max_x, "scale_x")
                dist_scale_y = self.__play(min_y, max_y, "scale_y")
                self.transform.scale.x = self.transform.scale.x + dist_scale_x
                self.transform.scale.y = self.transform.scale.y + dist_scale_y

            if self.key_frames[self.current_kf_idx].alpha is not None:
                max_alpha = self.key_frames[self.current_kf_idx + 1].alpha
                min_alpha = self.key_frames[self.current_kf_idx].alpha
                dist_alpha = self.__play(min_alpha, max_alpha, "alpha")
                self.game_object.material.alpha += dist_alpha

            if self.new_frame:
                self.new_frame = False

    def __play(self, value_min, value_max, value_name):
        """
        Calculate the difference that must be add at this frame to a parameter in this frame
        :param value_min: the value in the keyframe before this time
        :param value_max: the value in the keyframe after this time
        :param value_name: a string that specify the name of value
        """
        if self.new_frame:
            self.max_parameter[value_name] = value_max - value_min
            self.total_parameter[value_name] = 0.0

        interpolated_value = self.interpolation(self.current_animation_time, value_min, value_max,
                                                self.key_frames[self.current_kf_idx].time,
                                                self.key_frames[self.current_kf_idx + 1].time)

        dist_value = interpolated_value - self.total_parameter[value_name]
        if self.__is_end_of_key_frame():
            dist_value = self.max_parameter[value_name] - self.total_parameter[value_name]
            self.total_parameter[value_name] = self.max_parameter[value_name]
        else:
            self.total_parameter[value_name] += dist_value

        return dist_value

    def __next_key(self):
        """
        Change to next key frame in keyframe list
        """
        self.current_kf_idx += 1
        if self.current_kf_idx >= len(self.key_frames)-1:
            self.__next_loop()

    def __next_loop(self):
        if self.__should_loop():
            self.current_loop += 1
            self.current_kf_idx = 0
            self.current_animation_time = 0.0
        else:
            self.__end_animation()

    def __should_loop(self):
        """
        Verify whether it should loop or not
        """
        if self.loop:
            if self.num_of_loops == "inf":
                return True
            else:
                return self.current_loop >= self.num_of_loops
        else:
            return False

    def __end_animation(self):
        """
        end this animation
        """
        self.animator.play_next_animation()

    def __is_end_of_key_frame(self):
        """
        Verify if it is the end of a keyframe
        """
        return abs(self.current_animation_time - self.key_frames[self.current_kf_idx + 1].time)\
               < Time.delta_time(self.unscaled, self.game_object.time_scale) * (3 / 2)

    def __set_interpolation(self, kind):
        """
        Will define which interpolation will be made between the two points
        linear function: just a linear interpolation between the two points
        ease funcions: in_cubic, out_cubic, in_out_quint
        You can see demos of how these ease interpolation happens:
        http://easings.net/
        :param kind: the string specifing the interpolation
        """
        if kind == "linear":
            self.interpolation = self.__linear
        elif kind == "in_cubic":
            self.interpolation = self.__in_cubic
        elif kind == "out_cubic":
            self.interpolation = self.__out_cubic
        elif kind == "in_out_quint":
            self.interpolation = self.__in_out_quint

    def __linear(self, t, value1, value2, t1, t2):
        """
        Linear interpolation
        Constant variation in time
        :param t: current time
        :param value1: function upper bounder result value
        :param value2: function lower bounder result value
        :param t1: function upper bounder time value
        :param t2: function lower bounder time value
        :return: the result value for that given time
        """
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = tn
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __in_cubic(self, t, value1, value2, t1, t2):
        """
        Cubic with time
        slow at the begging and fast at end
        :param t: current time
        :param value1: function upper bounder result value
        :param value2: function lower bounder result value
        :param t1: function upper bounder time value
        :param t2: function lower bounder time value
        :return: the result value for that given time
        """
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = (tn**3)
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __out_cubic(self, t, value1, value2, t1, t2):
        """
        Cubic with time
        fast at the begging and slow at end
        :param t: current time
        :param value1: function upper bounder result value
        :param value2: function lower bounder result value
        :param t1: function upper bounder time value
        :param t2: function lower bounder time value
        :return: the result value for that given time
        """
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = (1-(1-tn)**3)
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f

    def __in_out_quint(self, t, value1, value2, t1, t2):
        """
        5th power with time
        slow at the begging, fast at the middle and slow at end
        :param t: current time
        :param value1: function upper bounder result value
        :param value2: function lower bounder result value
        :param t1: function upper bounder time value
        :param t2: function lower bounder time value
        :return: the result value for that given time
        """
        if t1 != t2 and abs(t - t1) > 0.01:
            tn = (t - t1) / (t2 - t1)
            fn = (tn*tn*tn*(tn*(6*tn-15)+10))
            f = (value2 - value1) * fn
        else:
            f = 0.0
        return f
