from game.scripts.scenes_controller_script import ScenesControllerScript
from game.scripts.constants import Constants


class GameSettings:

    game_name = "Balance"
    screen_width = Constants.screen_width
    screen_height = Constants.screen_height
    scenes_list = ScenesControllerScript.get_scenes()
