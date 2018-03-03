import pygame


class Time:
    get_ticks_last_frame = pygame.time.get_ticks()

    @classmethod
    def end_of_loop(cls):
        """
        Set the time at the moment to get_ticks_last_frame
        """
        cls.get_ticks_last_frame = pygame.time.get_ticks()

    @classmethod
    def end_of_start(cls):
        """
        Set the time at the moment to get_ticks_last_frame
        """
        cls.get_ticks_last_frame = pygame.time.get_ticks()

    @classmethod
    def delta_time(cls):
        """
        :return: the duration of that frame in seconds
        """
        return (pygame.time.get_ticks() - cls.get_ticks_last_frame) / 1000.0

