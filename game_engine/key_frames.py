from pygame.math import Vector2


class KeyFrame:

    def __init__(self, time, position=None, rotation=None, scale=None, layer=None, interpolation="in_cubic"):
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.layer = layer
        self.time = time
        self.interpolation = interpolation
