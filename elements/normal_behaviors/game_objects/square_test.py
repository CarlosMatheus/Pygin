from game_engine.input import Input
from game_engine.time import Time
from game_engine.game_object import GameObject


class SquareTest(GameObject):

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.move_velocity = 200
        self.fall_velocity = 50

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        if Input.is_pressing_right:
            self.move_right()
        if Input.is_pressing_left:
            self.move_left()
        self.fall()

    def move_right(self):
        """
        Move the rectangle right
        """
        self.transform.translate = (self.transform.translate[0] + self.move_velocity * Time.delta_time(),
                                    self.transform.translate[1])

    def move_left(self):
        """
        Move the rectangle left
        """
        self.transform.translate = (self.transform.translate[0] - self.move_velocity * Time.delta_time(),
                                    self.transform.translate[1])

    def fall(self):
        """
        make the rectangle fall with constant velocity
        """
        self.transform.translate = (self.transform.translate[0],
                                    self.transform.translate[1] + self.fall_velocity * Time.delta_time())
