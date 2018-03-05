from game_engine.time import Time
from game_engine.game_object import GameObject


class SquareTestFalling(GameObject):

    def start(self):
        """
        NomalBehaivor start method
        will be called when the object is instantiate on scene
        """
        self.fall_velocity = 25

    def update(self):
        """
        NomalBehaivor update method
        will be call every frame
        """
        self.fall()

    def fall(self):
        """
        make the rectangle fall with constant velocity
        """
        self.transform.translate = (self.transform.translate[0],
                                    self.transform.translate[1] + self.fall_velocity * Time.delta_time())
