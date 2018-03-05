import pygame


class Time:
    last_frame_tick = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    @classmethod
    def end_of_loop(cls):
        """
        Set the time at the moment to get_ticks_last_frame
        """
        cls.last_frame_tick = pygame.time.get_ticks()
        cls.clock.tick(200)

    @classmethod
    def end_of_start(cls):
        """
        Set the time at the moment to get_ticks_last_frame
        """
        cls.last_frame_tick = pygame.time.get_ticks()
        cls.clock.tick(200)

    @classmethod
    def delta_time(cls):
        """
        :return: the duration of that frame in seconds
        """
        if cls.clock.get_fps() != 0:
            return 1/cls.clock.get_fps()
        else:
            return 0
