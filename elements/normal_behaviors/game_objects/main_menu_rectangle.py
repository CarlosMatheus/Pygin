from game_engine.components.rectangle_mash import RectangleMash
from game_engine.game_object import GameObject
from game_engine.engine import Engine
from game_engine.time import Time


class Rectangle(GameObject):

    def __init__(self, position_x, position_y, width, height, color):
        """
        Add the rectangle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the rectangle
        :param position_y: initial position y of the rectangle
        :param width: initial width of the rectangle
        :param height: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        self.rectangle_mash = RectangleMash(position_x, position_y, width, height, color)
        super(Rectangle, self).__init__(position_x, position_y, 0, 1, 1)

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.fall_velocity = 250

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        if self.is_out_of_screen():
            GameObject.destroy(self)
        self.fall()

    def is_out_of_screen(self):

        return self.transform.translate[1] > Engine.screen_height

    def fall(self):
        """
        make the rectangle fall with constant velocity
        """
        self.transform.translate = (self.transform.translate[0],
                                    self.transform.translate[1] + self.fall_velocity * Time.delta_time())