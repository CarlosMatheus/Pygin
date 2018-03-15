import pygame
import asyncio


class Time:
    ioloop = asyncio.get_event_loop()
    last_frame_tick = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    tasks = []

    @classmethod
    def start_game(cls):
        """
        Run the coroutine tasks list
        """
        cls.ioloop.run_until_complete(asyncio.wait(cls.tasks))
        cls.ioloop.close()

    @classmethod
    def start_coroutine(cls, method):
        """
        Add a method to be run simultaneously along the game
        :param method: The async method that will be added to the task list
        """
        cls.tasks.append(cls.ioloop.create_task(method()))

    @classmethod
    def end_of_start(cls):
        """
        Set the time at the moment to get_ticks_last_frame
        """
        cls.last_frame_tick = pygame.time.get_ticks()
        cls.clock.tick(200)

    @classmethod
    def end_of_loop(cls):
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

    @classmethod
    def now(cls):
        """
        :return: the time right now in seconds, based on how long the game is running
        """
        return pygame.time.get_ticks()/1000
