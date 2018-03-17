from game_engine.key_frames import KeyFrame
from game_engine.component import Component


class Animator(Component):

    def __init__(self, game_object, animation_list):
        """
        :param game_object:
        """
        self.animation_list = animation_list
        self.current_playing_animation = None
        self.animation_idx = 0
        for animation in self.animation_list:
            animation.set_animator(self)
        super().__init__(game_object)

    def play(self, animation_idx=0):
        """
        will play the list of animation in sequence
        :return:
        """
        self.animation_idx = animation_idx
        self.current_playing_animation = self.animation_list[self.animation_idx]

    def stop(self):
        self.current_playing_animation = None

    def update(self):
        if self.current_playing_animation is not None:
            self.current_playing_animation.update()

    def play_next_animation(self):
        self.animation_list[self.animation_idx].play(self.animation_idx)
