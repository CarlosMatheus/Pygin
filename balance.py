from game_engine.engine import Engine
from elements.scenes.scenes_controller import ScenesController

game_name = "Balance"

Engine.start_game(game_name, ScenesController.get_scenes())
