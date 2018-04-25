import pygame


class Input:

    engine = None
    is_pressing_left = False
    is_pressing_right = False
    is_pressing_space = False
    press_left_down = False
    press_right_down = False
    press_space_down = False

    @classmethod
    def update_input(cls, events):
        """
        find on the events list all events to update the input
        :param events: events list from pygame queue
        """
        cls.reset_keys()
        for event in events:
            if event.type == pygame.KEYDOWN:
                cls.__key_down(event)
            elif event.type == pygame.KEYUP:
                cls.__key_up(event)
            elif event.type == pygame.QUIT:
                cls.__quit_game()

    @classmethod
    def set_engine_reference(cls, class_ref):
        """
        Set the reference of engine class to this class
        :param class_ref: The reference to engine class
        """
        cls.engine = class_ref

    @classmethod
    def reset_keys(cls):
        """
        Press key down reset
        """
        cls.press_left_down = False
        cls.press_right_down = False
        cls.press_space_down = False

    @classmethod
    def __key_down(cls, event):
        """
        player started to press a key
        set it to true
        :param event: keydown event
        """
        if event.key == pygame.K_LEFT:
            cls.is_pressing_left = True
            cls.press_left_down = True
        if event.key == pygame.K_RIGHT:
            cls.is_pressing_right = True
            cls.press_right_down = True
        if event.key == pygame.K_SPACE:
            cls.is_pressing_space = True
            cls.press_space_down = True

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
        if event.key == pygame.K_SPACE:
            cls.is_pressing_space = False

    @classmethod
    def __quit_game(cls):
        """
        if pressed quit key
        call the engine's method to quit
        """
        cls.engine.end_game()
