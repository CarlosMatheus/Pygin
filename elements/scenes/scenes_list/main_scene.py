from game_engine.scene import Scene
from game_engine.color import Color
from elements.normal_behaviors.game_objects.square_test import SquareTest
from elements.normal_behaviors.game_objects.square_test_falling import SquareTestFalling


class MainScene(Scene):

    def __init__(self):
        """
        Create the list of normal_behaviors and call the superclass constructor passing the list
        """
        self.normal_behaviors_list = [SquareTest(30, 40, 0, 50, 40, Color.white),
                                      SquareTestFalling(123, 234, 0, 12, 40, Color.red),
                                      SquareTestFalling(342, 123, 0, 50, 32, Color.red),
                                      SquareTestFalling(12, -123, 0, 50, 32, Color.red),
                                      SquareTestFalling(342, -232, 0, 50, 32, Color.red)
                                      ]
        super(MainScene, self).__init__(self.normal_behaviors_list)
