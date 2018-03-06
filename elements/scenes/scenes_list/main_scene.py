from game_engine.scene import Scene
from game_engine.color import Color
from elements.normal_behaviors.game_objects.rectangle import Rectangle
from elements.normal_behaviors.game_objects.circle import Circle
from elements.normal_behaviors.game_objects.square_test import SquareTest
from elements.normal_behaviors.game_objects.square_test_falling import SquareTestFalling


class MainScene(Scene):

    def __init__(self):
        self.game_object_list = [Circle(100, 480, 20, (253, 102, 0)),
                                 Circle(260, 480, 20, (0, 120, 255))
                                 ]
        super(MainScene, self).__init__(self.game_object_list)
