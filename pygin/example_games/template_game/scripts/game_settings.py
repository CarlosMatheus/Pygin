from .scenes_script import ScenesScript

class GameSettings:
    game_name = "default"
    screen_width = 500
    screen_height = 500
    scenes_list = ScenesScript.get_scenes()
