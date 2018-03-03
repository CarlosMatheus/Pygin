import pygame

class Engine:

    game_display = 0
    screen_width = 300
    screen_height = 600

    @staticmethod
    def start_game(game_name):
        pygame.init()
        Engine.game_display = pygame.display.set_mode( (Engine.screen_width, Engine.screen_height) )
        pygame.display.set_caption(game_name)


    @staticmethod
    def end_game():
        asdf = 0


