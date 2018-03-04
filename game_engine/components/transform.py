class Transform:

    def __init__(self, position_x, position_y, rotation, scale_x, scale_y):
        """
        Set the initial parameters
        :param position_x: game_object's x initial position
        :param position_y: game_object's y initial position
        :param rotation: game_object's initial rotation in degrees
        :param scale_x: game_object's x initial scale
        :param scale_y: game_object's y initial scale
        """
        self.translate = (position_x, position_y)
        self.rotate = rotation
        self.scale = (scale_x, scale_y)
