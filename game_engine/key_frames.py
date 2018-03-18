class KeyFrame:

    def __init__(self, time, position=None, rotation=None, scale=None, layer=None, alpha=None, interpolation="in_cubic"):
        """
        Define one key_frame that will compound a list of key_frames that will be passed to an animation
        :param time:
        :param position:
        :param rotation:
        :param scale:
        :param layer:
        :param alpha:
        :param interpolation:
        """
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.layer = layer
        self.alpha = alpha
        self.time = time
        self.interpolation = interpolation
