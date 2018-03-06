from game_engine.time import Time
from game_engine.game_object import GameObject
from game_engine.engine import Engine


class SquareTestFalling(GameObject):

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
