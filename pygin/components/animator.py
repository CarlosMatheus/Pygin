from pygin.component import Component


class Animator(Component):

    def __init__(self, game_object, animation_list):
        """
        Initiate Animator with the animation list
        :param game_object: the list of animations for this animator
        """
        self.animation_list = animation_list
        self.current_playing_animation = None
        self.animation_idx = 0
        self.is_paused = False
        for animation in self.animation_list:
            animation.set_animator(self)
        super().__init__(game_object)

    def play(self, animation_idx=0, should_loop=False, loops="inf"):
        """
        will play the list of animation in sequence
        """
        self.should_loop = should_loop
        self.loops = loops
        self.current_loop = 0
        self.animation_idx = animation_idx
        self.current_playing_animation = self.animation_list[self.animation_idx]
        self.animation_list[self.animation_idx].reset()

    def play_next_animation(self):
        """
        Play the next animation on animation list
        It checks before if it can play and if it should loop
        """
        if self.animation_idx < len(self.animation_list)-1:
            self.__next()
        elif self.should_loop:
            self.__loop()
        else:
            self.stop()

    def pause(self):
        """
        pause animation
        """
        self.is_paused = True

    def resume(self):
        """
        Resume animation from where it stopped
        """
        self.is_paused = False

    def stop(self):
        """
        stop playing animation
        """
        self.current_playing_animation = None

    def __next(self):
        """
        play next animation
        """
        self.animation_idx += 1
        self.current_playing_animation = self.animation_list[self.animation_idx]
        self.animation_list[self.animation_idx].reset()

    def __loop(self):
        """
        loop in animation list
        """
        if self.loops is "inf":
            self.play()
        else:
            if self.loops > self.current_loop:
                self.current_loop += 1
                self.play()
            else:
                self.stop()

    def __update(self):
        """
        This will run every frame
        Will update the current animation
        """
        if (self.current_playing_animation is not None) and (not self.is_paused):
            self.current_playing_animation.update()
