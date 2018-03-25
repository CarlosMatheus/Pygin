from game_engine.components.polygon_collider import PolygonCollider
from game_engine.basic_objects.basic_rectangle import BasicRectangle
from game_engine.game_object import GameObject
from game_engine.time import Time
from pygame.math import Vector2
from balance.scripts.constants import Constants


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material):
        """
        Add the rectangle mesh component
        Call the superclass constructor passing basic game_object parameters
        :param position.x: initial position x of the rectangle
        :param position.y: initial position y of the rectangle
        :param dimension.x: initial width of the rectangle
        :param dimension.y: initial height of the rectangle
        :param material: initial color of the rectangle
        """
        super(Rectangle, self).__init__(position, dimension, material, layer=1)
        self.polygon_collider = PolygonCollider(self)

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
        return self.transform.position.y > Constants.screen_height


    def fall(self):
        """
        make the rectangle fall with constant velocity
        """
        self.transform.translate(Vector2(self.transform.position.x,
                                         self.transform.position.y + self.fall_velocity * Time.delta_time()))