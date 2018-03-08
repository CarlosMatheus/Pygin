from game_engine.components.box_collider import BoxCollider
from elements.game_objects.game_objects.basic_objects.basic_rectangle import BasicRectangle
from game_engine.game_object import GameObject
from game_engine.engine import Engine
from game_engine.time import Time
from pygame.math import Vector2


class Rectangle(BasicRectangle):

    def __init__(self, position, dimension, material):
        """
        Add the rectangle mash component
        Call the superclass constructor passing basic game_object parameters
        :param position_x: initial position x of the rectangle
        :param position_y: initial position y of the rectangle
        :param width: initial width of the rectangle
        :param height: initial height of the rectangle
        :param color: initial color of the rectangle
        """
        self.box_collider = BoxCollider(self)
        super(Rectangle, self).__init__(position, dimension, material)

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
        return self.transform.position.y > Engine.screen_height


    def fall(self):
        """
        make the rectangle fall with constant velocity
        """
        self.transform.translate(Vector2(self.transform.position.x,
                                         self.transform.position.y + self.fall_velocity * Time.delta_time()))