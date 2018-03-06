from game_engine.scene import Scene
from game_engine.color import Color
from elements.normal_behaviors.game_objects.rectangle import Rectangle
from elements.normal_behaviors.game_objects.square_test import SquareTest
from elements.normal_behaviors.game_objects.square_test_falling import SquareTestFalling


class MainScene(Scene):

    def __init__(self):
        self.game_object_list = [Rectangle(30, 40, 50, 40, 32),
                                 SquareTestFalling(123, 234, 0, 12, 40),
                                 SquareTestFalling(342, 123, 0, 50, 32),
                                 SquareTestFalling(12, -123, 0, 50, 32),
                                 SquareTestFalling(342, -232, 0, 50, 32)
                                 ]
        super(MainScene, self).__init__(self.game_object_list)
