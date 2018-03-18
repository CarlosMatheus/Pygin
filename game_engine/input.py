import pygame


class Input:

    engine = None
    is_pressing_left = False
    is_pressing_right = False

    @classmethod
    def update_input(cls, events):
        """
        find on the events list all events to update the input
        :param events: events list from pygame queue
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                cls.__key_down(event)
            elif event.type == pygame.KEYUP:
                cls.__key_up(event)
            elif event.type == pygame.QUIT:
                cls.__quit_game()

    @classmethod
    def set_engine_reference(cls, class_ref):
        cls.engine = class_ref

    @classmethod
    def __key_down(cls, event):
        """
        player started to press a key
        set it to true
        :param event: keydown event
        """
        if event.key == pygame.K_LEFT:
            cls.is_pressing_left = True
        if event.key == pygame.K_RIGHT:
            cls.is_pressing_right = True

    @classmethod
    def __key_up(cls, event):
        """
        player stopped to press a key
        set it to false
        :param event: keyup event
        """
        if event.key == pygame.K_LEFT:
            cls.is_pressing_left = False
        if event.key == pygame.K_RIGHT:
            cls.is_pressing_right = False

    @classmethod
    def __quit_game(cls):
        """
        if pressed quit key
        call the engine's method to quit
        """
        cls.engine.end_game()
